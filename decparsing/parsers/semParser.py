from typing import List

import pandas as pd

from ..models import analyze_pb2 as apb
from .tfidfTransformer import TFIDFTransformer
from ..utils import handle_duplicates


class SemParser:
    def __init__(self, classes: List[apb.Class_] = None, methods: List[apb.Method_] = None, is_distributed=False):
        self.classes = classes
        self.methods = methods
        self.is_distributed = is_distributed

    def get_class_names(self) -> List[str]:
        if self.classes is None:
            return []
        elif self.is_distributed:
            names = [class_.serviceName.replace(" ", "") + "." + class_.fullName for class_ in self.classes]
        else:
            names = [class_.fullName for class_ in self.classes]
        return handle_duplicates(names)

    def get_method_names(self) -> List[str]:
        if self.methods is None:
            return []
        elif self.is_distributed:
            names = [method_.serviceName.replace(" ","") + "." + method_.fullName for method_ in self.methods]
        else:
            names = [method_.fullName for method_ in self.methods]
        return handle_duplicates(names)

    def get_tfidf_data(self, level="class") -> pd.DataFrame:
        if level == "class":
            tfidf = TFIDFTransformer([c.textAndNames for c in self.classes])
            tfidf.build()
            names = self.get_class_names()
        elif level == "method":
            tfidf = TFIDFTransformer([m.textAndNames for m in self.methods])
            tfidf.build()
            names = self.get_method_names()
        else:
            raise NotImplementedError(
                "Unrecognized level {}. Only accepted levels are \"class\" and \"method\"!".format(level))
        df = pd.DataFrame(tfidf.get_matrix(), columns=tfidf.get_vocabulary(), index=names)
        return df

    def get_count_data(self, level="class") -> pd.DataFrame:
        # TODO Warning: misleading name, should be changed in the future
        if level == "class":
            tfidf = TFIDFTransformer([c.textAndNames for c in self.classes])
            tfidf.build()
            names = self.get_class_names()
        elif level == "method":
            tfidf = TFIDFTransformer([m.textAndNames for m in self.methods])
            tfidf.build()
            names = self.get_method_names()
        else:
            raise NotImplementedError(
                "Unrecognized level {}. Only accepted levels are \"class\" and \"method\"!".format(level))
        word_count = pd.DataFrame(tfidf.word_counts.reshape(1, -1), columns=tfidf.get_vocabulary())
        word_intersection = tfidf.get_matrix()
        word_intersection = word_intersection[:, word_count.iloc[0] <= word_intersection.shape[0] // 2]
        word_intersection = word_intersection.dot(word_intersection.transpose())
        df = pd.DataFrame(word_intersection, columns=names, index=names)
        return df

