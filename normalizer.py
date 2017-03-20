"""
Created on Mon Mar 19 9:21:10 2017

@author: ZNevzz
"""

import pandas as pd

# read file

filenames = ['data_joined_2.csv']
df = pd.read_csv(filenames[0])
#print(df.head(2))
#print(df.columns)

# drop last id column

df.drop(df.columns[6],axis=1,inplace=True)
#print(df.columns)

# test date extraction
date_format="Wed, Nov 09 2016. 10 38 PM"
splitter = date_format.split()
print(splitter)

month={'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}

date = splitter[3][0:-1]+'-'+month[splitter[1]]+'-'+splitter[2]
print(date)




