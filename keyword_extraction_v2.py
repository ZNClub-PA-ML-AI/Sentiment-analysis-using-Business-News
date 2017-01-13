# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 14:40:36 2017

@author: ZNevzz
KEYWORD EXTRACTION TO NEW CSV

"""

import re
import pandas as pd
from collections import defaultdict
from numpy import array
import csv


    ## text file
file_name = ['economictimes_data.csv','livemint_data.csv']

df1 = pd.read_csv(file_name[0],encoding='iso-8859-1')
#print(df.head())

df2 = pd.read_csv(file_name[1],encoding='iso-8859-1')
#print(df.head())

    ## make dictionary from xlxs file

## pattern file
df3 = pd.read_excel('company_keyword.xlsx', sheetname='Sheet1')
helper = defaultdict(list)
df4 = pd.DataFrame(columns=('date','title','intro','href'))

for index, row in df3.iterrows():
    helper[row.company] = list(row.keyword.split(","))

for index, row in df2.iterrows():
    
    for key, value in helper.items():
        
        for v in value:
            
            pattern = row.title.lower()
            v = v.lower()
            
            if re.search(v,pattern):
                print(v+"--"+pattern)
                df5 = pd.DataFrame({'date':[row.date],
                                   'title':[row.title.lower()],
                                   'intro':[row.intro.lower()],
                                   'href':[row.href]
                                   })
                df4 = pd.concat([df4,df5])
                
                #print(df4.head())
print(df4.shape)
print(df1.shape)
df4.to_csv('filtered_news3.csv', sep=',', encoding='utf-8')

        
