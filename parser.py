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

# with open("data_",'r') as f:
#     data = f.read()
#     data = data[2:]
#     data = data.replace('\\n','')
#     data = data[:-1]    
#     with open("corpus.xml",'w') as w:
#         w.write(data)

med_terms = []
punctuations = set(string.punctuation)

def extract_values(obj, key):
    """Pull all values of specified key from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results

with open("ABAadultMouseBrainOntology.json") as f:
        data = f.read()
        read_json = json.loads(data)
        med_terms = extract_values(read_json, "text")

print(len(med_terms))

stop_words = set(stopwords.words('english'))

# i=100
root = ElementTree.parse("corpus2.xml").getroot()
D = {}
for item in root.findall("entry"):
    doc_id = item.find("id")
    doc_id = ElementTree.tostring(doc_id,encoding="unicode")
    doc_id = doc_id.replace('<id>','')
    doc_id = doc_id.replace('</id>','')
#     print(doc_id)

    summary = item.find("summary")
    summary = ElementTree.tostring(summary,encoding="unicode")
    summary = summary.replace('<summary>','')
    summary = summary.replace('</summary>','')
    summary = summary.lower().split(' ')
    # print(summary)

    
    for i in range(len(med_terms)):
        term = med_terms[i]
        term = term.lower()
        # if term == 'pons':
        #         print('---------------------')
        #         print(doc_id)
        #         print(med_terms)
        #         print(i)                
        #         sys.exit(1)
        # print(term, i/len(med_terms)*100, flush=True)
        
        if term in summary:
                # print(term, i/len(med_terms)*100, flush=True)
                if term in D.keys():
                        D[term].append(doc_id)
                else:
                        D[term] = [doc_id]

#     i -= 1
#     if not i: break
    
print(D)
