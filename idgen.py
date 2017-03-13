import pandas as pd
import codecs

#read file

import re
import pandas as pd
from collections import defaultdict
from numpy import array
import csv

def generate(df):
	test=''
	result=pd.DataFrame()
	for index,row in df.iterrows():
		splitter=row.href.split("/")
#		test=splitter[4]
		rdf=pd.DataFrame({'id':splitter[4],'body':[row.body]})
		result=pd.concat([result,rdf])
#	print(test)		
	result.set_index('id', inplace=True)
	return result

filenames_d = ['livemint_data.csv','livemint_data_2.csv']
filenames_b = ['livemint_data_body.csv','livemint_data_body_2.csv']
output=[]
for i in filenames_b:
	df=pd.read_csv(i,encoding='iso-8859-1')
	print(df.columns)
	output.append(generate(df))
#	print(result.head(2))


out=pd.DataFrame()

for i in output:
	out=pd.concat([out,i])
print(out.describe())
out.to_csv('data_o2.csv', sep=',', encoding='utf-8')





