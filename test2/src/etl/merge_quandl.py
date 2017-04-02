



import pandas as pd
import sys

#filenames=[sys.argv[1],sys.argv[2]]
filenames=['../../TCS_sentiment.csv','../../NSE-TCS.csv']


#sentiment csv
df1=pd.read_csv(filenames[0])
df1=df1.set_index('date')
#print(df1.head(1))

#quandl csv
df2=pd.read_csv(filenames[1])
df2=df2.set_index('Date')
#print(df2.head(1))

df3=pd.concat([df1,df2],axis='2',join='inner')
#print(df3.head(1),df3.columns,df3.describe())
#print(df3.index.values)
#print(df1.shape,df2.shape,df3.shape)

splitter=filenames[0].split('/')
filename=splitter[-1]

#print(filename[:-3])
#print(df3[[0]])

#fix first col

#in=df3[[0]]


#shape your df
df3.columns=['#','open_score','close_score','Open','High','Low','Last','Close','Total Trade Quantity','Turnover (Lacs)']

df3=df3.sort_index()
df3.to_csv('../../'+filename[:3]+'_qs.csv',encoding='utf-8',sep=',')
print(df3.head())



