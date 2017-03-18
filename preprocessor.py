"""
Created on Mon Mar 18 11:27:40 2017
@author: ZNevzz
"""
from bs4 import BeautifulSoup
import pandas as pd

#read file
filenames=['data_o2.csv']
'''
html='<p xmlns:fn=""http://www.w3.org/2005/xpath-functions"" id=""U10478744187zRC"" style="" letter-spacing: -7; ;"">The December quarter result of auto component'

#print(BeautifulSoup.(html).get_text())
t=BeautifulSoup(html,"lxml")
tt=t.get_text()
print(tt)
'''

df1=pd.read_csv(filenames[0])
#print(df1.head(1))

df2=pd.DataFrame()
for k,r in df1.iterrows():
	temp1=BeautifulSoup(str(r.body),"lxml")
	df=pd.DataFrame({'id':[r.id],'body':[temp1.get_text()]})
	df2=pd.concat([df2,df])
df2.to_csv('data_o3.csv', sep=',', encoding='utf-8')


