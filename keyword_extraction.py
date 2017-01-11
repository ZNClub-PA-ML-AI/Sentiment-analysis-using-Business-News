# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 10:42:03 2017

@author: ZNevzz
"""

import re
import pandas as pd

#print(re.search("tara","tcs "))

    ## read text and pattern files


    ## text file
file_name = ['economictimes_data.csv','livemint_data.csv']
#
#df = pd.read_csv(file_name[0],encoding='iso-8859-1')
#print(df.head())

df = pd.read_csv(file_name[1],encoding='iso-8859-1')
#print(df.head())

#print(df['title'])
news_list=df['title'].tolist()
#print(len(news_list))


    ## pattern file
df = pd.read_excel('company_keyword.xlsx', sheetname='Sheet1')
#print(df.head())
#print(df['company'].count())
#
#describe=df.describe()
#print(describe.company)

#
#count=0
#for index, row in df.iterrows():
#        #print(row.company,row.keyword)
#        k = row.company
#        v = row.keyword
#        v_list = v.split(',')
##        print(v_list)
#        for i in v_list:
#            print(i)
#            count+=1
#
#print(count)

    ## create dataframe filtered news

f_news = pd.DataFrame()

for index, row in df.iterrows():
    df2 = pd.DataFrame({row.company:[]})
    f_news = f_news.append(df2)

    
#f_news = pd.DataFrame()





count=0
for news in news_list:
    news = news.lower()
    #print(news)
    
    for index, row in df.iterrows():
        #print(row.company,row.keyword)
        k = row.company
        
        v = row.keyword
        v_list = v.split(',')
        #print(k)
        for i in v_list:
            i=i.lower()
            if re.search(i,news):
                print(k+"---"+news)
                count+=1
#                df2 = pd.DataFrame()
#                f_news[k].append(news)
                ## add company as column
                

print(count)           
print(len(news_list))    
print(f_news.head())
