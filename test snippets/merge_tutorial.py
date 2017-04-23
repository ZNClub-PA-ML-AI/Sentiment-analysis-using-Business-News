import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1'],'B':['B0','B1']},index=[0,1])
df2 = pd.DataFrame({'C':['C0','C1']},index=[0,1])

df3= pd.concat([df1,df2],axis=2)
#print(df3.head())

df = pd.read_csv('REL.csv')
#df = df.set_index(['date'])
df = df.sort_values(['date'],ascending=[1])

df.to_csv('REL.csv',sep=',',encoding='utf-8')
