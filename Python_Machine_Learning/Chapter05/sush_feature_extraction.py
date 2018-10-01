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
    X : Array of attributes
    Y: Output class:
    Returns
    ---------------------------------------------
    Transformation:Matrix W
    """
    def __init__(self,n_components=2):
        self.n_components = n_components
        return None

