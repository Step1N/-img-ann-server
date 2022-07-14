import json
from .img_ann_exception import *


class ImgAnnResponse(object):
    def __init__(self, status_code, status='UNKNOWN'):
        self.status = status
        self.status_code = status_code

    def get_json(self):
        return json.dumps(self.__dict__, default=lambda o: o)

    def get_dict(self):
        return json.loads(json.dumps(self.__dict__, default=lambda o: o))


class SuccessResponse(ImgAnnResponse):
    def __init__(self, payload, status_code=200):
        ImgAnnResponse.__init__(self, status_code, status='SUCCESS')
        self.payload = payload

    def __setattr__(self, key, value):
        if key is 'status_code' and not (200 <= value < 300):
            raise ImgAnnServiceException('Status code for success cant be {}'.format(value))
        ImgAnnResponse.__setattr__(self, key, value)


class FailureResponse(ImgAnnResponse):
    def __init__(self, status_code=1000, message='unknown error occurred'):
        ImgAnnResponse.__init__(self, status_code, status='FAILURE')
        self.message = message
        self.errors = {"info": message}

    def __setattr__(self, key, value):
        if key is 'status_code' and 200 <= value < 300:
            raise ImgAnnServiceException('Status code for failure cant be {}'.format(value))
        ImgAnnResponse.__setattr__(self, key, value)
