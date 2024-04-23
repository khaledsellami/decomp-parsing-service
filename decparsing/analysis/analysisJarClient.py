import os
from typing import List, Optional
import subprocess
import tempfile

from .analysisLocalClient import AnalysisLocalClient
from ..models import analyze_pb2 as apb


class AnalysisJarClient(AnalysisLocalClient):
    JAR_FILENAME = "java-analysis-service-1-3-0.jar"

    def __init__(self, app_name: str, app_path: str, jar_path: Optional[str], is_distributed: bool = False):
        self.app_path = app_path
        self.jar_path = jar_path if jar_path is not None else os.path.join(os.path.dirname(__file__), "resources",
                                                                           self.JAR_FILENAME)
        self.temp_folder = tempfile.TemporaryDirectory()
        super().__init__(app_name, os.path.join(self.temp_folder.name, app_name), is_distributed=is_distributed)

    def __del__(self):
        self.temp_folder.cleanup()

    def _trigger_analysis(self):
        command = ['java', '-jar', self.jar_path, 'analyze', self.app_name, "-p", self.app_path,
                   "-o", self.temp_folder.name]
        if self.is_distributed:
            command.append("-d")
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()
        if process.returncode != 0:
            raise subprocess.CalledProcessError(returncode=process.returncode, output=out, stderr=err, cmd=command)
        assert os.path.exists(self.data_path)

    def get_classes(self) -> List[apb.Class_]:
        if not os.path.exists(self.data_path):
            self._trigger_analysis()
        return super().get_classes()

    def get_methods(self) -> List[apb.Method_]:
        if not os.path.exists(self.data_path):
            self._trigger_analysis()
        return super().get_methods()

    def get_invocations(self) -> List[apb.Invocation_]:
        if not os.path.exists(self.data_path):
            self._trigger_analysis()
        return super().get_invocations()
