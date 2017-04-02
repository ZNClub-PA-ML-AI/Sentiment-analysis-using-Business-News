

"""
Created on Wed Mar 22 11:41:40 2017

@author: ZNevzz
"""
import sys
import pandas as pd
from collections import defaultdict
import re

# read file
filenames=['../../labeled.csv','../../../data/explicit/company_keyword.xlsx']
df = pd.read_csv(filenames[0])
df1=pd.read_excel(filenames[1],sheetname='Sheet1')
df2=pd.read_excel(filenames[1],sheetname='Sheet2')

'''
#company keyword dict
company = defaultdict(list)
for i,r in df1.iterrows():
    company[str(r.company)]=str(r.keyword).split(',')


#competitor keyword dict
competitor = defaultdict(list)
for i,r in df2.iterrows():
    ids,others=str(r.competitor).split(';')
    comp_id=str(ids).split(',')
    
#id,sector=sys.argv[1],sys.argv[2]
id,sector='TCS','IT'

company[id].extend(company[sector])


print(company[id])
'''
sector,company,competitor=dict(),dict(),dict()
company_id='TCS'
company[company_id]='Tata Consultancy Services,TCS,Natarajan Chandrasekaran,Ratan Tata,Tata Group,JRD Tata,J.R.D. Tata,F.C. Kohli,FC Kohli'
competitor[company_id]='Infosys,HCL,TechMahindra,Wipro,Accenture,Cognizant,HP,Genpact,IBM'
sector[company_id]='information technology,IT industry'


result = pd.DataFrame()

for i,r in df.iterrows():
    t=str(r.title).lower()
    i=str(r.intro).lower()
    b=str(r.body).lower()
    
    
    cmpy_list,cmpt_list,sect_list=company[id].split(','),competitor[id].split(','),sector[id].split(',')
    cmpy_set,cmpt_set,sect_set=set(cmpy_list),set(cmpt_list),set(sect_list)
    tag=''
    score=0.0
    match=False
    
    # company
    keywords=cmpy_list
    for k in keywords:
        pattern=k.lower()
        if re.search(pattern,i) or re.search(pattern,t) or re.search(pattern,b):
            tag='company'
            match=True
            score+=float(r.score)
            break
    # competitor
    keywords=cmpt_list
    for k in keywords:
        pattern=k.lower()
        if re.search(pattern,i) or re.search(pattern,t) or re.search(pattern,b):
            tag='competitor'
            match=True
            score-=float(r.score)
            break    
    # sector
    keywords=sect_list
    for k in keywords:
        pattern=k.lower()
        if re.search(pattern,i) or re.search(pattern,t) or re.search(pattern,b):
            if match:
                tag='both'
            else:
                tag='general'
            score+=float(r.score)
            break            
    if match:
        temp=pd.DataFrame({'date':[r.date],'id':[r.id],'time':[r.time],'title':[r.title],'intro':[r.intro],'body':[r.body],'score':score,'tag':tag})
        result=pd.concat([result,temp])


        
result = result.set_index(['score'])
print(result.describe())
result.to_csv('../../'+id+'.csv',encoding='utf-8',sep=',')


