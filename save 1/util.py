from pprint import pprint
from sentence_transformers import SentenceTransformer
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
import numpy as np
import re


model = SentenceTransformer('all-MiniLM-L6-v2')
df = pd.read_csv("global_dataset_32000_plus.csv", sep=",")
emb = np.load("embeddings.npy")
c = df.columns[0]
column = df[c]
emb = emb[column]
df['embeddings'] = emb.tolist()
X = np.array(list(df['embeddings']))
Y = np.array(df['c1'])
m = Pipeline(steps=[("knn", KNeighborsClassifier(n_neighbors=11, metric='cosine'))]).fit(X, Y)


def cut_text(text:str):
    result = {}
    run = True
    i = 1
    i_begin = 0
    i_end = 0
    while run:
        text_begin = "%s. " % i
        text_end = "%s. " % (i+1)
        i_begin = text.find(text_begin)
        i_end = text.find(text_end)
        t = text[i_begin+3:i_end]
        result["Claim %s " % i] = t
        i += 1
        if i_end == -1:
            run = False
    return result




def get_classes(claim):
    phrases = re.split("[.,:;!?]", claim)
    phrases = [sub.strip() for sub in phrases if sub.strip()]
    print(phrases)
    print(len(phrases))
    phrases_embedings = model.encode(phrases)
    lettres = m.predict(phrases_embedings)
    result = {}
    for i in range(len(lettres)):
        if lettres[i] not in result:
            result[lettres[i]] = []
        result[lettres[i]].append(phrases[i])
    return result





if __name__ == "__main__":
    with open("test.txt", "r") as f:
        text = f.read()
    # text = "1. hello world. 2. hello. 3. world."
    result = cut_text(text)
    # for t in result:
    #     print(result[t])
    pprint(result)