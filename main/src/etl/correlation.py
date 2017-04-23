


import pandas as pd


df=pd.read_csv('../../TCS_qs.csv')

#print(dir(df))
result=df.corr(method='pearson',min_periods=1)



#print(result)

result=df.cov()
print(result)

#result.to_csv('../../REL_corr.csv',encoding='utf-8',sep=',')


