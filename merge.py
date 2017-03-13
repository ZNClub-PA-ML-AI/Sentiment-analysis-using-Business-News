# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 11:27:40 2017

@author: ZNevzz
"""

import pandas as pd
import codecs

#read file

import re
import pandas as pd
from collections import defaultdict
from numpy import array
import csv


filenames=['data_o1.csv','data_o2.csv']

df1=pd.read_csv(filenames[0])
df2=pd.read_csv(filenames[1])
#print(df2.head(1))
#
#result = pd.concat([df1, df2], axis=1, join_axes=[df1.index])
#print(result.describe())
#result.to_csv('data_joined_1.csv', sep=',', encoding='utf-8')

# create sets of ids

id_df1=set(df1['id'].tolist())
print(len(id_df1))

id_df2=set(df2['id'].tolist())
print(len(id_df2))

ids=id_df1.intersection(id_df2)
print(len(ids))

