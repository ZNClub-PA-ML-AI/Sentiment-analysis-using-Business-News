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
	for index,row in df.iterrows():
		splitter=row.href.split("/")
#		test=splitter[4]
		rdf=pd.DataFrame({'id':splitter[4],'date':[row.date],'title':[row.title],'intro':[row.intro]})
#	print(test)		
	rdf.set_index('id', inplace=True)
	return rdf

filenames_d = ['livemint_data.csv','livemint_data_2.csv']
filenames_b = ['livemint_data_body.csv','livemint_data_body_2.csv']

for i in filenames_d:
	df=pd.read_csv(i,encoding='iso-8859-1')
	print(df.columns)
	result=generate(df)
#	print(result.head(2))
	result.to_csv('data_o1.csv', sep=',', encoding='utf-8')
