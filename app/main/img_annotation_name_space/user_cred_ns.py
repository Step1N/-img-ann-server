from flask_restplus import Namespace
from flask_restplus import fields

class UserCred:
    api = Namespace('User login ', description="Validate user login ")
    user_info = api.model('User_INFO', {
        "username": fields.String(required=True),
        "password": fields.String(required=True)
    })
