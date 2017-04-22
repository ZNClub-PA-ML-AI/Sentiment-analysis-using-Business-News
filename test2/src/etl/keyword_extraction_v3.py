"""
Created on Wed Mar 22 11:41:40 2017

@author: ZNevzz
"""

import sys
import platform
import pandas as pd
from collections import defaultdict
import re

if platform.system()=='Windows':
    company_id='AX'
else:
    company_id=sys.argv[1]

# read file
filenames=['../../labeled.csv','../../../data/explicit/company_keyword.xlsx']

df =pd.read_csv(filenames[0])
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

#hardcode database for demo


if company_id=='REL':
    company[company_id]='Reliance Industries,Mukesh Ambani,Anil Ambani,Reliance Commercial Corporation,RELIANCE,RIL,Jio'
    competitor[company_id]='BPCL,GAIL,NTPC,ONGC,PG,TP,Airtel,Vodafone,Idea,BSNL'
    sector[company_id]='Telecom,Telecommunication,Department of Telecommunications,mopng,Ministry of Petroleum and Natural Gas,mop&ng,natural gas,petroleum,energy sector,powermin,Ministry of Energy sources,Ministry of New and Renewable'    

elif company_id=='TCS':
    company[company_id]='Tata Consultancy Services,TCS,Natarajan Chandrasekaran,Ratan Tata,Tata Group,JRD Tata,J.R.D. Tata,F.C. Kohli,FC Kohli'
    competitor[company_id]='Infosys,HCL,TechMahindra,Wipro,Accenture,Cognizant,HP,Genpact,IBM'
    sector[company_id]='information technology,IT industry'
elif company_id=='AX':
    company[company_id]='AXIS bank,AXISBANK,Shikha Sharma,Sanjiv Misra'
    competitor[company_id]='BOB,HDFC,HDFCB,ICICI,ININ,KMB,SBI,YB'
    sector[company_id]='banking,finance,financial services,Reserve Bank of India,RBI,R.B.I.,banking system,banking structure,finmin,Ministry of Finance, Department of Financial Services'
    





result = pd.DataFrame()

for i,r in df.iterrows():
    t=str(r.title).lower()
    i=str(r.intro).lower()
    b=str(r.body).lower()
    
    
    cmpy_list,cmpt_list,sect_list=company[company_id].split(','),competitor[company_id].split(','),sector[company_id].split(',')
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
            score=float(r.score)
            break
    # competitor
    keywords=cmpt_list
    for k in keywords:
        pattern=k.lower()
        if re.search(pattern,i) or re.search(pattern,t) or re.search(pattern,b):
            tag='competitor'
            match=True
            score=0.0-float(r.score)
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
            # check in title
            if re.search(pattern,t) or re.search(pattern,i) and k in cmpy_set:
                score=float(r.score)
            elif re.search(pattern,t) or re.search(pattern,i) and k in cmpt_set:
                score=0.0-float(r.score)
            break            
    if match:
        temp=pd.DataFrame({'date':[r.date],'id':[r.id],'time':[r.time],'title':[r.title],'intro':[r.intro],'body':[r.body],'score':score,'tag':tag})
        result=pd.concat([result,temp])


        
result = result.set_index(['score'])
print(result.describe())
result.to_csv('../../'+company_id+'.csv',encoding='utf-8',sep=',')


