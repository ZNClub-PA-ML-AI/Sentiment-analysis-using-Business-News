


import sys
import pandas as pd

#print(sys.argv)

filename=str(sys.argv[1])
df=pd.read_csv(filename)
#df = df.set_index(['date'])
df = df.sort_values(['Date'],ascending=[1])
print(df.head(1))
#print(filename[:-3])
#df.to_json(filename[:-3]+'json')






