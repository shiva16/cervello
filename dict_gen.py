from __future__ import print_function   

import xml.etree.ElementTree as ET
from xml.etree import ElementTree

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk 
# nltk.download('wordnet')
import json
import string
import sys
import pickle
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import wordnet

stemmer = SnowballStemmer("english", ignore_stopwords=True)

# with open("data_",'r') as f:
#     data = f.read()
#     data = data[2:]
#     data = data.replace('\\n','')
#     data = data[:-1]    
#     with open("corpus.xml",'w') as w:
#         w.write(data)

med_terms = []
acronyms= []
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
        # acronyms = extract_values(read_json, "acronym")

print('Total brain regions considered:',len(med_terms))
print('Processing...')
stop_words = set(stopwords.words('english'))

root = ElementTree.parse("corpus2.xml").getroot()
D = {}

if len(sys.argv) > 1:
    step = int(sys.argv[1])
    print(step)
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
    summary = summary.lower()
    # summary = nltk.word_tokenize(summary)
    # print(summary)

    # for i in range(len(summary)):
    #     term = summary[i]
    #     term = term.lower()        
    #     acr = ""
    #     pos = i
    #     copy = term
    #     # term = stemmer.stem(term)
    #     if term in med_terms:
    #         # print(term,copy)

    #         if term in D.keys():
    #             D[term].append([doc_id,pos])
    #         else:
    #             D[term] = [[doc_id,pos]]

    # #     # if  term in acronyms and not wordnet.synsets(term):
    # #     if  term in acronyms:
    # #         # print(term, copy)

    # #         term = med_terms[acronyms.index(term)]

    # #         # pos = summary.index(acr)
    # #         if term in D.keys():
    # #             D[term].append([doc_id,pos])
    # #         else:
    # #             D[term] = [[doc_id,pos]]
    
    for i in range(len(med_terms)):
        term = med_terms[i]
        term = term.lower()
        # acr = acronyms[i]
        # if term == 'frontal pole, layer 2/3': print('-------', summary)
        
        if term in summary:     
            pos = summary.index(term)       
            if term in D.keys():
                D[term].append([doc_id,pos])
            else:
                D[term] = [[doc_id,pos]]

    if len(sys.argv) > 1:
        step -= 1
        if step == 0:
            print(D)
            break       
    

    ##SAVE DICTIONARY TO FILE
    f = open("file.pkl","wb")
    pickle.dump(D,f)
    f.close()

    