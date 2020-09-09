import json
from collections import defaultdict
from werkzeug.exceptions import abort

from Python.src.constants import KEYWORD_NOT_FOUND_ERROR, DATA_MODEL_ERROR
from Python.src.preprocessor import Preprocessor


class DataExtraction:

    def __init__(self, text, data, model_name):
        self.text = text
        self.data = data
        self.model_name = model_name

    def _extract_properties(self, apartment_specs, key):
        property_keywords = self.data[key]
        if len(property_keywords) != 0:
            for keyword in property_keywords:
                if keyword in apartment_specs:
                    return apartment_specs
        else:
            abort(400, KEYWORD_NOT_FOUND_ERROR)

    def map_extracted_properties(self):
        pre_process = Preprocessor(self.text, self.model_name)
        apartment_properties = pre_process.nlp_process()
        default_dict = defaultdict(list)
        try:
            mapped_parameters = [{key: self._extract_properties(apartment_specs, key)} for key in self.data for
                                 apartment_specs in apartment_properties if
                                 self._extract_properties(apartment_specs, key)]
            [default_dict[key].append(value) for dictionary in mapped_parameters for key, value in dictionary.items()]
        except(TypeError, KeyError):
            abort(400, DATA_MODEL_ERROR)
        finally:
            return json.dumps(default_dict)
