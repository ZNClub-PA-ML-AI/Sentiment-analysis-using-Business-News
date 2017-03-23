"""
Created on Mon Mar 20 11:41:40 2017

@author: ZNevzz
"""

import pandas as pd
from collections import defaultdict
import re

# read file
filenames=['labeled.csv','company_keyword.xlsx']
df = pd.read_csv(filenames[0])

print(df.describe(),df.head())

helper = defaultdict(list)
keywords='Reliance Industries,Mukesh Ambani,Anil Ambani,Reliance Commercial Corporation,RELIANCE,RIL,Jio'
helper['REL']=keywords.split(',')

print(helper)
c=0
for i,r in df.iterrows():
	t=str(r.title).lower()
	i=str(r.intro).lower()
	pattern=k.lower()
	for k in helper['REL']:
		if re.search(pattern,i) or re.search(pattern,t):
			c=c+1
			break
print(c)

