from typing import Optional

from .analysis import DataClient
from .analysis.analysisClient import AnalysisClient
from .analysis.analysisLocalClient import AnalysisLocalClient
from .analysis.analysisJarClient import AnalysisJarClient


def select_client(app_name: str, data_path: str, use_jar: bool = False,
                  jar_path: Optional[str] = None, is_distributed: bool = False,
                  parsing_path: Optional[str] = None, *args, **kwargs) -> DataClient:
    if parsing_path:
        client = AnalysisLocalClient(app_name, parsing_path, is_distributed=is_distributed)
    elif use_jar:
        client = AnalysisJarClient(app_name, data_path, jar_path, is_distributed=is_distributed)
    else:
        client = AnalysisClient(app_name, data_path, is_distributed=is_distributed)
    return client
