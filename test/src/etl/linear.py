"""
Created on Thu Mar 23 14:50:34 

@author: ZNevzz
"""

#import quandl
import numpy as np
import pandas as pd
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

#df = quandl.get("NSE/INFY", authtoken="-zLmnBx6NmesMSEA_2MU")
df=pd.read_csv('../../REL_qs.csv')


#print(df.head(1))
#print(df.describe())
#print(df.columns)
#print(df.date)

X=np.array(df[['open_score']])
Y=np.array(df[['Open']])

print(len(X),len(Y))
x_train,x_test, y_train, y_test = cross_validation.train_test_split(X, Y, test_size=0.25)
print(len(x_train),len(x_test),len(y_train),len(y_test))
## linear
clf= LinearRegression(n_jobs=-1)
clf.fit(x_train, y_train)
confidence = clf.score(x_test, y_test)
print('Linear Confidence Score: %f'%(confidence*100))


## svm 

df_new=pd.DataFrame()
for i,r in df.iterrows():
	label=''
	if float(r.open_score)>0.0:
		label="POSITIVE"
	elif float(r.open_score)<0.0:
		label="NEGATIVE"
  	else:
		label="NEUTRAL"
	temp=pd.DataFrame({})


clf= svm.SVC(kernel='linear',gamma=1)
clf.fit(x_train, y_train.ravel())
confidence = clf.score(x_test, y_test)
print('SVR  Confidence Score: %f'%(confidence*100))


