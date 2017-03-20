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


# test vader with title

t_list = df.title.tolist()[:4]
print(len(t_list))
sia = SentimentIntensityAnalyzer()

for t in t_list:

	ps = sia.polarity_scores(t)
	print(ps['compound'])


print("ends")

