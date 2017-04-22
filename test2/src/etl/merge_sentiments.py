


import pandas as pd
import sys
import platform

if platform.system()=='Windows':
    company_id='AX'
else:
    company_id=sys.argv[1]

filenames=['../../'+company_id+'_score_open.csv','../../'+company_id+'_score_close.csv']

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

out.to_csv('../../'+company_id+'_sentiment.csv',encoding='utf-8',sep=',')



