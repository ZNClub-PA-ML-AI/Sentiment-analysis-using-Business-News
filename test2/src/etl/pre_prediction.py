"""
Created on Thu Mar 23 20:58:21

@author: ZNevzz
"""
import datetime
import pandas as pd
import collections
import re
import platform
import sys


if platform.system()=='Windows':
    company_id,filter='AX','open'
else:
    company_id,filter=sys.argv[1],sys.argv[2]

filenames=['../../'+company_id+'.csv']

df=pd.read_csv(filenames[0])
date_list = df.date.tolist()
dates=set(date_list)
#print(len(dates))

result=pd.DataFrame()
cnt = collections.Counter(date_list)
#print(len(cnt))

od = collections.OrderedDict(sorted(cnt.items()))

score=dict()
for k,v in od.items():
    print(k,v)
    score[k]=0

## competitor def
def is_competitor(title,intro,body,company):
    
    df1 = pd.read_excel('../../../data/explicit/company_keyword.xlsx','Sheet1')
    df2 = pd.read_excel('../../../data/explicit/company_keyword.xlsx','Sheet2')
    competitors=list()
    competitor=collections.defaultdict(list)

    for i,r in df2.iterrows():
        if str(r.company)==company:
            competitors=str(r.competitors).split(',')
            break
    
    for i,r in df1.iterrows():
        if str(r.company) in competitors:
            competitor[str(r.company)]=str(r.keyword).split(',')
    
    t=title.lower()
    i=intro.lower()
    b=body.lower()
    
    for company in competitors:
        for keyword in competitor[company]:
            pattern=keyword.lower()
            if re.search(pattern,i) or re.search(pattern,t) or re.search(pattern,b):
                return False
    
    return True

next_date=[]
for i,r in df.iterrows():
    
    date=str(r.date)
    time=datetime.datetime.strptime(str(r.time),'%H:%M')
    time_open=datetime.datetime.strptime('09:00','%H:%M')
    time_close=datetime.datetime.strptime('16:00','%H:%M')
    sc=float(r.score)
    
    # before markets open
    if time<=time_open and filter=='open':
         
         if len(next_date)>0:
            score[date]+=sum(next_date)
            score[date]+=sc
            od[date]+=len(next_date) 
            next_date=[]
         else:
             score[date]+=sc    
    #after markets close
    elif time>time_close and filter=='open':
         
         next_date.append(sc)
    #during trading hours
    elif filter=='close':
         
         score[date]+=sc
for k,v in od.items():
    score[k]=score[k]/v
    print(k,score[k])
#print(len(score))
#print(score)

df=pd.DataFrame(score,index=['score'])
df=df.transpose()
df.to_csv('../../'+company_id+'_score_'+filter+'.csv',sep=',',encoding='utf-8')
#df.to_json('TCS_score_open.json')

