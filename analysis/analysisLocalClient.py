import os
import json
from typing import List

from analysis.dataClient import DataClient
from models.analyze_pb2 import Class_, Method_, Invocation_


class AnalysisLocalClient(DataClient):
    def __init__(self, app_name: str, data_path: str):
        super().__init__(app_name)
        self.data_path = data_path

    def get_classes(self) -> List[Class_]:
        self.logger.debug("loading classes")
        with open(os.path.join(self.data_path, "typeData.json"), "r") as f:
            class_data = json.load(f)["classes"]
        classes = []
        for class_ in class_data:
            if "fieldCalls" in class_:
                class_["fieldCalls"] = [Invocation_(**fc) for fc in class_["fieldCalls"]]
            classes.append(Class_(**class_))
        return classes

    def get_methods(self) -> List[Method_]:
        self.logger.debug("loading methods")
        with open(os.path.join(self.data_path, "methodData.json"), "r") as f:
            method_data = json.load(f)["methods"]
        methods = []
        for method_ in method_data:
            for k in ["localInvocations", "invocations"]:
                if k in method_:
                    method_[k] = [Invocation_(**i) for i in method_[k]]
            methods.append(Method_(**method_))
        return methods

    def get_invocations(self) -> List[Invocation_]:
        self.logger.debug("loading invocations")
        with open(os.path.join(self.data_path, "invocationData.json"), "r") as f:
            invocation_data = json.load(f)["invocations"]
        return [Invocation_(**invocation_) for invocation_ in invocation_data]