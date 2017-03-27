


import sys
import pandas as pd

#print(sys.argv)

filename,type=sys.argv[1],sys.argv[2]
df=pd.read_csv(filename)

if type=='q':
	df = df.sort_values(['Date'],ascending=[1])
print(df.head(1))

splitter=filename.split('/')
filename=splitter[-1]

print(filename[:-3])
df.to_json('../../../data/json/'+filename[:-3]+'json')






