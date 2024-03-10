from .dataHandler import DataHandler
from ._version import __version__
import os
import nltk
nltk.data.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "nltk_data"))
