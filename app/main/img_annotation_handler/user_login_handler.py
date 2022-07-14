from flask_restplus import Resource
from flask import request
from ..img_annotation_name_space.user_cred_ns import *
from ..img_annotation_logger.img_ann_logger import *
from ..img_annotation_exception.json_response import *

logger = get_app_logger()
api = UserCred.api
user_info = UserCred.user_info


@api.route('/token')
class UserLoginHandler(Resource):

    @api.doc('To upload image files')
    @api.expect(user_info)
    def post(self):
        cred = request.json
        if len(cred) == 0:
            return get_failure_response("error in request payload")

        logger.info("UserLoginHandler: found user info %d", len(cred))
        logger.info("UserLoginHandler: validating user info %s", cred['username'])
        return get_success_response({"token":"test123"})
