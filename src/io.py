# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 09:25:26 2017

@author: ZNevzz
"""

import pandas as pd
import codecs

df = pd.read_excel('company_keyword.xlsx', sheetname='Sheet1')
#print(df.head())
print(df.shape)

file_name = 'economictimes_data.csv'

df = pd.read_csv(file_name,encoding='iso-8859-1')
#print(df.head())
print(df.shape)

file_name = 'livemint_data.csv'

df = pd.read_csv(file_name,encoding='iso-8859-1')
#print(df.head())
print(df.shape)

  ## read file with encodings
#with codecs.open(file_name,'r',encoding='utf8') as f:
#    text = f.read()

file_name = 'output_89.csv'

df = pd.read_csv(file_name,encoding='iso-8859-1')
#print(df.head())
print(df.shape[0]*100/(1978+995))
