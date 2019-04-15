from __future__ import print_function   

import xml.etree.ElementTree as ET
from xml.etree import ElementTree

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk 
# nltk.download('stopwords')
import json
import string
import sys
import pickle

with open('file.pkl', 'rb') as handle:
    D = pickle.load(handle)
    print(len(D))
