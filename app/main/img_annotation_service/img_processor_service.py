from ..img_annotation_storage.mongo_storage import MongoStorage
from ..img_annotation_exception.img_ann_exception import *
from ..img_annotation_util.api_request_timer import *


logger = get_app_logger()


class ImgProcessorService:

    def __init__(self):
        self.img_col = MongoStorage("image_storage")

    @request_timer
    def process_img(self, image, img_name, img_dsc):
        import datetime
        logger.info("ImgProcessorService[process_img]: processing img input")

        status = self.img_col.save_one_img(image, img_name, img_dsc)
        return status

    @request_timer
    def fetch_img(self, img_name):
        logger.info("ImgProcessorService[fetch_img]: processing img input")
        img = self.img_col.find_all_img(img_id='', img_name=img_name)
        logger.info("ImgProcessorService[fetch_img]: found image for given input %d", len(img))
        return img
