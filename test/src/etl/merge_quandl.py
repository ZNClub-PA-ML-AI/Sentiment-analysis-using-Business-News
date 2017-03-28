



import pandas as pd
import sys

filenames=[sys.argv[1],sys.argv[2]]

#sentiment csv
df1=pd.read_csv(filenames[0])
df1=df1.set_index('date')
#print(df1.head(1))

#quandl csv
df2=pd.read_csv(filenames[1])
df2=df2.set_index('Date')
#print(df2.head(1))

df3=pd.concat([df1,df2],axis='1',join='inner')
#print(df3.head(1),df3.columns,df3.describe())

print(df1.shape)

