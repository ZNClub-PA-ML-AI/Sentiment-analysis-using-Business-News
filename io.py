# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 09:25:26 2017

@author: universe
"""

import pandas as pd
df = pd.read_excel('company_keyword.xlsx', sheetname='Sheet1')
print(df.head())