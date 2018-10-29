# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from sklearn import preprocessing

## Reading data
# %%
df = pd.read_csv('wdbc.data',header=None)
df.head()

# %%
le = preprocessing.LabelEncoder()
X = df.iloc[:,2:].values
Y = df.iloc[:,1].values
le.fit_transform(Y)
