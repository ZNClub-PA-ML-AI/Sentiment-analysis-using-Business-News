"""
Created on Mon Mar 19 9:21:10 2017

@author: ZNevzz
"""

import pandas as pd

filenames = ['data_joined_2.csv']
df = pd.read_csv(filenames[0])
print(df.head(2))

