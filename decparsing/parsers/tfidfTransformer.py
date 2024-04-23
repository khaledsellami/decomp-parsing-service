import os.path
import re

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from nltk.stem import PorterStemmer


class TFIDFTransformer:
    CHARS_TO_REMOVE = ['/', ';', '?', '.', '*', '@', '#', '!', ',', '$','|','-','"',"'",'&','(',')','[',']','{','}',
                       '=','+','°']

    def __init__(self, dataset, debugging=False):
        self.CHARS_TO_REMOVE_MAP = {ord(x): '' for x in self.CHARS_TO_REMOVE}
        self.dataset = dataset
        self.class_words = dict()
        self.word_counts = dict()
        self.tfidf_vectors = dict()
        self.classes = list()
        # self.vocabulary = set()
        self.stemmer = PorterStemmer()
        self.debugging = debugging
        self.tfidf_vectorizer = TfidfVectorizer(preprocessor=' '.join, stop_words=None)
        self.count_vectorizer = CountVectorizer(preprocessor=' '.join, stop_words=None)
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.pardir, "stopwords.txt"), "r") as f:
            self.stopwords = f.read().splitlines()

    def reset(self):
        self.class_words = dict()
        self.tfidf_vectors = dict()
        self.word_counts = dict()
        self.classes = list()
        # self.vocabulary = set()
        self.stemmer = PorterStemmer()
        self.tfidf_vectorizer = TfidfVectorizer(preprocessor=' '.join, stop_words=None)
        self.count_vectorizer = CountVectorizer(preprocessor=' '.join, stop_words=None)

    def build(self):
        self.reset()
        for i in range(len(self.dataset)):
            self.get_words(i)
        self.measure_vectors()

    def get_words(self, item):
        #class_ref = self.db.ent_from_id(class_)
        data = self.dataset[item]
        self.class_words[item] = list()
        debug_string = "    Found: "
        # Analyze class name
        for text in data:
            self.analyze(text, item)

    def analyze(self, text, item):
        words = self.preprocess(text)
        # self.vocabulary = self.vocabulary.union(set(words))
        self.class_words[item] += words

    def split_words(self, text):
        return [i for w in text.split(" ") for x in w.split("_")
                 for i in re.sub(r'((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))', r' \1', x).split()]

    def preprocess(self, text, remove_stopwords=True):
        preprocessed = list()
        text = text.translate(self.CHARS_TO_REMOVE_MAP)
        words = self.split_words(text)
        for word in words:
            word = word.lower()
            if remove_stopwords and (word in self.stopwords or len(word) < 2):
                continue
            word = self.stemmer.stem(word)
            preprocessed.append(word)
        return preprocessed

    def measure_vectors(self):
        self.tfidf_vectors = self.tfidf_vectorizer.fit_transform(self.class_words.values())
        self.word_counts = (self.count_vectorizer.fit_transform(self.class_words.values()).toarray() > 0).sum(axis=0)

    def get_class_vector(self, class_):
        return self.tfidf_vectors[class_].toarray()

    def get_sim(self, class1, class2):
        vector1 = self.get_class_vector(class1)
        vector2 = self.get_class_vector(class2)
        return vector1.dot(vector2.T).sum()

    def get_matrix(self):
        return self.tfidf_vectors.toarray()

    def get_vocabulary(self):
        return self.count_vectorizer.get_feature_names_out()