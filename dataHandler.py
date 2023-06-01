import io
import json
import logging
import os
from typing import List, Union, Tuple
import pickle

import pandas as pd

from analysisClient import AnalysisClient
from parsers import StructParser, SemParser
from models.parse_pb2 import Format


class DataHandler:
    """ Handler for loading and saving the parsing data. Current implementation uses a local volume and saves the
    data as pickle and json files. In the future, we should use a more suitable storage format"""
    LOCAL_PATH = "./data/"
    DATA_FORMAT = Format.PARQUET

    def __init__(self, client: AnalysisClient, format: Format = Format.PARQUET):
        self.app_name = client.app_name
        self.app_repo = client.app_repo
        self.client = client
        self.format = format
        self.logger = logging.getLogger(__name__)

    def get_names(self, level="class") -> List[str]:
        if level == "class":
            classes = self.client.get_classes()
            parser = StructParser(classes)
            return parser.get_class_names()
        elif level == "method":
            methods = self.client.get_methods()
            parser = StructParser(methods=methods)
            return parser.get_method_names()
        else:
            raise NotImplementedError()

    def load_all(self) -> int:
        classes = methods = None
        for file_name in ["interactions", "calls", "tfidf", "word_count"]:
            if not os.path.exists(
                    os.path.join(self.LOCAL_PATH, self.app_name, "{}.{}".format(file_name,
                                                                                Format.Name(self.DATA_FORMAT).lower()))
            ):
                try:
                    if classes is None:
                        classes = self.client.get_classes()
                    if methods is None:
                        methods = self.client.get_methods()
                    if file_name == "interactions":
                        parser = StructParser(classes, methods)
                        data, calls, _, _ = parser.get_interactions()
                        self.save(calls, "calls")
                    elif file_name == "calls":
                        parser = StructParser(classes, methods)
                        data, _ = parser.get_calls()
                    elif file_name == "tfidf":
                        parser = SemParser(classes, methods)
                        data = parser.get_tfidf_data()
                    else:
                        parser = SemParser(classes, methods)
                        data = parser.get_count_data()
                    self.save(data, file_name)
                except Exception as e:
                    self.logger.error(e)
                    return 1
        return 0

    def save(self, data: pd.DataFrame, name: str):
        path = os.path.join(self.LOCAL_PATH, self.app_name, "{}.{}".format(name, Format.Name(self.DATA_FORMAT).lower()))
        os.makedirs(os.path.dirname(path), exist_ok=True)
        if self.DATA_FORMAT == Format.PARQUET:
            data.to_parquet(path)
        elif self.DATA_FORMAT == Format.CSV:
            data.to_csv(path)
        elif self.DATA_FORMAT == Format.PICKLE:
            data.to_pickle(path)
        elif self.DATA_FORMAT == Format.JSON:
            data.to_json(path)
        else:
            raise ValueError("Unrecognized data_format {}!".format(Format.Name(self.DATA_FORMAT).lower()))

    def load(self, path: str) -> pd.DataFrame:
        if self.DATA_FORMAT == Format.PARQUET:
            data = pd.read_parquet(path)
        elif self.DATA_FORMAT == Format.CSV:
            data = pd.read_csv(path)
        elif self.DATA_FORMAT == Format.PICKLE:
            data = pd.read_pickle(path)
        elif self.DATA_FORMAT == Format.JSON:
            data = pd.read_json(path)
        else:
            raise ValueError("Unrecognized data_format {}!".format(Format.Name(self.DATA_FORMAT).lower()))
        return data

    def get_data(self, data_type: str) -> Tuple[str, Union[pd.DataFrame, None]]:
        assert data_type in ["interactions", "calls", "tfidf", "word_count"]
        data_path = os.path.join(self.LOCAL_PATH, self.app_name, "{}.{}".format(data_type,
                                                                                Format.Name(self.DATA_FORMAT).lower()))
        if not os.path.exists(data_path):
            classes = self.client.get_classes()
            methods = self.client.get_methods()
            if data_type == "interactions":
                parser = StructParser(classes, methods)
                data, calls, _, _ = parser.get_interactions()
            elif data_type == "calls":
                parser = StructParser(classes, methods)
                data, _ = parser.get_calls()
            elif data_type == "tfidf":
                parser = SemParser(classes, methods)
                data = parser.get_tfidf_data()
            else:
                parser = SemParser(classes, methods)
                data = parser.get_count_data()
            self.save(data, data_type)
            return data_path, data
        return data_path, None

    def convert(self, path: str = None, data: pd.DataFrame = None, format: Format = Format.PARQUET):
        assert not (path is None and data is None)
        if path is not None:
            data = self.load(path)
        if format == Format.PARQUET:
            return io.BytesIO(data.to_parquet())
        elif format == Format.CSV:
            return io.BytesIO(data.to_csv().encode(encoding="utf-8"))
        elif format == Format.PICKLE:
            return io.BytesIO(pickle.dumps(data))
        elif format == Format.JSON:
            return io.BytesIO(data.to_json().encode(encoding="utf-8"))
        else:
            raise ValueError("Unrecognized data_format {}!".format(format))




