
import numpy as np
import pandas as pd
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression


df=pd.read_csv('../../REL_qs.csv')

df['shift_close']=df['Close'].shift(-1)
df['PC_open']=df['Open']-df['shift_close']
df['PC_close']=df['Open']-df['Close']

#df.dropna(inplace=True)

## avg for fillna
list_close=df['Close']
list_open=df['Open']

avg_close=sum(list_close)/len(list_close)
avg_open=sum(list_open)/len(list_open)
df.fillna(avg_open,inplace=True)

print(df.head(10))

# open price 
X=np.array(df[['open_score']])
Y=np.array(df[['PC_open']])

x_train,x_test, y_train, y_test = cross_validation.train_test_split(X, Y, test_size=0.2)
#print(len(x_train),len(x_test),len(y_train),len(y_test))

clf= LinearRegression(n_jobs=-1)
clf.fit(x_train, y_train)
confidence = clf.score(x_test, y_test)
#print('Linear Confidence Score: %f'%(confidence*100))

#df['PC_open']=df['PC_open'] if (df['PC_open']>30.0)


df1=df.corr()
print("PC open vs sentiment=\n",df1[['PC_open','open_score']])
print("PC close vs sentiment=\n",df1[['PC_close','close_score']])


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

