# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 11:27:40 2017

@author: ZNevzz
"""

import pandas as pd
import copy

#read file
sys_path='../../../data/processed/'
filenames=['data_o1.csv','data_o3.csv']

df1=pd.read_csv(sys_path+filenames[0])
df2=pd.read_csv(sys_path+filenames[1])
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
# copy of ids for 2nd for loop
cp_ids = copy.deepcopy(ids)

not_present=id_df1-id_df2
#print(len(not_present))

# create new df1 with unique rows
df3=pd.DataFrame()
c=0
for i1,r1 in df1.iterrows():
    if r1.id in ids:
        temp=pd.DataFrame({'id':[r1.id],'date':[r1.date],'title':[r1.title],'intro':[r1.intro]})
        df3=pd.concat([df3,temp])
        c=c+1
        ids.remove(r1.id)

print("df3",df3.columns)

df1 = df3.sort_values(['id'],ascending=[1])
df1.set_index('id') 

#print(df1.head(3))

# create new df2 with unique rows
print(len(cp_ids))
df4=pd.DataFrame()
for i2,r2 in df2.iterrows():
    
    if r2.id in cp_ids:
        
        temp=pd.DataFrame({'id':[r2.id],'body':[r2.body]})
        df4=pd.concat([df4,temp])
        cp_ids.remove(r2.id)

#print(df3.describe())
#print(df4.describe())

#print(c,len(ids))

# sort both dataframes

print("df4",df4.columns)
df2 = df4.sort_values(['id'],ascending=[1])
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

result=pd.DataFrame()
print(len(df1['id'].tolist()),len(df2['id'].tolist()))
result = pd.concat([df1, df2], axis=1,join='inner') 
result.to_csv(sys_path+'data_merged.csv', sep=',', encoding='utf-8')



