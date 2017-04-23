"""
Created on Mon Mar 19 9:21:10 2017

@author: ZNevzz
"""

import pandas as pd
from datetime import datetime as dt

# read file
sys_path='../../../data/processed/'

filenames = [sys_path+'data_merged.csv']
df = pd.read_csv(filenames[0])
#print(df.head(2))
#print(df.columns)

# drop last id column

df.drop(df.columns[6],axis=1,inplace=True)
#print(df.columns)

# date extraction algo

def date_ext(date_format):
	#date_format="Wed, Nov 09 2016. 10 38 PM"
	splitter = date_format.split()
	#print(splitter)
	
	month={'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}
	
	date = splitter[3][0:-1]+'-'+month[splitter[1]]+'-'+splitter[2]
	#print(date)
	return date

# time extraction algo

def time_ext(date_format):
		
	splitter = date_format.split()
	splitter_time=splitter[4]+':'+splitter[5]+' '+splitter[6]
	#print(splitter_time)
	
	time_str = str(dt.strptime(splitter_time,'%I:%M %p'))
	time=time_str[11:16]
	#print(time)
	return time

result=pd.DataFrame()

for i,r in df.iterrows():
	temp=pd.DataFrame({'date':[date_ext(str(r.date))],'time':[time_ext(str(r.date))],'title':[r.title],'intro':[r.intro],'body':[r.body],'id':[r.id]})
	result=pd.concat([result,temp])

result=result.set_index(['date'])
print(result.head(2))
result.to_csv(sys_path+'normalized.csv',sep=',',encoding='utf-8')




