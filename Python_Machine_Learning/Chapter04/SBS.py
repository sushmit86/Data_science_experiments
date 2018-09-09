
from sklearn.base import clone
from sklearn.metrics import accuracy_score
from  itertools import combinations

class SBS():
    def __init__(self, estimator, k_features, scoring=accuracy_score, test_size=0.25,
                 random_state=1):
        self.estimator = estimator
        self.k_features = k_features
        self.scoring = scoring
        self.test_size = test_size
        self.random_state = random_state
def fit(X,y):
    """
    X: Input Dataframe
    y: Input y
    """
    return None

