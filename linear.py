"""
Created on Thu Mar 23 14:50:34 

@author: ZNevzz
"""

import quandl
import numpy as np
import pandas as pd
from sklearn import preprocessing, cross_validation
from sklearn.linear_model import LinearRegression

df = quandl.get("NSE/INFY", authtoken="-zLmnBx6NmesMSEA_2MU")

#print(df.describe())
#print(df.columns)
print(df.date)


