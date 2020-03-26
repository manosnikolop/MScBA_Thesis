import io
from datetime import datetime
print('importing files')
print(datetime.now())
import re
import gensim
import bz2
import xml.sax
import mwparserfromhell


with io.open('D:\document_parsed_spacy.txt','r',encoding="utf-8") as file:
    document_spacy=file.read()
    file.close()



print('paras')
print(datetime.now())
paras = [[w for w in p.split()] for p in document_spacy.lower().split('.')]


print('training model')
print(datetime.now())

model2 = gensim.models.Word2Vec(paras, size=300, window=3, min_count=5, workers=4, alpha=0.03, min_alpha=0.0007,
                                negative=5)
model2.save("word2vec_wikipedia.modelbig")


# Load model
print('loading model')
print(datetime.now())
model3 = gensim.models.Word2Vec.load("word2vec_wikipedia.modelbig")


print('finding similarities')
print(datetime.now())