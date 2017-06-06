import numpy as np
import pandas as pd
from sklearn.cross_validation import ShuffleSplit
from sklearn.metrics import make_scorer


#Load data
data = pd.read_csv('housing.csv')
prices = data['MEDV']
features = data.drop('MEDV', axis=1)

print data

print "Minimum Price ", np.min(prices)
print "Maximum Price ", np.max(prices)
print "Mean ", np.mean(prices)
print "Median ", np.median(prices)
print "Standard Deviation ", np.std(prices)

make_scorer()