'''
Exploring data
'''

import numpy as np
import pandas as pd
#import visuals as vs
from IPython.display import display


#load the data
in_file = 'titanic_data.csv'
full_data = pd.read_csv(in_file)

print(full_data)

#Store survived feature in variable
outcomes = full_data['Survived']
data = full_data.drop('Survived', axis = 1)
