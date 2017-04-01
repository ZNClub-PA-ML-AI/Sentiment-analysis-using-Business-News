

"""
Created on Wed Mar 22 11:41:40 2017

@author: ZNevzz
"""

import pandas as pd
from collections import defaultdict
import re

# read file
filenames=['labeled.csv','company_keyword.xlsx']
df = pd.read_csv(filenames[0])

#print(df.describe(),df.head())

helper = defaultdict(list)
#keywords='Reliance Industries,Mukesh Ambani,Anil Ambani,Reliance Commercial Corporation,RELIANCE,RIL,Jio'
keywords='Tata Consultancy Services,TCS,Natarajan Chandrasekaran,Ratan Tata,Tata Group,JRD Tata,J.R.D. Tata,F.C. Kohli,FC Kohli'
others=',information technology,I.T.,IT Industry,ITes'
keywords=keywords+others
helper['TCS']=keywords.split(',')

#print(helper)
c=0
result = pd.DataFrame()

for i,r in df.iterrows():
	t=str(r.title).lower()
	i=str(r.intro).lower()
	b=str(r.body).lower()
	
	for k in helper['TCS']:
		pattern=k.lower()
		if re.search(pattern,i) or re.search(pattern,t) or re.search(pattern,b):
			c=c+1
			temp=pd.DataFrame({'date':[r.date],'id':[r.id],'time':[r.time],'title':[r.title],'intro':[r.intro],'body':[r.body],'score':[r.score]})
			result=pd.concat([result,temp])
			break
#print(c)
result = result.set_index(['score'])
print(result.describe())
result.to_csv('TCS.csv',encoding='utf-8',sep=',')

