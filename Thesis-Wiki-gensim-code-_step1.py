print('importing files')
import re
import gensim
import bz2
import xml.sax
import mwparserfromhell
from datetime import datetime


import spacy
nlp = spacy.load("el_core_news_sm")
nlp.max_length = 733629200

data_path = 'D:\Downloads\elwiki-20191220-pages-articles.xml.bz2'

print('reading file')
print(datetime.now())
class WikiXmlHandler(xml.sax.handler.ContentHandler):
    """Content handler for Wiki XML data using SAX"""

    def __init__(self):
        xml.sax.handler.ContentHandler.__init__(self)
        self._buffer = None
        self._values = {}
        self._current_tag = None
        self._pages = []

    def characters(self, content):
        """Characters between opening and closing tags"""
        if self._current_tag:
            self._buffer.append(content)

    def startElement(self, name, attrs):
        """Opening tag of element"""
        if name in ('title', 'text', 'timestamp'):
            self._current_tag = name
            self._buffer = []

    def endElement(self, name):
        """Closing tag of element"""
        if name == self._current_tag:
            self._values[name] = ' '.join(self._buffer)

        if name == 'page':
            self._pages.append((self._values['title'], self._values['text']))


# Content handler for Wiki XML
handler = WikiXmlHandler()

# Parsing object
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
print('enumerating')
print(datetime.now())
lines = []
for i, line in enumerate(bz2.BZ2File(data_path, 'r')):
    parser.feed(line)
    if len(handler._pages) > 361000:
        break

		
print('parsing file')
print(datetime.now())

document = 'a'
doc_list=[]

for i in range(0,  361000):
    wiki = mwparserfromhell.parse(handler._pages[i][1])
    tmp = wiki.strip_code().strip()
    #document = document + str(' ') + str(tmp)
    doc_list.append(tmp)


print('done parsing file and joining list')
print(datetime.now())
document=" ".join(doc_list)

#print(document)
print('begin writing file')
print(datetime.now())



import io
with io.open('D:\document_parsed.txt', "w", encoding="utf-8") as f:
    f.write("%s" % document)



