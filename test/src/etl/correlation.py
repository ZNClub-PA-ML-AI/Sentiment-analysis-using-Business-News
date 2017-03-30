


import pandas as pd


df=pd.read_csv('../../REL_qs.csv')

#print(dir(df))
result=df.corr(method='pearson',min_periods=100)

print(result)
#result.to_csv('../../REL_corr.csv',encoding='utf-8',sep=',')


