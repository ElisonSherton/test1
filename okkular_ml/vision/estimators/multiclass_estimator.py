'''
@author Vinayak
@email vnayak@okkular.io / nayakvinayak95@gmail.com
@create date 2021-10-28 17:40:49
@modify date 2021-10-28 18:47:15
@desc Class for singlelabel i.e. multi-class classification (Only one label/op for every datapoint)
'''

from os import stat
from okkular_ml.vision.estimators.base_estimator import *


class multiclass_estimator(base_estimator):

    @staticmethod
    def get_dls_from_df():
        pass
    
    @staticmethod
    def preprocess(kps, type):
        if type == "top":
            pass
        elif type == "bottom":
            pass
        elif type == "middle":
            pass

        