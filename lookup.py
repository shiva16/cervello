from __future__ import print_function   
import string
import sys
import pickle

with open('file.pkl', 'rb') as handle:
    D = pickle.load(handle)
    for v in D:
        print(v, len(D[v]), D[v][:2])
    print(len(D))
