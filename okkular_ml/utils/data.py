'''
@author Vinayak
@email vnayak@okkular.io / nayakvinayak95@gmail.com
@create date 2021-10-28 18:01:47
@modify date 2021-10-28 18:48:02
@desc A utility file for getting/uploading data from/to AWS utilities
'''

import boto3
from typing import List
import PIL.Image, cv2

class data:

    @staticmethod
    def untar_s3_data(bucketname:str, s3uri:str, destination_path:str):
        pass

    @staticmethod
    def upload_data(bucketname:str, s3uri: str, file_path:str):
        pass

    @staticmethod
    def check_image_sanity(imgpth: str) -> List[bool, str]:
        try:
            i = PIL.Image.open(imgpth)
            assert len(i) == 3  # Assert that the image has 3 dimensions w x h x c (Should not have alpha channel else it would be 4 dimensions)
            assert i[-1] == 3   # Assert that the channel dimension is 3 i.e. RGB and not BW
            return [True, "Image is acceptable"]
        except Exception as e:
            return [False, str(e)]