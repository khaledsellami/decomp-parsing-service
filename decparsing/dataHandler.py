import io
import logging
import os
from typing import List, Union, Tuple, Optional
import pickle

import pandas as pd

from .analysis import DataClient
from .parsers import StructParser, SemParser
from .models import parse_pb2 as ppb


Format = ppb.Format


class DataHandler:
    """ Handler for loading and saving the parsing data. Current implementation uses a local volume and saves the
    data as pickle and json files. In the future, we should use a more suitable storage format"""
    LOCAL_PATH = "./data/"
    DATA_FORMAT = Format.PARQUET

    def __init__(self, client: DataClient, format: Format = Format.PARQUET, output_path: Optional[str] = None):
        self.app_name = client.app_name
        self.is_distributed = client.is_distributed
        self.client = client
        self.format = format
        self.output_path = self.LOCAL_PATH if output_path is None else output_path
        self.logger = logging.getLogger(self.__class__.__name__)

    def get_names(self, level="class") -> List[str]:
        if level == "class":
            classes = self.client.get_classes()
            parser = StructParser(classes, is_distributed=self.is_distributed)
            names = parser.get_class_names()
        elif level == "method":
            methods = self.client.get_methods()
            parser = StructParser(methods=methods, is_distributed=self.is_distributed)
            names = parser.get_method_names()
        else:
            raise NotImplementedError()
        return names

    def load_all(self, level="class") -> int:
        if level not in ["class", "method"]:
            raise ValueError(f"level {level} is not in ['class', 'method']")
        classes = methods = None
        for file_name in ["interactions", "calls", "tfidf", "word_count"]:
            if not os.path.exists(
                    os.path.join(self.output_path, self.app_name, "{}_{}.{}".format(level, file_name,
                                                                                    Format.Name(self.format).lower()))
            ):
                try:
                    if classes is None:
                        classes = self.client.get_classes()
                    if methods is None:
                        methods = self.client.get_methods()
                    if file_name == "interactions":
                        parser = StructParser(classes, methods, is_distributed=self.is_distributed)
                        if level == "class":
                            data, calls, _, _ = parser.get_interactions()
                            self.save(calls, f"{level}_calls")
                        else:
                            data = parser.get_calls(level)
                    elif file_name == "calls":
                        parser = StructParser(classes, methods, is_distributed=self.is_distributed)
                        data = parser.get_calls(level)
                    elif file_name == "tfidf":
                        parser = SemParser(classes, methods, is_distributed=self.is_distributed)
                        data = parser.get_tfidf_data(level)
                    else:
                        parser = SemParser(classes, methods, is_distributed=self.is_distributed)
                        data = parser.get_count_data(level)
                    self.save(data, f"{level}_{file_name}")
                except Exception as e:
                    self.logger.error(e)
                    return 1
        return 0

    def save(self, data: pd.DataFrame, name: str):
        path = os.path.join(self.output_path, self.app_name, "{}.{}".format(name, Format.Name(self.format).lower()))
        self.logger.debug(f"Saving data in {path}")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        if self.format == Format.PARQUET:
            data.to_parquet(path)
        elif self.format == Format.CSV:
            data.to_csv(path)
        elif self.format == Format.PICKLE:
            data.to_pickle(path)
        elif self.format == Format.JSON:
            data.to_json(path)
        else:
            raise ValueError("Unrecognized data_format {}!".format(Format.Name(self.format).lower()))

    def load(self, path: str) -> pd.DataFrame:
        if self.format == Format.PARQUET:
            data = pd.read_parquet(path)
        elif self.format == Format.CSV:
            data = pd.read_csv(path)
        elif self.format == Format.PICKLE:
            data = pd.read_pickle(path)
        elif self.format == Format.JSON:
            data = pd.read_json(path)
        else:
            raise ValueError("Unrecognized data_format {}!".format(Format.Name(self.format).lower()))
        return data

    def get_data(self, data_type: str, level="class") -> Tuple[str, Union[pd.DataFrame, None]]:
        assert data_type in ["interactions", "calls", "tfidf", "word_count"]
        data_path = os.path.join(self.output_path, self.app_name, "{}_{}.{}".format(level, data_type,
                                                                                   Format.Name(self.format).lower()))
        if not os.path.exists(data_path):
            classes = self.client.get_classes()
            methods = self.client.get_methods()
            if data_type == "interactions":
                if level == "method":
                    self.logger.warning(f"data type {data_type} not valid for level {level}. Defaulting to calls "
                                        f"instead!")
                    parser = StructParser(classes, methods, is_distributed=self.is_distributed)
                    data = parser.get_calls(level)
                else:
                    parser = StructParser(classes, methods, is_distributed=self.is_distributed)
                    data, calls, _, _ = parser.get_interactions()
            elif data_type == "calls":
                parser = StructParser(classes, methods, is_distributed=self.is_distributed)
                data = parser.get_calls(level)
            elif data_type == "tfidf":
                parser = SemParser(classes, methods, is_distributed=self.is_distributed)
                data = parser.get_tfidf_data(level)
            else:
                parser = SemParser(classes, methods, is_distributed=self.is_distributed)
                data = parser.get_count_data(level)
            self.save(data, f"{level}_{data_type}")
        else:
            data = self.load(data_path)
        return data_path, data

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




