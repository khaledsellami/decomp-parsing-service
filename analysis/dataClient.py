from typing import List

from models.analyze_pb2 import Class_, Method_, Invocation_


class DataClient:

    def __init__(self, app_name: str):
        self.app_name = app_name

    def get_classes(self) -> List[Class_]:
        raise NotImplementedError()

    def get_methods(self) -> List[Method_]:
        raise NotImplementedError()

    def get_invocations(self) -> List[Invocation_]:
        raise NotImplementedError()