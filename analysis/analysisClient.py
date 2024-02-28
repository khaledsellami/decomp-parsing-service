import os
from typing import List

import grpc

from analysis.dataClient import DataClient
from models.analyze_pb2_grpc import AnalyzerStub
from models.analyze_pb2 import AstRequest, Class_, Method_, Invocation_


DEFAULT_ANALYSIS_SERVICE_PORTS = dict(java=50100, python=50101)


class AnalysisClient(DataClient):
    SERVICE_NAME = {lang: os.getenv(f'SERVICE_{lang.upper()}_ANALYSIS', "localhost") for lang in ["java", "python"]}
    ANALYSIS_SERVICE_PORTS = {lang: os.getenv(f'SERVICE_{lang.upper()}_ANALYSIS_PORT',
                                    DEFAULT_ANALYSIS_SERVICE_PORTS[lang]) for lang in ["java", "python"]}

    def __init__(self, app_name: str, app_repo: str, language: str = "java"):
        super().__init__(app_name)
        if language not in self.ANALYSIS_SERVICE_PORTS:
            raise ValueError(
                "Unrecognized language {}. Supported languages are {}".format(
                    language, list(self.ANALYSIS_SERVICE_PORTS.keys())))
        self.app_repo = app_repo
        self.language = language

    def get_classes(self) -> List[Class_]:
        self.logger.debug(
            f"getting classes from {self.SERVICE_NAME[self.language]}:{self.ANALYSIS_SERVICE_PORTS[self.language]}")
        with grpc.insecure_channel(f'{self.SERVICE_NAME[self.language]}:{self.ANALYSIS_SERVICE_PORTS[self.language]}') \
                as channel:
            stub = AnalyzerStub(channel)
            request = AstRequest(appName=self.app_name, appRepo=self.app_repo)
            return [c for c in stub.getClasses(request)]

    def get_methods(self) -> List[Method_]:
        self.logger.debug(
            f"getting methods from {self.SERVICE_NAME[self.language]}:{self.ANALYSIS_SERVICE_PORTS[self.language]}")
        with grpc.insecure_channel(f'{self.SERVICE_NAME[self.language]}:{self.ANALYSIS_SERVICE_PORTS[self.language]}') \
                as channel:
            stub = AnalyzerStub(channel)
            request = AstRequest(appName=self.app_name, appRepo=self.app_repo)
            return [m for m in stub.getMethods(request)]

    def get_invocations(self) -> List[Invocation_]:
        self.logger.debug(
            f"getting invocations from {self.SERVICE_NAME[self.language]}:{self.ANALYSIS_SERVICE_PORTS[self.language]}")
        with grpc.insecure_channel(f'{self.SERVICE_NAME[self.language]}:{self.ANALYSIS_SERVICE_PORTS[self.language]}') \
                as channel:
            stub = AnalyzerStub(channel)
            request = AstRequest(appName=self.app_name, appRepo=self.app_repo)
            return [i for i in stub.getInvocations(request)]