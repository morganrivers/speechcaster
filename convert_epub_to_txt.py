from gtts import gTTS

# from ebooklib import epub
# import ebooklib
# import os
# import nltk
# input_path = r"/home/dmrivers/Documents/Books/"
# german_corpus = []
# book = epub.read_epub(os.path.join(input_path,'Aldous Huxley, Brave New World (2010).epub'))
# i = 0
# # print("book.get_items()")
# # print(book.get_items())
# for doc in book.get_items():
#     doc_content = str(doc.content)
#     print("nltk.word_tokenize(doc_content)")
#     print(nltk.word_tokenize(doc_content))
#     for w in nltk.word_tokenize(doc_content):
#         german_corpus.append(w.lower())
#         print(w.lower())
#         quit()
#         if(i==10):
#             print(german_corpus)
#             quit()

#another, more successful attempt

# import ebooklib
# from ebooklib import epub

# book = epub.read_epub('/home/dmrivers/Documents/Books/Aldous Huxley, Brave New World (2010).epub')

# for doc in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
#     print(doc.content)
#     quit()


#copied wholesale from https://xwiki.recursos.uoc.edu/wiki/mat00001ca/view/Research%20on%20Translation%20Technologies/Working%20with%20PDF%20files%20using%20Python/

import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import sys
import codecs

def chap2text(chap):
    output = ''
    soup = BeautifulSoup(chap, 'html.parser')
    text = soup.find_all(text=True)
    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)
    return output
  
blacklist = [   '[document]',   'noscript', 'header',   'html', 'meta', 'head','input', 'script',   ]

bookname='/home/dmrivers/Documents/Books/Aldous Huxley, Brave New World (2010).epub'
outputname='out.txt'

outputfile=codecs.open(outputname,"w",encoding="utf-8")

book = epub.read_epub(bookname)

chapters = []
for item in book.get_items():
    if item.get_type() == ebooklib.ITEM_DOCUMENT:
        chapters.append(item.get_content())

for chapter in chapters:
    text=chap2text(chapter)
    outputfile.write(text+"\n")