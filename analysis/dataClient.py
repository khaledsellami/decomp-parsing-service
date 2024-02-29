from typing import List
import logging

from models import analyze_pb2 as apb


class DataClient:

    def __init__(self, app_name: str):
        self.app_name = app_name
        self.logger = logging.getLogger(self.__class__.__name__)

    def get_classes(self) -> List[apb.Class_]:
        raise NotImplementedError()

    def get_methods(self) -> List[apb.Method_]:
        raise NotImplementedError()

    def get_invocations(self) -> List[apb.Invocation_]:
        raise NotImplementedError()