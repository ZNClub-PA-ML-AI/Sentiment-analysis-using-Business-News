import pandas as pd
import collections

df = pd.read_csv('REL.csv')
date_list = df.date.tolist()
dates=set(date_list)
#print(len(dates))

result=pd.DataFrame()
cnt = collections.Counter(date_list)
#print(len(cnt))

for k,v in cnt.items():
	print(k,v)


"""
for i,r in df.iterrows():
	date=str(r.date)
	if prev=-1 or prev!=date:
		prev=
"""

#df = df.set_index(['date'])
#df.to_csv('REL.csv',sep=',',encoding='utf-8')

