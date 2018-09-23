import numpy as np
### it is assumed that both fit_transform and transform are being passed standard values
class PCA():
    def __init__(self,n_components =2):
        self.n_components = n_components
        return None
    def fit_transform(self, X):
        eigen_values,eigen_vector = np.linalg.eigh(np.cov(X.T))
        eigen_values[::-1].sort()
        eigen_vector = np.fliplr(eigen_vector)
        self.W_transform = eigen_vector[:, 0: self.n_components]
        self.lamda_values = eigen_values
        self.explaned_varaince_ratio = np.cumsum(
            self.lamda_values/self.lamda_values.sum())
        return X.dot(self.W_transform)
    def transform(self,X):
        return X.dot(self.W_transform)
