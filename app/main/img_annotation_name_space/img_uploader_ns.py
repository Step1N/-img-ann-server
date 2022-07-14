from flask_restplus import Namespace
from werkzeug.datastructures import FileStorage


class ImgUploaderNS:
    api = Namespace('Img Uploader ', description="Image upload endpoint's ")
    upload_parser = api.parser()
    upload_parser.add_argument('ann_img', location='files', type=FileStorage, required=True)
    upload_parser.add_argument('img_name', required=True)
    upload_parser.add_argument('img_desc', required=True)
