# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.piple

## Reading data
# %%
df = pd.read_csv('wdbc.data',header=None)
df.head()

## label encoding first

# %%
le = preprocessing.LabelEncoder()
X = df.iloc[:,2:].values
y = df.iloc[:,1].values
y=le.fit_transform(y)
le.classes_
# split the data test train_test_split
X_train,y_train,X_test,y_test = train_test_split(X,y,test_size=0.20,random_state=1)
