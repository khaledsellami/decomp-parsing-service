from typing import List, Dict

from . import DataClient
from ..models import analyze_pb2 as apb


class AnalysisRuntimeClient(DataClient):
    def __init__(self, app_name: str, class_data: List[Dict], method_data: List[Dict], invocation_data: List[Dict],
                 is_distributed: bool = False):
        super().__init__(app_name, is_distributed)
        self.logger.debug("converting data")
        self.class_data = self.convert_classes(class_data)
        self.method_data = self.convert_methods(method_data)
        self.invocation_data = self.convert_invocations(invocation_data)

    @staticmethod
    def convert_classes(class_data: List[Dict]) -> List[apb.Class_]:
        classes = []
        for class_ in class_data:
            class_ = class_.copy()
            if "fieldCalls" in class_:
                class_["fieldCalls"] = [apb.Invocation_(**fc) for fc in class_["fieldCalls"]]
            classes.append(apb.Class_(**class_))
        return classes

    @staticmethod
    def convert_methods(method_data: List[Dict]) -> List[apb.Method_]:
        methods = []
        for method_ in method_data:
            for k in ["localInvocations", "invocations"]:
                method_ = method_.copy()
                if k in method_:
                    method_[k] = [apb.Invocation_(**i) for i in method_[k]]
            methods.append(apb.Method_(**method_))
        return methods

    @staticmethod
    def convert_invocations(invocation_data: List[Dict]) -> List[apb.Invocation_]:
        return [apb.Invocation_(**invocation_) for invocation_ in invocation_data]

    def get_classes(self) -> List[apb.Class_]:
        return self.class_data

    def get_methods(self) -> List[apb.Method_]:
        return self.method_data

    def get_invocations(self) -> List[apb.Invocation_]:
        return self.invocation_data
