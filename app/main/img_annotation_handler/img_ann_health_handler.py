from flask_restplus import Resource

from ..img_annotation_name_space.img_ann_test_ns import *
from ..img_annotation_logger.img_ann_logger import *
from ..img_annotation_exception.json_response import *

logger = get_app_logger()
api = ImgAnnTestNS.api


@api.route('/health')
class ImgAnnTestApi(Resource):

    @api.doc('to see service status')
    def get(self):
        return get_success_response("I'm well and alive")
