
from sklearn.base import clone
from sklearn.metrics import accuracy_score
from collections import OrderedDict
import operator
from sklearn.model_selection import train_test_split

class SBS():
    def __init__(self, estimator, k_features, scoring=accuracy_score, test_size=0.25,
                 random_state=1):
        self.estimator = clone(estimator)
        self.k_features = k_features
        self.scoring = scoring
        self.test_size = test_size
        self.random_state = random_state
    def fit(self,X,y):
        """
        X: Input Dataframe
        y: Input y
        """
        k = X.shape[1]
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=self.test_size,random_state= self.random_state)
        self.od_set_attributes = OrderedDict()
        self.od_set_attributes[tuple(X.columns)] = self.__calc_score(X_train, X_test, y_train, y_test)
        set_attributes_current = set(X.columns)
        while (k > self.k_features):
            attribute_to_exlude = {}
            for attribute in set_attributes_current:
                temp_set = {*()} # create an empty set
                temp_set.add(attribute)
                train_temp_set = set_attributes_current - temp_set
                attribute_to_exlude[tuple(train_temp_set)] = self.__calc_score(
                    X_train.loc[:, train_temp_set], X_test.loc[:, train_temp_set], y_train, y_test)
            max_attribute=max(attribute_to_exlude.items(), key=operator.itemgetter(1))
            self.od_set_attributes[max_attribute[0]]= max_attribute[1]
            set_attributes_current= set(max_attribute[0])
            k = k -1
        return self
            


    def __calc_score(self, X_train, X_test, y_train, y_test):
        self.estimator.fit(X_train,y_train.values.ravel())
        y_pred = self.estimator.predict(X_test)
        return self.scoring(y_test,y_pred)
