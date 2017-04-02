

"""
Created on Wed Mar 22 11:41:40 2017

@author: ZNevzz
"""
import sys
import pandas as pd
from collections import defaultdict
import re

# read file
filenames=['../../labeled.csv','../../../data/explicit/company_keyword.xlsx']
df = pd.read_csv(filenames[0])

#print(df.describe(),df.head())


#company keyword dict
company=pd.read_excel(filenames[1],sheetname='Sheet1')
helper = defaultdict(list)

for i,r in company.iterrows():
	helper[str(r.company)]=str(r.keyword).split(',')
#print(helper)

#id,sector=sys.argv[1],sys.argv[2]
id,sector='TCS','IT'

helper[id].extend(helper[sector])


print(helper[id])

c=0
result = pd.DataFrame()

for i,r in df.iterrows():
	t=str(r.title).lower()
	i=str(r.intro).lower()
	b=str(r.body).lower()
	
	for k in helper[id]:
		pattern=k.lower()
		if re.search(pattern,i) or re.search(pattern,t) or re.search(pattern,b):
			c=c+1
			temp=pd.DataFrame({'date':[r.date],'id':[r.id],'time':[r.time],'title':[r.title],'intro':[r.intro],'body':[r.body],'score':[r.score]})
			result=pd.concat([result,temp])
			break
#print(c)
result = result.set_index(['score'])
print(result.describe())
result.to_csv(id+'.csv',encoding='utf-8',sep=',')


