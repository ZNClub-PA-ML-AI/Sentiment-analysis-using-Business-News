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

result = pd.DataFrame()
for i,r in df.iterrows():
	score=sentiment_cal(str(r.title),str(r.intro),str(r.body))
	temp=pd.Dataframe({'date':[r.date],'time':[r.time],'id':[r.id],'title':[r.title],'intro':[r.intro],'body':[r.body],'score':[score]})
	result = pd.concat([result,temp])


"""

# test vader with title
sia = SentimentIntensityAnalyzer()

t_list = df.title.tolist()[:4]
ts=[]
for t in t_list:
	ps = sia.polarity_scores(t)
	print(ps['compound'],ps['pos'],ps['neg'],ps['neu'])
	ts.append(ps['compound'])	

i_list = df.intro.tolist()[:4]
iis=[]
for i in i_list:
	ps = sia.polarity_scores(i)
	print(ps['compound'],ps['pos'],ps['neg'],ps['neu'])
	iis.append(ps['compound'])

b_list = df.body.tolist()[:4]
bs=[]
for b in b_list:
	ps = sia.polarity_scores(b)
	print(ps['compound'],ps['pos'],ps['neg'],ps['neu'])
	bs.append(ps['compound'])

score=[0 for i in range(4)]

print(ts,iis,bs)

for i in range(0,4):
	print(i,ts[i],iis[i],bs[i])
	score[i]=ts[i]+(iis[i]*float(0.5))+(bs[i]*float(0.25))
print(score)
"""
