"""
Created on Mon Mar 19 9:21:10 2017

@author: ZNevzz
"""

import pandas as pd

# read file

filenames = ['data_joined_2.csv']
df = pd.read_csv(filenames[0])
print(df.head(2))

# drop last id column


df.drop(df.columns[5],axis=1,inplace=True)
print(df.columns)


