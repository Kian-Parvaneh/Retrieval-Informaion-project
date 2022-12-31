import os;
import json;
import nltk;
import numpy as np;
import pandas as pd;
from pattern.text.en import singularize
nltk.download('stopwords');
nltk.download('punkt');
nltk.download('omw-1.4');
nltk.download('wordnet');
from nltk.corpus import stopwords;
from nltk.tokenize import word_tokenize;

path =r"C:/Users/kianp/Desktop/retrieval info project/Docs";
os.chdir(path);

def read_files(file_path):#read files and add them to array
   with open(file_path, 'r', encoding="utf8") as file:
      Docs.append(file.read());


Docs = [];#an array of stored files
m=1
for file in os.listdir():#locating files to read
    file_path =f"{path}/{m}.txt";
    read_files(file_path);
    m+=1;
    if(m>10):
        break
for i in Docs:
    print(i)
    print('\n\n')
removeStopwords = [];
normalized = [];
for doc in Docs:
    removeStopwords.append([word for word in word_tokenize(doc) if word not in stopwords.words('english')]);
for doc in removeStopwords:
    normalized.append([singularize(word) for word in doc])


values = [];
for doc in normalized :
    values.append(json.loads(pd.value_counts(np.array(doc)).to_json()));


while(True):
    result = {};
    query = singularize(input("Enter word:"));
    i = 1;
    for doc in values:
        try:
            result[str(i)] = doc[query];
        except:
            result[str(i)] = 0;
        i+=1;
    print(sorted(result.items(), key=lambda x:x[1], reverse=True));