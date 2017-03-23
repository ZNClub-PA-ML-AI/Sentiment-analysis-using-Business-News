import pandas as pd

df = pd.read_csv('REL.csv')
dates=set(df.date.tolist())
print(len(dates))


#df = df.set_index(['date'])
#df.to_csv('REL.csv',sep=',',encoding='utf-8')

