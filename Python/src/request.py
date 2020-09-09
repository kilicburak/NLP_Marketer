import json

from flask import request
from werkzeug.exceptions import abort
import ast
from Python.src.constants import PAYLOAD_NOT_FOUND_ERROR, MODEL_NOT_FOUND_ERROR


class Request:

    def __init__(self):
        pass

    def get_data(self):
        property_parameters = self._check_file_payload(request.form.get('json'))
        parse_input = json.loads(property_parameters)
        return parse_input

    def get_text(self):
        text = self._check_file_payload(request.form.get('text'))
        if type(text) == str:
            return text.lower()
        else:
            abort(400, )

    def get_text_list(self):
        texts = self._check_file_payload(request.form.get('texts'))
        if texts:
            return ast.literal_eval(texts)
        else:
            abort(400, )

    def get_model_name(self):
        model_name = request.form.get('modelName')
        if model_name:
            return model_name
        else:
            return abort(400, MODEL_NOT_FOUND_ERROR)

    def _check_file_payload(self, property_parameters):
        if not property_parameters:
            return abort(400, PAYLOAD_NOT_FOUND_ERROR)
        else:
            return property_parameters
