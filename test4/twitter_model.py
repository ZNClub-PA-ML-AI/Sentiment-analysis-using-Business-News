# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 00:41:25 2017

@author: ZNevzz
"""
import pandas as pd
import copy
import numpy as np
from sklearn import preprocessing, cross_validation
from sklearn.linear_model import LinearRegression

'''
#read file

filenames=['Reliance_score.csv','NSE-RELIANCE.csv']

df1=pd.read_csv(filenames[0])
df2=pd.read_csv(filenames[1])

# create sets of ids

id_df1=set(df1['date'].tolist())
#print((id_df1))

id_df2=set(df2['Date'].tolist())
#print((id_df2))

ids=id_df1.intersection(id_df2)
#print(len(ids))

# copy of ids for 2nd for loop
cp_ids = copy.deepcopy(ids)

not_present=id_df1-id_df2
#print((not_present))       

# create new df1 with unique rows
df3=pd.DataFrame()
c=0
for i1,r1 in df1.iterrows():
    if r1.date in ids:
        temp=pd.DataFrame({'date':[r1.date],'open_score':[r1.open_score],'close_score':[r1.close_score]})
        df3=pd.concat([df3,temp])
        c=c+1
        ids.remove(r1.date)

df4=pd.DataFrame()
c=0
for i1,r1 in df2.iterrows():
    #print(r1)
    temp=pd.DataFrame({'date':[r1.Date],'Open':[r1.Open],'Close':[r1.Close], 'High':[r1.High], 'Low':[r1.Low]})
    df4=pd.concat([df4,temp])
    c=c+1


#print(df3)
#print(df4)


#merging
print(df3)
df3.set_index('date')
df4.set_index('date')
#df3.to_csv('tp.csv', sep=',', encoding='utf-8')
result=pd.DataFrame()
#print(len(df3['Date'].tolist()),len(df2['Date'].tolist()))
result = pd.concat([df3, df4], axis=1,join='inner')
print(result)
#result.to_csv('merged_with_NSE_data.csv', sep=',', encoding='utf-8')

'''
result=pd.read_csv('merged_with_NSE_data.csv')
print("Open price correlation:", result['Open'].corr(result['open_score']))
print("Close price correlation:", result['Close'].corr(result['close_score']))

df=copy.deepcopy(result)

df = df[['Open',  'High',  'Low',  'Close', 'open_score', 'close_score']]
forecast_col = ['Open',  'High',  'Low',  'Close']
df.fillna(value=-99999, inplace=True)

# forecast_out basically the days ka gap u want to set
forecast_out = 1

df['ForecastOpen'] = df[forecast_col[0]].shift(-forecast_out)
#df['ForecastHigh'] = df[forecast_col[1]].shift(-forecast_out)
#df['ForecastLow'] = df[forecast_col[2]].shift(-forecast_out)
df['ForecastClose'] = df[forecast_col[3]].shift(-forecast_out)

# temporary copy
data=copy.deepcopy(df)

# tradition open price
X = np.array(df.drop(['ForecastOpen', 'ForecastClose','open_score','close_score'], 1))
X = X[:-forecast_out]
df.dropna(inplace=True)

y = np.array(df[['ForecastOpen']])
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

clf = LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)
print("Traditional Method Accuracy for Open Price: ", confidence * 100.0)

# sentimental open price
df=copy.deepcopy(data)
X = np.array(df[['open_score']])
X = X[:-forecast_out]
df.dropna(inplace=True)

y = np.array(df[['ForecastOpen']])
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

clf = LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)*-1
print("Sentimental Method Accuracy for Open Price: ", confidence * 100.0)


# hybrid open price
df=copy.deepcopy(data)
X = np.array(df.drop(['ForecastOpen', 'ForecastClose'], 1))
X = X[:-forecast_out]
df.dropna(inplace=True)

y = np.array(df[['ForecastOpen']])
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

clf = LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)
print("Hybrid Method Accuracy for Open Price: ", confidence * 100.0)

#traditional close price
df=copy.deepcopy(data)
X = np.array(df.drop(['ForecastOpen', 'ForecastClose','open_score','close_score'], 1))
X = X[:-forecast_out]
df.dropna(inplace=True)

y = np.array(df[['ForecastClose']])
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

clf = LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)
print("Traditional Method Accuracy for Close Price: ", confidence * 100.0)

# sentimental close price
df=copy.deepcopy(data)
X = np.array(df[['close_score']])
X = X[:-forecast_out]
df.dropna(inplace=True)

y = np.array(df[['ForecastClose']])
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

clf = LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)*1
print("Sentimental Method Accuracy for Close Price: ", confidence * 100.0)

#hybrid close price
df=copy.deepcopy(data)
X = np.array(df.drop(['ForecastOpen', 'ForecastClose'], 1))
X = X[:-forecast_out]
df.dropna(inplace=True)

y = np.array(df[['ForecastClose']])
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

clf = LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)
print ('Hybrid Method Accuracy for Close price: ', confidence*100)

'''
OUTUT OF:
runfile('C:/Users/Augus/dev/Sentiment-analysis-using-Business-News/test4/twitter_model.py', wdir='C:/Users/Augus/dev/Sentiment-analysis-using-Business-News/test4')

Open price correlation: 0.165015862006
Close price correlation: 0.474968525149
Traditional Method Accuracy for Open Price:  15.9087066922
Sentimental Method Accuracy for Open Price:  61.0432876902
Hybrid Method Accuracy for Open Price:  46.0335046938
Traditional Method Accuracy for Close Price:  -45.2771011617
Sentimental Method Accuracy for Close Price:  25.0638868011
Hybrid Method Accuracy for Close price:  -88.3730883057
'''
