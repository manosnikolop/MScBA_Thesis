print('importing files')
import re
import gensim
import bz2
import xml.sax
import mwparserfromhell
from datetime import datetime
import spacy


# Set up spacy

#Run command if needed to download model
#python -m spacy download en_core_web_lg

import en_core_web_lg
nlp = en_core_web_lg.load()
nlp.max_length = 733629200

print("Reading file")

data_path = 'D:\Downloads\All_evaluations_values_3.txt'

data_file= open(data_path, "r", encoding="utf8")
all_data = data_file.read() 

print('cleaning text')
print(datetime.now())

all_data = re.sub(r"[^A-Za-z0-9 + .\s + Α-Ωα-ωίϊΐόάέύϋΰήώ]+", '', all_data)
all_data=re.sub('\d','',all_data)

print('clearing nouns')
print(datetime.now())

#Keep only these words that are necessary 
all_data_nlp=nlp(all_data,disable = ['ner', 'parser'])
keep=['NOUN','PROPN','NN','NNP','NNPS','NNS','NE','NNE','NP','ADJ','JJ','JJR','JJS','ADJA','ADJD','ADJP' ]
keep_2=['ADJ','JJ','JJR','JJS','ADJA','ADJD','ADJP' ]

final_doc_list=[]
final_doc=''

for token in all_data_nlp:
    #print(token.text, token.tag_, token.is_stop)
    if token.tag_ in keep:
        final_doc = final_doc + str(' ') + str(token.text)
		
print('all_data_paras')
print(datetime.now())
all_data_paras = [[w for w in p.split()] for p in final_doc.lower().split('.')]


print('training model')
print(datetime.now())

model25 = gensim.models.Word2Vec(all_data_paras, size=300, window=3, min_count=5, workers=4, alpha=0.03, min_alpha=0.0007,
                                negative=5)
model25.save("word2vec_evaluations.modelbig")


# Load model
print('loading model')
print(datetime.now())
model35 = gensim.models.Word2Vec.load("word2vec_evaluations.modelbig")


print('finding similarities')
print(datetime.now())

##### Test model - Find similar words ########

test_words = ['male', 'female']
for i in test_words:
    print("Most similar to {0}".format(i),model35.wv.most_similar(positive=i, topn=50) )

##### Test model - Find similar words with Cosine Similarity Distance ############3

def cosine_distance (model, word,target_list , num) :
    cosine_dict ={}
    word_list = []
    a = model[word]
    for item in target_list :
        if item != word :
            b = model [item]
            cos_sim = np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b))
            cosine_dict[item] = cos_sim
    dist_sort=sorted(cosine_dict.items(), key=lambda dist: dist[1],reverse = True) ## in Descedning order
    for item in dist_sort:
        word_list.append((item[0], item[1]))
    return word_list[0:num]

# Similarity tests 


# MALES #
print("If male is sure, then female;".format('female'), model35.wv.most_similar(positive=['female', 'sure'], negative=['male'], topn=15))
print("If male is experienced, then female;".format('female'), model35.wv.most_similar(positive=['female', 'experienced'], negative=['male'], topn=15))
print("If male is professional, then female;".format('female'), model35.wv.most_similar(positive=['female', 'professional'], negative=['male'], topn=15))
print("If male is serious, then female;".format('female'), model35.wv.most_similar(positive=['female', 'serious'], negative=['male'], topn=15))
print("If male is comfortable, then female;".format('female'), model35.wv.most_similar(positive=['female', 'comfortable'], negative=['male'], topn=15))
print("If male is fine, then female;".format('female'), model35.wv.most_similar(positive=['female', 'fine'], negative=['male'], topn=15))
print("If male is certain, then female;".format('female'), model35.wv.most_similar(positive=['female', 'certain'], negative=['male'], topn=15))
print("If male is formal, then female;".format('female'), model35.wv.most_similar(positive=['female', 'formal'], negative=['male'], topn=15))
print("If male is typical, then female;".format('female'), model35.wv.most_similar(positive=['female', 'typical'], negative=['male'], topn=15))
print("If male is trainable, then female;".format('female'), model35.wv.most_similar(positive=['female', 'trainable'], negative=['male'], topn=15))
print("If male is listener, then female;".format('female'), model35.wv.most_similar(positive=['female', 'listener'], negative=['male'], topn=15))
print("If male is sincere, then female;".format('female'), model35.wv.most_similar(positive=['female', 'sincere'], negative=['male'], topn=15))
print("If male is disciplined, then female;".format('female'), model35.wv.most_similar(positive=['female', 'disciplined'], negative=['male'], topn=15))
print("If male is eager, then female;".format('female'), model35.wv.most_similar(positive=['female', 'eager'], negative=['male'], topn=15))
print("If male is extraordinary, then female;".format('female'), model35.wv.most_similar(positive=['female', 'extraordinary'], negative=['male'], topn=15))
print("If male is humble, then female;".format('female'), model35.wv.most_similar(positive=['female', 'humble'], negative=['male'], topn=15))
print("If male is introvert, then female;".format('female'), model35.wv.most_similar(positive=['female', 'introvert'], negative=['male'], topn=15))
print("If male is overqualified, then female;".format('female'), model35.wv.most_similar(positive=['female', 'overqualified'], negative=['male'], topn=15))
print("If male is satisfactory, then female;".format('female'), model35.wv.most_similar(positive=['female', 'satisfactory'], negative=['male'], topn=15))
print("If male is overqualified, then female;".format('female'), model35.wv.most_similar(positive=['female', 'overqualified'], negative=['male'], topn=15))


# FEMALES #
print("If female is strong, then male;".format('male'), model35.wv.most_similar(positive=['male', 'strong'], negative=['female'], topn=15))
print("If female is understanding, then male;".format('male'), model35.wv.most_similar(positive=['male', 'understanding'], negative=['female'], topn=15))
print("If female is decent, then male;".format('male'), model35.wv.most_similar(positive=['male', 'decent'], negative=['female'], topn=15))
print("If female is happy, then male;".format('male'), model35.wv.most_similar(positive=['male', 'happy'], negative=['female'], topn=15))
print("If female is straightforward, then male;".format('male'), model35.wv.most_similar(positive=['male', 'straightforward'], negative=['female'], topn=15))
print("If female is capable, then male;".format('male'), model35.wv.most_similar(positive=['male', 'capable'], negative=['female'], topn=15))
print("If female is fun, then male;".format('male'), model35.wv.most_similar(positive=['male', 'fun'], negative=['female'], topn=15))
print("If female is strange, then male;".format('male'), model35.wv.most_similar(positive=['male', 'strange'], negative=['female'], topn=15))
print("If female is communicative, then male;".format('male'), model35.wv.most_similar(positive=['male', 'communicative'], negative=['female'], topn=15))
print("If female is desperate, then male;".format('male'), model35.wv.most_similar(positive=['male', 'desperate'], negative=['female'], topn=15))
print("If female is determined, then male;".format('male'), model35.wv.most_similar(positive=['male', 'determined'], negative=['female'], topn=15))
print("If female is impressive, then male;".format('male'), model35.wv.most_similar(positive=['male', 'impressive'], negative=['female'], topn=15))
print("If female is motivated, then male;".format('male'), model35.wv.most_similar(positive=['male', 'motivated'], negative=['female'], topn=15))
print("If female is passionate, then male;".format('male'), model35.wv.most_similar(positive=['male', 'passionate'], negative=['female'], topn=15))
print("If female is promising, then male;".format('male'), model35.wv.most_similar(positive=['male', 'promising'], negative=['female'], topn=15))
print("If female is shy, then male;".format('male'), model35.wv.most_similar(positive=['male', 'shy'], negative=['female'], topn=15))
print("If female is straightforward, then male;".format('male'), model35.wv.most_similar(positive=['male', 'straightforward'], negative=['female'], topn=15))
