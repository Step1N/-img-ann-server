from .response_config import FailureResponse, SuccessResponse


def get_failure_response(message):
    response = FailureResponse(message=message)
    del response.status_code
    return response.get_dict()


def get_success_response(payload):
    response = SuccessResponse(payload)
    del response.status_code
    return response.get_dict()
