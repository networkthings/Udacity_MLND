# Import libraries necessary for this project
import sys
sys.path.append("/usr/local/lib/python2.7/site-packages")

import numpy as np
import pandas as pd
import dateutil
from sklearn.cross_validation import ShuffleSplit

# # Import supplementary visualizations code visuals.py
# import visuals as vs

# # Pretty display for notebooks
# # %matplotlib inline

# # Load the Boston housing dataset
data = pd.read_csv('housing.csv')
prices = data['MEDV']
features = data.drop('MEDV', axis = 1)
    
# # Success
# print data.shape
print "Boston housing dataset has %s data points with %s variables each." %(data.shape[0], data.shape[1])