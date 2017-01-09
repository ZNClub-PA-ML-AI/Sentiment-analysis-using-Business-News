# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 10:42:03 2017

@author: ZNevzz
"""

import re

#print(re.search("tara","tcs "))

news="\u200bICICI Pru makes tepid debut, stock plunges over 5% from issue price"
news = news.lower()
print(news)
tokens = ["tcs","tata consultancy services"] 


for i in tokens:
    #print(i,news)
    if re.search(i,news):
        print("found")
    else:
        print("not found")