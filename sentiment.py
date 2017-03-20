"""
Created on Mon Mar 20 11:41:40 2017

@author: ZNevzz
"""

import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize

# read file
filenames=['normalized.csv']
df = pd.read_csv(filenames[0])

def sentiment_cal(title,intro,body):
	
	sia = SentimentIntensityAnalyzer()

	#t_score = 

	return


# test vader with title,intro

#t_list = df.title.tolist()[:4]
i_list = df.intro.tolist()[:4]
print(len(i_list))
sia = SentimentIntensityAnalyzer()

#for t in t_list:
for i in i_list:
	ps = sia.polarity_scores(i)
	print(ps['compound'])


print("ends")

