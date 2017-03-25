"""
Created on Thu Mar 23 20:58:21

import datetime
"""

import pandas as pd
import collections

df = pd.read_csv('REL.csv')
date_list = df.date.tolist()
dates=set(date_list)
#print(len(dates))

result=pd.DataFrame()
cnt = collections.Counter(date_list)
#print(len(cnt))

od = collections.OrderedDict(sorted(cnt.items()))

score=dict()
for k,v in od.items():
	print(k,v)
	score[k]=0


for i,r in df.iterrows():
	date=str(r.date)
	time=datetime.datetime.strptime(str(r.time),'%H:%M')
	time_open=datetime.datetime.strptime('09:00','%H:%M')
	time_close=datetime.datetime.strptime('16:00','%H:%M')
	
	#before open time
	if time<=time_open:
		score[date]+=float(r.score)
	#after close time
	elif time>time_close:
		date=date.split('-')
		day=date[2]
		day=int(day)+1
		new_date=date[0]+'-'+date[1]+'-'+str(day)
		score[new_date]+=float(r.score)
	elif time in range(time_open,time_close):
		pass

for k,v in od.items():
	score[k]=score[k]/v
	print(k,score[k])
#print(len(score))
#print(score)

df=pd.DataFrame(score,index=['score'])
df=df.transpose()
df.to_csv('REL_score_open.csv',sep=',',encoding='utf-8')
df.to_json('REL_score_open.json')






#print(score)

df=pd.DataFrame(score,index=['score'])
df=df.transpose()
df.to_csv('REL_score_open.csv',sep=',',encoding='utf-8')
df.to_json('REL_score_open.json')





