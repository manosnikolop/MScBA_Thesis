print('importing files')
import re
import gensim
import bz2
import xml.sax
import mwparserfromhell
import spacy


# First install spacy

# What each tag means (e.g. PUNCT=Punctuation) can ne found here:
#glossary here: https://github.com/explosion/spaCy/blob/master/spacy/glossary.py

# Then run this on console. it is a greek pretrained model that matches a word to its tag
#python -m spacy download el_core_news_sm

# Set up spacy
import en_core_web_sm
nlp = en_core_web_sm.load()

nlp.max_length = 17000000

female_data_path = 'D:\Downloads\Female_evaluations_values.txt'
male_data_path = 'D:\Downloads\Male_evaluations_values.txt'

print('reading files')

female_file= open(female_data_path, "r", encoding="utf8")
female_data = female_file.read() 
#print(female_data) 

male_file= open(male_data_path, "r", encoding="utf8")
male_data = male_file.read() 
#print(female_data) 

## Spacy - Female ###
print('Female data preparation')
print('clearing nouns')

female_data = re.sub(r"[^a-zA-Z0-9]+", ' ', female_data)

female_document_nlp=nlp(female_data,disable = ['ner', 'parser'])

keep=['NOUN','PROPN','NN','NNP','NNPS','NNS','NE','NNE','NP','ADJ','JJ','JJR','JJS','ADJA','ADJD','ADJP' ]
female_final_doc=''

for female_token in female_document_nlp:
    #print(female_token.text, female_token.tag_, female_token.is_stop)
    if female_token.tag_ in keep:
        female_final_doc = female_final_doc + str(' ') + str(female_token.text)


female_paras = [w for w in female_final_doc.lower().split()]

female_paras = [i for i in female_paras if len(i) > 2]

from collections import Counter

counts = Counter(female_paras)

print(type(counts))
print(counts)


#Write outcome to file '|' seperated word|frequency
print('write in file')
with open('female_test1.csv', encoding='utf-8-sig', mode='w') as fp:
    fp.write('KMC|freq\n')  
    for tag, count in counts.items():  
        fp.write('{}|{}\n'.format(tag, count))  
		

## Spacy - Male ###
print('Male data preparation')
print('clearing nouns')

male_data = re.sub(r"[^a-zA-Z0-9]+", ' ', male_data)

male_document_nlp=nlp(male_data,disable = ['ner', 'parser'])

keep=['NOUN','PROPN','NN','NNP','NNPS','NNS','NE','NNE','NP','ADJ','JJ','JJR','JJS','ADJA','ADJD','ADJP' ]
male_final_doc=''

for male_token in male_document_nlp:
    #print(female_token.text, female_token.tag_, female_token.is_stop)
    if male_token.tag_ in keep:
        male_final_doc = male_final_doc + str(' ') + str(male_token.text)


male_paras = [w for w in male_final_doc.lower().split()]

male_paras = [i for i in male_paras if len(i) > 2]

from collections import Counter

counts = Counter(male_paras)

print(type(counts))
print(counts)
    

#print(female_data)
#print(female_paras)

#Write outcome to file '|' seperated word|frequency
print('write in file')
with open('male_test1.csv', encoding='utf-8-sig', mode='w') as fp:
    fp.write('KMC|freq\n')  
    for tag, count in counts.items():  
        fp.write('{}|{}\n'.format(tag, count))  