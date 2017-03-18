import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1'],'B':['B0','B1']},index=[0,1])
df2 = pd.DataFrame({'C':['C0','C1']},index=[0,1])

df3= pd.concat([df1,df2],axis=2)
print(df3.head())

