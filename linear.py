import quandl
import numpy as np
import pandas as pd
from sklearn import preprocessing, cross_validation
from sklearn.linear_model import LinearRegression

df = quandl.get("NSE/INFY", authtoken="-zLmnBx6NmesMSEA_2MU")

print(df.describe())


