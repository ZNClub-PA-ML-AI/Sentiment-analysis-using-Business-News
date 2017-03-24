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

#print(od['2015-11-04'])


for i,r in df.iterrows():
	date=str(r.date)
	score[date]+=float(r.score)

print(len(score))
print(score)

df=pd.DataFrame(score,index=['score'])
df=df.transpose()
df.to_csv('REL_score.csv',sep=',',encoding='utf-8')
df.to_json('REL_score.json')





