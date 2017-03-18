"""
Created on Mon Mar 18 11:27:40 2017
@author: ZNevzz
"""
from bs4 import BeautifulSoup
import pandas as pd

#read file
filenames=['data_o2.csv']

html='<p xmlns:fn=""http://www.w3.org/2005/xpath-functions"" id=""U10478744187zRC"" style="" letter-spacing: -7; ;"">The December quarter result of auto component'

print(BeautifulSoup.(html).get_text())
