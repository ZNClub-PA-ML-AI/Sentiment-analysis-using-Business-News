"""
Created on Sun Apr 23 16:43:13 2017

@author: ZNevzz
"""

import pandas as pd

def generate_id(df,df_type):
    #result=None
    result=pd.DataFrame()    
    if df_type=='body':
        for index,row in df.iterrows():
            splitter=row.href.split("/")
    #        test=splitter[4]
            rdf=pd.DataFrame({'id':splitter[4],'body':[row.body]})
            result=pd.concat([result,rdf])
    elif df_type=='data':
        for index,row in df.iterrows():
            splitter=row.href.split("/")
    #        test=splitter[4]
            rdf=pd.DataFrame({'id':splitter[4],'title':[row.title],'intro':[row.intro],'date':[row.date]})
            result=pd.concat([result,rdf])
#    print(test)        
    result.set_index('id', inplace=True)
    return result

def process(filenames,p,mode):
    p=str(p)    
    output=[]

    for i in filenames:
        df=pd.read_csv(sys_path+path_in+i,encoding='iso-8859-1')
        print(df.columns)
        output.append(generate_id(df,mode))
    
    #out=None
    out=pd.DataFrame()

    for i in output:
        out=pd.concat([out,i])
    print(out.describe())
    
    out.to_csv(sys_path+path_out+'data_o'+p+'.csv', sep=',', encoding='utf-8')
    

    
sys_path='../../../data/'
path_in='scrapy/'
path_out='processed/'


filenames_d = ['livemint_data.csv','livemint_data_2.csv','livemint_data_3.csv']
filenames_b = ['livemint_data_body.csv','livemint_data_body_2.csv','livemint_data_body_3.csv']
output=[]
mode=['data','body']
lmode=len(mode)

for m in range(lmode):
    if mode[m]=='data':
        process(filenames_d,m+1,mode[m])
    elif mode[m]=='body':
        process(filenames_b,m+1,mode[m])
    
#end

