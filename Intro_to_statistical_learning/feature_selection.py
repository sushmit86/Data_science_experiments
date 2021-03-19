from itertools import combinations
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
import statsmodels.api as sm
import multiprocessing as mp
class feature_selection():
    '''
    X: Training data type: Pandas DataFrame
    y: Target Variable: Pandas Dataframe or Series
    '''
    def __init__(self,X,y):
        '''
        X: Training data type: Pandas DataFrame
        y: Target Variable: Pandas Dataframe or Series
        '''
        self.X = X
        self.y = y
        self.features = list(X.columns)
        self.best_subset_result_dict = {}
        self.forward_stepwise_result_dict = {}
    def best_subset_selection(self,num_features= 10):
        '''
        num_features : Number of features to iterate on pow(2,p) iteration will be executed
        '''
        
        self.best_subset_result_dict.clear() ## clear the 
        for i in (range(num_features+1)):
            if i == 0:
                y_mean = self.y.mean()
                mse = mean_squared_error(self.y.values,len(self.y) * [y_mean])
                self.best_subset_result_dict[i] = {'feature' :(), 'mse' :mse,'r2':0}
            else:
                temp_dict_mse = {}
                temp_dict_r2 = {}
                for _feature in combinations(self.features,i):
                    _y = self.y
                    _X = self.X.loc[:,_feature]
                    _X = sm.add_constant(_X)
                    _model = sm.OLS(_y,_X)
                    _results = _model.fit()
                    temp_dict_mse[_feature] = _results.mse_model
                    temp_dict_r2[_feature] = _results.rsquared
                best_feature = max(temp_dict_r2,key=temp_dict_r2.get)
                self.best_subset_result_dict[i] = {'feature' :best_feature, 'mse' :temp_dict_mse[best_feature],'r2':temp_dict_r2[best_feature]}
            if i%5 == 0:
                print(f'Done for {i} features')
        return self.best_subset_result_dict
    
    def forward_stepwise_selection(self, num_features = 10):
        '''
        num_features : Number of features to iterate. There will be 1 + p*(p+1)/2 features
        '''
        self.forward_stepwise_result_dict.clear()
        for i in (range(num_features+1)):
            if i == 0:
                y_mean = self.y.mean()
                mse = mean_squared_error(self.y.values,len(self.y) * [y_mean])
                self.forward_stepwise_result_dict[i] = {'feature' :(), 'mse' :mse,'r2':0}
            else :
                temp_dict_mse = {}
                temp_dict_r2 = {}  
                for _feature in self.features:
                    _new_feature = list(self.forward_stepwise_result_dict[i-1]['feature'])
                    _new_feature.append(_feature)
                    _new_feature = tuple(_new_feature)
                    _y = self.y
                    _X = self.X.loc[:,_new_feature]
                    _X = sm.add_constant(_X)
                    _model = sm.OLS(_y,_X)
                    _results = _model.fit()
                    temp_dict_mse[_new_feature] = _results.mse_model
                    temp_dict_r2[_new_feature] = _results.rsquared
                best_feature = max(temp_dict_r2,key=temp_dict_r2.get)
                self.forward_stepwise_result_dict[i] = {'feature' :tuple(best_feature), 'mse' :temp_dict_mse[best_feature],'r2':temp_dict_r2[best_feature]}
        return self.forward_stepwise_result_dict

    def select_best_model(self, model_type = 'best_subset'):
        '''
        adding AIC,BIC and adjusted_r2
        model_type = Type of model valid values 'best_subset','forward_stepwise' or 'backward_stepwise'
        '''
        if model_type == 'best_subset':
            result_dict = self.best_subset_result_dict
        elif model_type == 'forward_stepwise':
            result_dict = self.forward_stepwise_result_dict
        
        for p in result_dict.keys():
            if p == 0:
                result_dict[p]['aic'] = 0
                result_dict[p]['bic'] = 0
                result_dict[p]['adjusted_r2'] = 0
            else:  
                _feature = result_dict[p]['feature']
                _y = self.y
                _X = self.X.loc[:,_feature]
                _X = sm.add_constant(_X)
                _model = sm.OLS(_y,_X)
                _results = _model.fit()
                result_dict[p]['aic'] = _results.aic
                result_dict[p]['bic'] = _results.bic
                result_dict[p]['adjusted_r2'] = _results.rsquared_adj
                result_dict[p]['params'] = _results.params
        return result_dict

            
            
    