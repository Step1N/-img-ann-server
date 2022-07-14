from flask_restplus import Api
from flask import Blueprint
from flask_cors import CORS

from .main.img_annotation_handler.img_ann_health_handler import api as test_ns
from .main.img_annotation_handler.img_handler import api as file_reader_ns
from .main.img_annotation_handler.user_login_handler import api as user_login

blueprint = Blueprint('api', __name__)

authorizations = {
    'apiKey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'api_secrete'
    }
}
api = Api(blueprint,
          title='Image Annotation Service',
          version='1.0',
          description="Image Annotation backend API's supports",
          doc='/docs',
          authorizations=authorizations,
          catch_all_404s=True
          )

cors = CORS(blueprint, supports_credentials=False)

api.add_namespace(test_ns, path='/monitor')
api.add_namespace(file_reader_ns, path='/images')
api.add_namespace(user_login, path='/user')

