# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 15:12:06 2017

@author: ZNevzz
"""
import nltk
import codecs
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter

#def read():
#    with codecs.open('sample_news.txt','r',encoding='utf8') as f:
#        text = f.read()
#        text = text.lower()
#        #print(text)
#        return text
#        
#        
    
#bigrams = ngrams(token,2)
#trigrams = ngrams(token,3)
#fourgrams = ngrams(token,4)
#fivegrams = ngrams(token,5)

    ## read file
#text = read()

text={'cid':'','title':'','intro':'','body':'','datetime':''}



tokens = nltk.word_tokenize(text)
#print(tokens)

unigram = tokens

#print(unigram)
bigrams = ngrams(tokens,2)
#print(Counter(bigrams))
trigrams = ngrams(tokens,3)
#print(Counter(trigrams))



