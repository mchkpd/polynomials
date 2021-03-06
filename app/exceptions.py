from flask import Blueprint, jsonify

exceptions_blueprint = Blueprint('exceptions_blueprint', __name__)


class APIError(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


class RequiredParameterError(APIError):
    pass


class EvaluationError(APIError):
    pass


@exceptions_blueprint.app_errorhandler(RequiredParameterError)
@exceptions_blueprint.app_errorhandler(EvaluationError)
def handle_api_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
