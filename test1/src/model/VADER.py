# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 20:30:36 2017

@author: ZNevzz
"""

import nltk.sentiment.vader as vad
import re

def sentiment_cal(title,intro,body):
    
    sia = vad.SentimentIntensityAnalyzer()
    tscore = sia.polarity_scores(title)
    iscore= sia.polarity_scores(intro)
    bscore= sia.polarity_scores(body)
    tscore = float(tscore['neg'])
    iscore = float(iscore['compound'])
    bscore = float(bscore['compound'])
    #max_pos,max_neg=1.0,-1.0
    score=(tscore+iscore+bscore)
    
    return round(score,2)

t='The consequences of declining trust in CEOs'
i=''
b=''

print(sentiment_cal(t,i,b))
#
#a='IT'.lower()
#
#c='interest'.lower()
#
#print(re.search(a,c))
#
##print(vad.re)
#
#IT='information technology,IT,IT Industry'.split(',')
#print(IT)
#for k in IT:
#    print(re.search(k.lower(),b.lower()))
#    
#
