
''' 
IMPORTANT
Hey v are not exactly predicting the stock price of the next day.
But this approach can work because the v can think of row's in csv
as events, as 1st row happens before 2nd row and so on.....
This makes sense???


So basically if v get stock price and sentiment of a particular day
V can predict the "next stock price" 
(here the "next stock price" need not mean stock price of next day.
it means the next possible stock price -> maybe next day, next two days, ans so on..)

So u think upon this and see if it logicaly right.
U think about it and tell me 'I CAN BE WRONG WIHT THIS APPROACH'
so tell me if im wrong :) 
'''

import numpy as np
from sklearn import preprocessing, cross_validation
from sklearn.linear_model import LinearRegression
import pandas as pd

df=pd.read_csv('REL_qs.csv')
df = df[['Open',  'High',  'Low',  'Close', 'open_score', 'close_score']]
forecast_col = ['Open',  'High',  'Low',  'Close']
df.fillna(value=-99999, inplace=True)

print ('DF head')
print (df.head(10))
print ('DF tail')
print (df.tail(10))
# forecast_out basically the days ka gap u want to set
forecast_out = 1

df['ForecastOpen'] = df[forecast_col[0]].shift(-forecast_out)
#df['ForecastHigh'] = df[forecast_col[1]].shift(-forecast_out)
#df['ForecastLow'] = df[forecast_col[2]].shift(-forecast_out)
df['ForecastClose'] = df[forecast_col[3]].shift(-forecast_out)


# tradition open price

X = np.array(df.drop(['ForecastOpen', 'ForecastClose','open_score','close_score'], 1)) #, 'ForecastHigh', 'ForecastLow', 'ForecastClose'], 1))
#print(X[0], X.shape)
X = X[:-forecast_out]
#print(X[0], X.shape)
df.dropna(inplace=True)

y = np.array(df[['ForecastOpen']]) #, 'ForecastHigh', 'ForecastLow', 'ForecastClose']])
#print (y[0])
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)
#print("y: ", y[len(y) - 1])
#print("X_test: ", X_test[len(X_test) - 1])

clf = LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)
print("Traditional Method Accuracy for Open Price: ", confidence * 100.0)

# hybrid open pricec

X = np.array(df.drop(['ForecastOpen', 'ForecastClose'], 1)) #, 'ForecastHigh', 'ForecastLow', 'ForecastClose'], 1))
print(X[0], X.shape)
X = X[:-forecast_out]
#print(X[0], X.shape)
df.dropna(inplace=True)

y = np.array(df[['ForecastOpen']]) #, 'ForecastHigh', 'ForecastLow', 'ForecastClose']])
#print (y[0])
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)
#print("y: ", y[len(y) - 1])
#print("X_test: ", X_test[len(X_test) - 1])

clf = LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)
print("Hybrid Method Accuracy for Open Price: ", confidence * 100.0)

#traditional close price

X = np.array(df.drop(['ForecastOpen', 'ForecastClose','open_score','close_score'], 1)) #, 'ForecastHigh', 'ForecastLow', 'ForecastClose'], 1))
#print(X[0], X.shape)
X = X[:-forecast_out]
#print(X[0], X.shape)
df.dropna(inplace=True)

y = np.array(df[['ForecastClose']]) #, 'ForecastHigh', 'ForecastLow', 'ForecastClose']])
#print (y[0])
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)
#print("y: ", y[len(y) - 1])
#print("X_test: ", X_test[len(X_test) - 1])

clf = LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)
print("Traditional Method Accuracy for Close Price: ", confidence * 100.0)

#hybrid close price

X = np.array(df.drop(['ForecastOpen', 'ForecastClose'], 1)) #, 'ForecastHigh', 'ForecastLow', 'ForecastClose'], 1))
#print(X[0], X.shape)
X = X[:-forecast_out]
#print(X[0], X.shape)
df.dropna(inplace=True)

y = np.array(df[['ForecastClose']])
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)
#print (X)
#print ('________________________')
#print (y)
clf = LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)
print ('Hybrid Method Accuracy for Close price: ', confidence*100)




