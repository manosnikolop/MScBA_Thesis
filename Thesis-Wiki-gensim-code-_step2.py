print('importing files')
import re
import gensim
import bz2
import xml.sax
import mwparserfromhell
import io
from datetime import datetime



import spacy
nlp = spacy.load("el_core_news_sm")
nlp.max_length = 733629200

################ we parse the files individualy to minimize RAM consumption ################
################ Example parsing file 10. Rest of files in data folder      ################ 
with io.open('D:\document_parsed10.txt','r',encoding="utf-8") as file:
    document=file.read()
    file.close()
    #print(document)


print('cleaning text')
print(datetime.now())

document = re.sub(r"[^A-Za-z0-9 + .\s + Α-Ωα-ωίϊΐόάέύϋΰήώ]+", '', document)
document=re.sub('\d','',document)

# Common text 'garbage' (image names, attachments, hyperlinks etc.)
document = re.sub(r'\S+png', '', document)
document = re.sub(r'\S+jpg', '', document)
document = re.sub(r'\S+gif', '', document)
document = re.sub(r'\S+pdf', '', document)
document = re.sub(r'\S+px', '', document)
document = re.sub(' thumb ', '', document)
document = re.sub(r'href\S+', '', document)
document = re.sub(r'&lt\S+', '', document)
document = re.sub(r'class\S+', '', document)
document = re.sub(r'title\S+', '', document)
document = re.sub(r'File:\S+', '', document)
document = re.sub(r'Αρχείο:\S+', '', document)
document = re.sub(r'style=\S+', '', document)
document = re.sub(r'widths=\S+', '', document)
document = re.sub(r'heights=\S+', '', document)
document = re.sub(r'http\S+', '', document)
document = re.sub(r'https\S+', '', document)
document = re.sub(r'&quot;\S+', '', document)
document = re.sub("li", " ", document)
document = re.sub("/li", " ", document)
document = re.sub("ul", " ", document)
document = re.sub("/ul", " ", document)
document = re.sub("em", " ", document)
document = re.sub("Ank", " ", document)
document = re.sub("uploaded", " ", document)

print('clearing nouns')
print(datetime.now())

document_nlp=nlp(document,disable = ['ner', 'parser'])
keep=['NOUN','PROPN','NN','NNP','NNPS','NNS','NE','NNE','NP','ADJ','JJ','JJR','JJS','ADJA','ADJD','ADJP' ]
final_doc_list=[]
final_doc=''
for token in document_nlp:
    #print(token.text, token.tag_, token.is_stop)
    if token.tag_ in keep:
        #final_doc = final_doc + str(' ') + str(token.text)
        final_doc_list.append(str(token.text))
final_doc = " ".join(final_doc_list)

print('begin writing file')
print(datetime.now())


################ we parse the files individualy to minimize RAM consumption ################
################ Example writing file 10. Rest of files in data folder      ################ 
with io.open('D:\spacy10.txt', "w", encoding="utf-8") as f:
    f.write("%s" % final_doc)

print('end writing file')
print(datetime.now())

