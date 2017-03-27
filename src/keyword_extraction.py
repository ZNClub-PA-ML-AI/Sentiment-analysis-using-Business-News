# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 10:42:03 2017

@author: ZNevzz
"""

import re
import pandas as pd
from collections import defaultdict
from numpy import array
import csv

    ## read text and pattern files


    ## text file
file_name = ['economictimes_data.csv','livemint_data.csv']

#df = pd.read_csv(file_name[0],encoding='iso-8859-1')
#print(df.head())

df = pd.read_csv(file_name[1],encoding='iso-8859-1')
#print(df.head())
    
    ## extract news from title column
#print(df['title'])
news_list=df['title'].tolist()
href_list=df['href'].tolist()
#print(df['href'][0])
#print(len(news_list))


    ## pattern file
df = pd.read_excel('company_keyword.xlsx', sheetname='Sheet1')
#print(df.head())
#print(df['company'].count())
#
#describe=df.describe()
#print(describe.company)

    ## create dataframe filtered news

f_news = pd.DataFrame()
helper = defaultdict(list)
print(helper)
      
for index, row in df.iterrows():
    df2 = pd.DataFrame({row.company:[]})
    f_news = f_news.append(df2)
    helper[row.company].append([])
#print(helper)
    
#f_news = pd.DataFrame()

    ## apply search
href_set = set()
ll=[]
count=0
for news in news_list:
    n = news
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
                #print(k+"---"+news)
                count+=1
                #helper[row.company].append(href_list[news_list.index(n)])
                #href_set.add(href_list[news_list.index(n)])
                ll.append(href_list[news_list.index(n)])
                
                #hr.append(href_list[news_list.index(n)])
                
#print(helper)
#print(count)           
#print(len(news_list))    
#print(f_news.head())

#for index, row in df.iterrows():
#    f_news[row.company] = pd.Series(helper[row.company])
#print(f_news.head())

#series = pd.Series(news)
#f_news[k]=series
#print(len(ll))
#a = array(ll)
#a = a.transpose()
#l = a.tolist()
#labels =['href']
##links = pd.DataFrame.from_items(href_list, columns=labels)

#links.to_csv('filtered_news.csv', sep=',', encoding='utf-8')
#f_news.to_csv('filtered_news.csv', sep=',', encoding='utf-8')

with open('filteredagain.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(ll)

