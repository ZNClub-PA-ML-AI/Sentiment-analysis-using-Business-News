# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 11:27:40 2017

@author: ZNevzz
"""

import pandas as pd

#read file

filenames=['data_o1.csv','data_o3.csv']

df1=pd.read_csv(filenames[0])
df2=pd.read_csv(filenames[1])
#print(df2.head(1))
#
#result = pd.concat([df1, df2], axis=1, join_axes=[df1.index])
#print(result.describe())
#result.to_csv('data_joined_1.csv', sep=',', encoding='utf-8')

# create sets of ids

id_df1=set(df1['id'].tolist())
#print(len(id_df1))

id_df2=set(df2['id'].tolist())
#print(len(id_df2))

ids=id_df1.intersection(id_df2)
#print(len(ids))

not_present=id_df1-id_df2
#print(len(not_present))

df3=pd.DataFrame()

for i1,r1 in df1.iterrows():
    if r1.id not in not_present:
        temp=pd.DataFrame({'id':[r1.id],'date':[r1.date],'title':[r1.title],'intro':[r1.intro]})
        df3=pd.concat([df3,temp])
    
#print(df3.describe())
result=pd.DataFrame()
c=0

# sort both dataframes

df1 = df3.sort_values(['id'],ascending=[1])
df1.set_index('id') 
#print(df1.head(3))

df2 = df2.sort_values(['id'],ascending=[1])
df2.set_index('id')
#print(df2.head(3))
#for i1,r1 in df1.iterrows():
#    for i2,r2 in df2.iterrows():
#        id1 = r1.id
#        id2 = r2.id
#        if id1!=id2:
#            pass
#            #c=c+1
#            #match=pd.DataFrame({'id':[r1.id],'data':[r1.data],'title':[r1.title],'intro':[r1.intro],'body':[r2.body]})
#            #result = pd.concat([result,match])
#
##print(result.describe())
#print("cool",c)



result = pd.concat([df1, df2], axis=0,join='inner')
result.to_csv('data_joined_2.csv', sep=',', encoding='utf-8')



