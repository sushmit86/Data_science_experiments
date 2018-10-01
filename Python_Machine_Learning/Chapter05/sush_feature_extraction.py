import numpy as np
### it is assumed that both fit_transform 
# and transform are being passed standard values
# also fit transform
class PCA():
    def __init__(self,n_components =2):
        self.n_components = n_components
        return None
    def fit_transform(self, X):
        eigen_values,eigen_vector = np.linalg.eig(np.cov(X.T))
        list_eigen_pairs = []
        for _index,_value in np.ndenumerate(eigen_values):
            list_eigen_pairs.append((_value, eigen_vector[:,_index[0]]))
        list_eigen_pairs.sort(key = lambda tup: tup[0],reverse= True)
        for _index, _value in enumerate(list_eigen_pairs):
            eigen_values[_index] = _value[0]
            eigen_vector[:,_index] = _value[1]
        self.w = eigen_vector[:, 0:self.n_components]
        # self.explaned_varaince_ratio = self.lamda_values/self.lamda_values.sum()
        return X.dot(self.w)
    def transform(self,X):
        return X.dot(self.w)

class LDA():
    """
    Implementation of LDA
    ------------------------------------------
    Parameters :
    X : standardized array of attributes 
    Y: Output class correspoding to X
    Returns
    ---------------------------------------------
    Transformation:Matrix W
    """
    def __init__(self,n_components=2):
        self.n_components = n_components
        return None
    def fit_transform(self,X,y):
        #class_mean_vector = np.empty([X.shape[0],len(y.unique())])
        

        ####################### In case we need mean vector#####################
        # class_mean_vector = np.empty([X_train_std.shape[1],len(y.unique())])
        # S_W = np.zeros((X_train_std.shape[1],X_train_std.shape[1]))
        # _class_column = 0

        # for _class in y.unique():
        #     #class_mean_vector[:,_class_column] = X_train_std[(y_train==_class),:].mean(axis=0)
        #     #_class_column +=1
        #     temp_S_W=(X_train_std[(y_train==_class),:]- X_train_std[(y_train==_class),:].mean(axis=0))
        # #     print(temp_S_W.shape)
        # #     print(temp_S_W.T.shape)
        #     S_W = S_W + temp_S_W.T.dot(temp_S_W)

        # print(S_W)
        class_mean_vector = np.empty([X_train_std.shape[1], len(y.unique())])
        S_W = np.zeros((X.shape[1], X.shape[1]))
        for _class in y.unique():
            S_W = S_W + np.cov(X[(y == _class), :].T)
        return None
