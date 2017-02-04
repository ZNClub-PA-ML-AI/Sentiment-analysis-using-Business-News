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

text={
'cid':'GAIL',
'title':'GAIL stock: good results priced in',
'intro':'Investors will require more than one good quarter from GAIL to alter their view on the stock',
'body':"Investors will require more than one good quarter from GAIL (India) Ltd to alter their view on the stock, partly because the stock has gone up by almost a fourth in the last three months.One reason for this outperformance is the renegotiation of Qatar’s RasGas liquefied natural gas (LNG) contract announced at the end of December, which is expected to reduce input costs in GAIL’s petrochemicals business. But with petrochemical prices coming down, one will have to see whether the segment’s profit improves meaningfully. For the December quarter, the loss before interest and tax for the petrochemicals business dropped to Rs.161 crore from Rs.237 crore seen in the September quarter. The performance could have been better if it were not for stabilization issues faced at the new petrochemicals plant. As Jefferies Equity Research notes, given management commentary that GAIL almost entirely used spot LNG in the third quarter versus mainly RasGas in the second quarter (which was costlier), earnings improvement in petrochemicals was below par.Nevertheless, GAIL’s overall results did beat expectations. Its gas trading business exceeded expectations, reporting earnings before interest and tax of Rs.483 crore against Rs.51 crore for the year-ago period and Rs.193 crore in the September quarter. Gas pooling for the power sector fetched additional trading volumes sequentially. The company’s transmission business too performed well.The upshot: net profit increased 10% year-on-year to Rs.664 crore despite a 10% decline in revenues. Strong other income growth helped.What next? Gas volumes can go up once the increased LNG supplies from RasGas start and once power pooling is implemented in certain states like Andhra Pradesh (still pending due to taxation issues), point out JM Financial analysts.Currently, GAIL trades at 12.5 times estimated earnings for the next fiscal year. Given the rally in the stock over the last three months, most catalysts such as higher crude oil price, positive impact of lower gas price, transmission tariff revision and pickup in transmission volumes seem to be priced in, says Jefferies.",
'date':'Sep 30, 2016, 01:36 AM IST'
}







tokens = nltk.word_tokenize(text['title'])
#print(tokens)

unigram = tokens

print(unigram)


#bigrams = ngrams(tokens,2)
#print(Counter(bigrams))
#trigrams = ngrams(tokens,3)
#print(Counter(trigrams))



