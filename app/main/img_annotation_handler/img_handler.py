from flask import request
from flask_restplus import Resource
from werkzeug.utils import secure_filename
from urllib.parse import urlparse, parse_qs

from ..img_annotation_util.file_helper import *
from ..img_annotation_name_space.img_uploader_ns import *
from ..img_annotation_exception.json_response import *
from ..img_annotation_service.img_processor_service import *


logger = get_app_logger()
api = ImgUploaderNS.api
_upload_parser = ImgUploaderNS.upload_parser


@api.route('', methods = ["GET", "POST"])
class ImgUploadHandler(Resource):

    @api.doc('To upload image files')
    @api.expect(_upload_parser)
    def post(self):
        """to upload images"""
        all_files = request.files.getlist("ann_img")
        logger.info("ImgUploadHandler: total files in request %d", len(all_files))
        for img_file in all_files:
            req_url = urlparse(request.url)
            query = parse_qs(req_url.query)
            if 'img_desc' not in query:
                logger.error("ImgUploadHandler: image description not found")
            img_desc = query["img_desc"][0]
            if img_file.filename == '':
                logger.error("ImgUploadHandler: did not find file name")
                logger.error("ImgUploadHandler: error while processing file")

            if img_file and FileHelper.allowed_file(img_file.filename):
                filename = secure_filename(img_file.filename)
                logger.info("ImgUploadHandler: found file with name %s", filename)
                img_process = ImgProcessorService()
                resp = img_process.process_img(img_file, img_file.filename, img_desc)
                if not resp:
                    logger.error("ImgUploadHandler: error while processing file")
            else:
                logger.info("ImgUploadHandler: Unsupported file format %s", img_file.filename)

        return get_success_response(resp)

    @api.doc('To List out all images')
    def get(self):
        """to list out all images"""
        logger.info("ImgUploadHandler: fetching all images %s", "")
        img_process = ImgProcessorService()
        resp = img_process.fetch_img(img_name="")
        if not resp:
            return get_failure_response("error while processing images request")

        return get_success_response(resp)
