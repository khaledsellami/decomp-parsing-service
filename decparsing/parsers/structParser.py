import logging
from typing import List, Tuple

import numpy as np
import pandas as pd

from ..models import analyze_pb2 as apb
from ..utils import handle_duplicates


class StructParser:
    def __init__(self, classes: List[apb.Class_] = None, methods: List[apb.Method_] = None, is_distributed=False):
        self.classes = classes
        self.methods = methods
        self.is_distributed = is_distributed
        self.logger = logging.getLogger(__name__)

    def get_class_names(self) -> List[str]:
        if self.classes is None:
            return []
        elif self.is_distributed:
            names = [class_.serviceName.replace(" ", "") + "." + class_.fullName for class_ in self.classes]
        else:
            names = [class_.fullName for class_ in self.classes]
        return handle_duplicates(names)

    def get_method_names(self) -> List[str]:
        if self.methods is None:
            return []
        elif self.is_distributed:
            names = [method_.serviceName.replace(" ","") + "." + method_.fullName for method_ in self.methods]
        else:
            names = [method_.fullName for method_ in self.methods]
        return handle_duplicates(names)

    def find_class(self, name: str, service_name: str = None) -> Tuple[int, apb.Class_]:
        assert not (self.is_distributed and (service_name is None))
        for i, class_ in enumerate(self.classes):
            if class_.fullName == name:
                if self.is_distributed:
                    if class_.serviceName == service_name:
                        return i, class_
                else:
                    return i, class_
        return -1, None

    def get_calls(self, level: str = "class") -> pd.DataFrame:
        assert level in ["class", "method"]
        calls, method_calls = self._get_calls()
        return calls if level == "class" else method_calls

    def _get_calls(self) -> Tuple[pd.DataFrame, pd.DataFrame]:
        # TODO optimize
        assert self.classes is not None and self.methods is not None
        class_names = self.get_class_names()
        method_names = self.get_method_names()
        calls = np.zeros((len(self.classes), len(self.classes)))
        method_calls = np.zeros((len(self.methods), len(self.methods)))
        for i, method_ in enumerate(self.methods):
            if self.is_distributed:
                m, class_ = self.find_class(method_.parentName, method_.serviceName)
            else:
                m, class_ = self.find_class(method_.parentName, None)
            if class_ is None:
                raise ValueError("Class " + method_.parentName + " was not found!")
            # assert method_.fullName in [class_.fullName + "::" + m for m in
            #                                class_.methods + class_["constructors"]]
            for invocation_ in method_.localInvocations:
                ref_method_name = invocation_.invokedObject + "::" + invocation_.invokedMethod
                if self.is_distributed:
                    ref_method_name = method_.serviceName.replace(" ", "") + "." + ref_method_name
                if ref_method_name in method_names:
                    j = method_names.index(ref_method_name)
                    method_calls[i, j] += 1
                else:
                    self.logger.error("failed to find local method: " + ref_method_name)
                invoked_class_ = invocation_.invokedObject
                if self.is_distributed:
                    invoked_class_ = method_.serviceName.replace(" ", "") + "." + invoked_class_
                if invoked_class_ in class_names:
                    if self.is_distributed:
                        n, ref_class_ = self.find_class(invocation_.invokedObject, method_.serviceName)
                    else:
                        n, ref_class_ = self.find_class(invocation_.invokedObject, None)
                    if ref_class_ is None:
                        raise ValueError("Class " + invocation_.invokedObject + " was not found!")
                    calls[m, n] += 1
        for i, class_ in enumerate(self.classes):
            for method_ in class_.fieldCalls:
                ref_class_ = method_.invokedObject
                if self.classes:
                    ref_class_ = class_.serviceName.replace(" ", "") + "." + ref_class_
                if ref_class_ in class_names:
                    j = class_names.index(ref_class_)
                    calls[i, j] += 1
        calls = pd.DataFrame(calls, columns=class_names, index=class_names)
        method_calls = pd.DataFrame(method_calls, columns=method_names, index=method_names)
        return calls, method_calls

    def get_references(self) -> pd.DataFrame:
        # TODO optimize
        assert self.classes is not None and self.methods is not None
        class_names = self.get_class_names()
        references = np.zeros((len(self.classes), len(self.classes)))
        for i, method_ in enumerate(self.methods):
            if self.is_distributed:
                m, class_ = self.find_class(method_.parentName, method_.serviceName)
            else:
                m, class_ = self.find_class(method_.parentName, None)
            if class_ is None:
                raise ValueError("Class " + method_.parentName + " was not found!")
            # assert method_.fullName in [class_.fullName + "::" + m for m in
            #                                class_.methods + class_.constructors]
            for reference in method_.referencedTypes:
                if self.is_distributed:
                    reference = method_.serviceName.replace(" ", "") + "." + reference
                if reference in class_names:
                    n = class_names.index(reference)
                    references[m, n] += 1
        for i, class_ in enumerate(self.classes):
            for reference in class_.referencedTypes:
                if self.is_distributed:
                    reference = class_.serviceName.replace(" ", "") + "." + reference
                if reference in class_names:
                    j = class_names.index(reference)
                    references[i, j] = max(references[i, j], 1)
        references = pd.DataFrame(references, columns=class_names, index=class_names)
        return references

    def get_interactions(self) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        # TODO optimize
        assert self.classes is not None and self.methods is not None
        class_names = self.get_class_names()
        field_usage = np.zeros((len(self.classes), len(self.classes)))
        parameter_usage = np.zeros((len(self.classes), len(self.classes)))
        return_usage = np.zeros((len(self.classes), len(self.classes)))
        nested_usage = np.zeros((len(self.classes), len(self.classes)))
        inheritance_usage = np.zeros((len(self.classes), len(self.classes)))
        for i, class_ in enumerate(self.classes):
            # field_usage
            for ref_class_ in class_.fieldTypes:
                if self.is_distributed:
                    ref_class_ = class_.serviceName.replace(" ", "") + "." + ref_class_
                if ref_class_ in class_names:
                    j = class_names.index(ref_class_)
                    field_usage[i, j] += 1
            # parameter_usage
            for ref_class_ in class_.parameterTypes:
                if self.is_distributed:
                    ref_class_ = class_.serviceName.replace(" ", "") + "." + ref_class_
                if ref_class_ in class_names:
                    j = class_names.index(ref_class_)
                    parameter_usage[i, j] += 1
            # return_usage
            for ref_class_ in class_.returnTypes:
                if self.is_distributed:
                    ref_class_ = class_.serviceName.replace(" ", "") + "." + ref_class_
                if ref_class_ in class_names:
                    j = class_names.index(ref_class_)
                    return_usage[i, j] += 1
            # nested_usage
            for ref_class_ in class_.nestedTypes:
                if self.is_distributed:
                    ref_class_ = class_.serviceName.replace(" ", "") + "." + ref_class_
                if ref_class_ in class_names:
                    j = class_names.index(ref_class_)
                    nested_usage[i, j] += 1
            # inheritance_usage
            for ref_class_ in class_.inheritedTypes:
                if self.is_distributed:
                    ref_class_ = class_.serviceName.replace(" ", "") + "." + ref_class_
                if ref_class_ in class_names:
                    j = class_names.index(ref_class_)
                    inheritance_usage[i, j] += 1
        calls, method_calls = self._get_calls()
        references = self.get_references()
        interactions = np.sum([field_usage, parameter_usage, return_usage, nested_usage, inheritance_usage,
                               calls.values, references.values], axis=0)
        interactions = pd.DataFrame(interactions, columns=class_names, index=class_names)
        assert interactions.shape == calls.shape
        return interactions, calls, method_calls, references


