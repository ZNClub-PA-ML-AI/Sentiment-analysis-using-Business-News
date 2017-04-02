
import numpy as np
import pandas as pd
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression


df=pd.read_csv('../../TCS_qs.csv')
#print(df.shape)
df['shift_close']=df['Close'].shift(-1)
df['PC_open']=df['Open']-df['shift_close']
df['PC_close']=df['Open']-df['Close']

df.dropna(inplace=True)

## avg for fillna
list_close=df['Close']
list_open=df['Open']
#print(df[['PC_open','PC_close']])

df2=df[['PC_open']]
print(df2.describe())

mean=df2.describe().mean()
std=df2.describe().std()

neg_th=float(-std)
pos_th=float(std)

df3=pd.DataFrame()
for i,r in df.iterrows():
    
    pc=float(r['PC_open'])    
    if pc<=neg_th or pc>=pos_th:
        temp=pd.DataFrame({'PC':[r['PC_open']],'score':[r['open_score']]})
        df3=pd.concat([df3,temp])

print(df3.corr())



#avg_close=sum(list_close)/len(list_close)
#avg_open=sum(list_open)/len(list_open)
#avg=sum([avg_close,avg_open])/2
#df.fillna(avg,inplace=True)




#X=np.array(df[['close_score','open_score','PC_close']])
#Y=np.array(df[['Open']])
X=np.array(df3[['score']])
Y=np.array(df3[['PC']])

con=[]
for i in range(10):
    x_train,x_test, y_train, y_test = cross_validation.train_test_split(X, Y, test_size=0.25)
    #print(len(x_train),len(x_test),len(y_train),len(y_test))
    
    clf= LinearRegression(n_jobs=-1)
    clf.fit(x_train, y_train)
    confidence = clf.score(x_test, y_test)
    print('Linear Confidence Score: %f'%(confidence*100))
    con.append(confidence*100)

print("Avg confidence:",np.array(con).mean())
#df['PC_open']=df['PC_open'] if (df['PC_open']>30.0)


#df1=df.corr()
#print(df1[['PC_open','open_score','PC_close','close_score']])
#df2=df.cov()
#print(df2[['PC_open','open_score','PC_close','close_score']])


#ser=df.values.std(ddof=1) 
#print(ser)
#print(df[['PC_open']])
#df.to_csv('../../REL_qs_pc.csv',encoding='utf-8',sep=',')



'''
X=np.array(df[['close_score']])
Y=np.array(df[['PC_close']])

x_train,x_test, y_train, y_test = cross_validation.train_test_split(X, Y, test_size=0.2)
print(len(x_train),len(x_test),len(y_train),len(y_test))

clf= LinearRegression(n_jobs=-1)
clf.fit(x_train, y_train)
confidence = clf.score(x_test, y_test)
print('Linear Confidence Score: %f'%(confidence*100))
'''

