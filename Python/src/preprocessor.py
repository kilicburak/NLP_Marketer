import spacy
from werkzeug.exceptions import abort

from Python.src.constants import DATA_MODEL_ERROR

# A class to initiate the nlp processes and pre-process the text instances.
class Preprocessor:

    def __init__(self, text, model_name):
        self.text = text
        self.model_name = model_name

    def _nlp_pre_process(self):
        document = None
        try:
            nlp = spacy.load(self.model_name)
            document = nlp(self.text)
        except(TypeError, OSError):
            abort(400, DATA_MODEL_ERROR)
        return document

    def _get_noun_adjective_chunks(self):
        document = self._nlp_pre_process()
        apartment_properties = [chunk.text for chunk in document.noun_chunks]
        return apartment_properties

    def nlp_process(self):
        apartment_info = self._get_noun_adjective_chunks()
        return list(dict.fromkeys(apartment_info))
