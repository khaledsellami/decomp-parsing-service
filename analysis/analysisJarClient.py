import os
from typing import List
import subprocess
import tempfile

from analysis.analysisLocalClient import AnalysisLocalClient
from models.analyze_pb2 import Class_, Method_, Invocation_


class AnalysisJarClient(AnalysisLocalClient):
    def __init__(self, app_name: str, app_path: str, jar_path: str):
        self.app_path = app_path
        self.jar_path = jar_path
        self.temp_folder = tempfile.TemporaryDirectory()
        super().__init__(app_name, os.path.join(self.temp_folder.name, app_name))

    def __del__(self):
        self.temp_folder.cleanup()

    def _trigger_analysis(self):
        command = ['java', '-jar', self.jar_path, 'analyze', self.app_name, "-p", self.app_path,
                   "-o", self.temp_folder.name]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()
        if process.returncode != 0:
            raise subprocess.CalledProcessError(returncode=process.returncode, output=out, stderr=err, cmd=command)
        assert os.path.exists(self.data_path)

    def get_classes(self) -> List[Class_]:
        if not os.path.exists(self.data_path):
            self._trigger_analysis()
        return super().get_classes()

    def get_methods(self) -> List[Method_]:
        if not os.path.exists(self.data_path):
            self._trigger_analysis()
        return super().get_methods()

    def get_invocations(self) -> List[Invocation_]:
        if not os.path.exists(self.data_path):
            self._trigger_analysis()
        return super().get_invocations()
