# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('Solarize_Light2')
from scipy.special import comb
from scipy.stats import binom
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeigborsClassifier
from sklearn.tree
# %%
error_range = np.arange(0.0,1.01,0.01)
n_classifier = 11
np.ceil(n_classifier/2)
ens_errors=binom.sf(n_classifier - np.ceil(n_classifier/2),n_classifier,error_range)
plt.plot(error_range,ens_errors,linewidth=2,label= 'Ensemble Errors')
plt.plot(error_range,error_range,linestyle = '--',label = 'Base error')
plt.legend(loc='upper left')
plt.show()
# %%
# start writing for majority clasfier
# class MajorityVoteClassifier_sush():
#     return None
# %%
iris = datasets.load_iris()
X,y = iris.data[50:,[1,2]], iris.target[50:]
le = LabelEncoder()
y = le.fit_transform(y)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.5,random_state = 1,stratify =y)
