from sklearn.base import BaseEstimator,TransformerMixin, ClusterMixin ,RegressorMixin
from sklearn.externals import joblib
import numpy as np
import os
cur_dir = os.path.dirname(__file__)
regressor=joblib.load(os.path.join(cur_dir,'pkl_objects','ranf.pkl'))
class CreateResiduals(BaseEstimator, TransformerMixin):
    def __init__(self,param=True): # no *args or **kargs
        self.param = param
    def fit(self, X, y=None):
        return self # nothing else to do
    def transform(self, X, y=None):
        exog=X[:,:-1]
        endog=X[:,-1].reshape(-1,1)
        endog_pred=regressor.predict(exog).reshape(-1,1)
        resid=endog - endog_pred
        return np.c_[resid]