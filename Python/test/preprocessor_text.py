import unittest

from werkzeug import exceptions

from Python.src.constants import DATA_MODEL_ERROR
from Python.src.preprocessor import Preprocessor

response_type = '400 Bad Request: '


class TestPreprocessor(unittest.TestCase):
    def test_nlp_preprocessor_green(self):
        init_preprocessor = Preprocessor('test', 'en_core_web_sm')
        self.assertIsNotNone(init_preprocessor._nlp_pre_process())

    def test_nlp_preprocessor_no_text(self):
        init_preprocessor = Preprocessor(None, 'en_core_web_sm')
        with self.assertRaisesRegex(exceptions.BadRequest, response_type + DATA_MODEL_ERROR):
            init_preprocessor._nlp_pre_process()

    def test_nlp_preprocessor_no_model(self):
        init_preprocessor = Preprocessor('test', '')
        with self.assertRaisesRegex(exceptions.BadRequest, response_type + DATA_MODEL_ERROR):
            init_preprocessor._nlp_pre_process()
