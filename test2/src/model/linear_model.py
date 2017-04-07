
import numpy as np
from sklearn import preprocessing, cross_validation
from sklearn.linear_model import LinearRegression
import pandas as pd
import copy

df=pd.read_csv('../../TCS_qs.csv')
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




