'''
@author Vinayak
@email vnayak@okkular.io / nayakvinayak95@gmail.com
@create date 2021-10-28 17:15:10
@modify date 2021-10-29 09:09:26
@desc The base estimator class for all vision applications
'''

from fastai.vision.all import *
from typing import Dict, List, Set
class base_estimator(object):

    @staticmethod
    def get_dls_from_df():
        pass

    @staticmethod
    def get_item_tfms():
        pass

    @staticmethod
    def get_model():
        pass

    @staticmethod
    def get_cbs():
        pass

    @staticmethod
    def get_loss_func():
        pass

    @staticmethod
    def get_learner():
        pass

    @staticmethod
    def predict():
        pass
    
    @staticmethod
    def upload_logs():
        pass

