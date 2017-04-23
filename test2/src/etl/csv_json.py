


import sys
import pandas as pd
import platform

#sentiment or NSE
if platform.system()=='Windows':
    company_id,type_id='TCS','NSE'
else:
    company_id,type_id=sys.argv[1],sys.argv[2]

path_in='../../data/'
#path_in='../../'
path_out='../../../../view/js/data/'
#path_out=path_in

filenames=[]

if type_id=='NSE':
    filenames=[path_in+type_id+'-'+company_id+'.csv']
else:
    filenames=[path_in+company_id+'_'+type_id+'.csv']

df=pd.read_csv(filenames[0])

#df = df.set_index(['date'])
if type_id=='NSE':
    df = df.sort_values(['Date'],ascending=[1])
    
print(df.head(1))
#print(filename[:-3])
if type_id=='NSE':
    df.to_json(path_out+type_id+'-'+company_id+'.json')
else:
    df.to_json(path_out+company_id+'_'+type_id+'.json')






