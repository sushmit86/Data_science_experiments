from itertools import combinations
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
import statsmodels.api as sm
class feature_selection():
    def __init__(self,X,y):
        '''
        X: Training data type: Pandas DataFrame
        y: Target Variable: Pandas Dataframe or Series
        '''
        self.X = X
        self.y = y
        self.features = list(X.colums)
        self.result_dict = {}
    def best_subset_selection(self,num_features= 10):
        '''
        num_features : Number of features to iterate on pow(2,p) iteration will be executed
        '''
        for i in range(num_features):
            if i == 0:
                y_mean = self.y.mean()
                mse = mean_squared_error(Y.values,len(Y) * [Y.mean()])
                self.result_dict[i] = {'feature' :(), 'mse' :mse,'r2':0}
            else:
                temp_dict_ssr = {}
                temp_dict_r2 = {}
                for _feature in combinations(self.features,i):
                    _y = self.y
                    _X = self.X.loc[:,_feature]
                    _X = sm.add_constant(_X)
                    _model = sm.OLS(_y,_X)
                    _results = _model.fit()
                    temp_dict_ssr[_feature] = _results.ssr
                    temp_dict_r2[_feature] = _results.rsquared
                best_feature = min(temp_dict_ssr)
                self.result_dict[i] = {'feature' :best_feature, 'mse' :temp_dict_ssr[best_feature],'r2':temp_dict_r2[best_feature]}
        return self.result_dict 
                
                
                    
                    
                    
                    
                    
                    
                
                
        
        
        