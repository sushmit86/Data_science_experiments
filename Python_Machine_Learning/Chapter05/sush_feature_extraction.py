import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy import exp
from scipy.linalg import eigh
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

class MOITRI_LDA():
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
        S_W = np.zeros((X.shape[1], X.shape[1]))
        S_B = np.zeros((X.shape[1], X.shape[1]))
        mean_vec = X.mean(axis=0)
        mean_vec = mean_vec.reshape(13, 1)
        for _class in np.sort(y.unique()):
            S_W = S_W + np.cov(X[(y == _class), :].T)
            temp_S_B = X[(y == _class), :].mean(axis=0).reshape(13, 1) - mean_vec
            S_B = S_B + (X[(y == _class)].shape[0])*temp_S_B.dot(temp_S_B.T)
        eigen_values, eigen_vector = np.linalg.eig(np.linalg.inv(S_W).dot(S_B))
        list_eigen_pairs = []
        for _index, _value in np.ndenumerate(eigen_values):
            list_eigen_pairs.append((_value, eigen_vector[:, _index[0]]))
        list_eigen_pairs.sort(key=lambda tup: tup[0], reverse=True)
        for _index, _value in enumerate(list_eigen_pairs):
            eigen_values[_index] = _value[0]
            eigen_vector[:, _index] = _value[1]
        self.w = eigen_vector[:, 0:self.n_components]
        self.eigen_values = np.abs(eigen_values)


    def transform(self, X):
        return X.dot(self.w)

class MOITRI_RBF_Kernel():
    """
    RBF Kernel PCA Implementation
    Parameters
    -------------
    X: {numppy, ndarray},shape
    gamma: float
    n_components : Number of components
    returns
    X_pc: {numpy, ndaaray}
    """
    def __init__(self,gamma,n_components):
        self.gamma = gamma
        self.n_components = n_components
        return None
    def fit_transform(self,X):
        ### calculate square distance:
        squared_dist = pdist(X,'sqeuclidean')
        ### convert to square form
        mat_squared_dist = squareform(squared_dist)
        K = exp(- self.gamma * mat_squared_dist)
        ndim = K.shape[0]
        I_n = np.ones((ndim,ndim))/ndim
        K_1 = K - I_n.dot(K) - K.dot(I_n) + I_n.dot(K).dot(I_n)
        # eigvals, eigvecs = eigh(K_1)
        eigvecs = eigh(K_1)[1]
        return eigvecs[:,range(-1,- self.n_components-1,-1)]
