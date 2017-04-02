


import pandas as pd
import sys

#filenames=[sys.argv[1],sys.argv[2]]
filenames=['../../TCS_score_open.csv','../../TCS_score_close.csv']

#open.csv
df1=pd.read_csv(filenames[0])
df1.columns=['date','open_score']
#print(df1.head(2))

#close.csv
df2=pd.read_csv(filenames[1])
df2.columns=['date','close_score']

#df1=df1.set_index('date')

result=pd.concat([df1,df2],axis=1,join='inner')
out=pd.DataFrame(result[[0,1,3]])
print(out.head(23))
#print(result.head(23),result.describe(),result.columns)

#write to csv
print(filenames[0][6:9])
#out.to_csv('../../../data/processed/'+filenames[0][6:9]+'_sentiment.csv',encoding='utf-8',sep=',')

out.to_csv('../../'+filenames[0][6:9]+'_sentiment.csv',encoding='utf-8',sep=',')



