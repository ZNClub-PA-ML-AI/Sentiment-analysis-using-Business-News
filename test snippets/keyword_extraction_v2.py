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
df4 = pd.DataFrame(columns=('company','date','title','intro','href'))
df6 = pd.DataFrame(columns=('company','href'))
df7 = pd.DataFrame(columns=('company','href'))

for index, row in df3.iterrows():
    helper[row.company] = list(row.keyword.split(","))

for index, row in df1.iterrows():
    
    for key, value in helper.items():
        
        for v in value:
            
            title_pattern = row.title.lower()
            intro_pattern = row.intro.lower()
            v = v.lower()
            
            if re.search(v,title_pattern) or re.search(v,intro_pattern):
                #print(v+"--"+pattern)
                df5 = pd.DataFrame({'company':key,
                                    'date':[row.date],
                                   'title':[row.title.lower()],
                                   'intro':[row.intro.lower()],
                                   'href':[row.href]
                                   })
                df4 = pd.concat([df4,df5])
                
                df5 = pd.DataFrame({'company':[key],'href':[row.href]})
                df6 = pd.concat([df6,df5])

print(df4.shape[0]*100/df1.shape[0])

df1_out = df4.shape[0]


for index, row in df2.iterrows():
    
    for key, value in helper.items():
        
        for v in value:
            
            title_pattern = row.title.lower()
            intro_pattern = row.intro.lower()
            v = v.lower()
            
            if re.search(v,title_pattern) or re.search(v,intro_pattern):
                #print(v+"--"+pattern)
                df5 = pd.DataFrame({'company':key,
                                    'date':[row.date],
                                   'title':[row.title.lower()],
                                   'intro':[row.intro.lower()],
                                   'href':[row.href]
                                   })
                df4 = pd.concat([df4,df5])
                df5 = pd.DataFrame({'company':[key],'href':[row.href]})
                df7 = pd.concat([df7,df5])

print((df4.shape[0] - df1_out)*100/df2.shape[0])

print(df1_out,df6.shape[0],(df4.shape[0] - df1_out),df7.shape[0])

#
#df4.to_csv('output_89.csv', sep=',', encoding='utf-8')
#df6.to_csv('economictimes_href.csv', sep=',', encoding='utf-8')
#df7.to_csv('livemint_href.csv', sep=',', encoding='utf-8')
#        




