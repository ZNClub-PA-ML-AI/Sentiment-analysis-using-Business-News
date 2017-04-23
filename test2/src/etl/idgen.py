"""
Created on Sun Apr 23 16:43:13 2017

@author: ZNevzz
"""



import pandas as pd


def generate(df):
	
	result=pd.DataFrame()
	for index,row in df.iterrows():
		splitter=row.href.split("/")
#		test=splitter[4]
		rdf=pd.DataFrame({'id':splitter[4],'body':[row.body]})
		result=pd.concat([result,rdf])
#	print(test)		
	result.set_index('id', inplace=True)
	return result

sys_path='../../../data/'
path_in='scrapy/'
path_out='processed/'

filenames_d = ['livemint_data.csv','livemint_data_2.csv','livemint_data_3.csv']
filenames_b = ['livemint_data_body.csv','livemint_data_body_2.csv','livemint_data_body_3.csv']
output=[]

for i in filenames_d:
	df=pd.read_csv(sys_path+path_in+i,encoding='iso-8859-1')
	print(df.columns)
	output.append(generate(df))
#	print(result.head(2))


out=pd.DataFrame()

for i in output:
	out=pd.concat([out,i])
print(out.describe())

out.to_csv(sys_path+path_out+'data_o1.csv', sep=',', encoding='utf-8')





