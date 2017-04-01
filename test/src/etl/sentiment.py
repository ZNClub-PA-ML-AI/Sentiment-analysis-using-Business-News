"""
Created on Mon Mar 20 11:41:40 2017

@author: ZNevzz
"""

import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
import time
start=time.time()


# read file
filenames=['../../normalized.csv']
df = pd.read_csv(filenames[0])

def sentiment_cal(title,intro,body):
	
	sia = SentimentIntensityAnalyzer()
	tscore = sia.polarity_scores(title)
	iscore= sia.polarity_scores(intro)
	bscore= sia.polarity_scores(body)
	tscore = float(tscore['compound'])
	iscore = 0.5*float(iscore['compound'])
	bscore = 0.25*float(bscore['compound'])
	max_pos,max_neg=1.0,-1.0
	score=(tscore+iscore+bscore)
	if score>max_pos:
		score=max_pos
	elif score<max_neg:
		score=max_neg
	return round(score,2)


result = pd.DataFrame()
for i,r in df.iterrows():
	score=sentiment_cal(str(r.title),str(r.intro),str(r.body))
	temp=pd.DataFrame({'date':[r.date],'time':[r.time],'id':[r.id],'title':[r.title],'intro':[r.intro],'body':[r.body],'score':[score]})
	result = pd.concat([result,temp])
#print(result.head(2))

result.to_csv('../../labeled_round.csv',encoding='utf-8',sep=',')
print(time.time()-start)


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
for i in i_list:
	ps = sia.polarity_scores(i)
	print(ps['compound'],ps['pos'],ps['neg'],ps['neu'])
	iis.append(ps['compound'])

b_list = df.body.tolist()[:4]
for i in i_list:
	ps = sia.polarity_scores(i)
	print(ps['compound'],ps['pos'],ps['neg'],ps['neu'])
	iis.append(ps['compound'])

b_list = df.body.tolist()[:4]
for i in i_list:
	ps = sia.polarity_scores(i)
	print(ps['compound'],ps['pos'],ps['neg'],ps['neu'])
	iis.append(ps['compound'])

b_list = df.body.tolist()[:4]
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
