import unittest

from werkzeug import exceptions

from Python.src.constants import KEYWORD_NOT_FOUND_ERROR
from Python.src.data_extraction import DataExtraction

response_type = '400 Bad Request: '


class TestDataExtraction(unittest.TestCase):
    def test_data_extraction_no_value(self):
        init_data_extraction = DataExtraction('test', {"test": ''}, 'en_core_web_sm')
        with self.assertRaisesRegex(exceptions.BadRequest, response_type + KEYWORD_NOT_FOUND_ERROR):
            init_data_extraction._extract_properties('test', 'test')

    def test_data_extraction_pass(self):
        init_data_extraction = DataExtraction('test', {"test": 'test'}, 'en_core_web_sm')
        self.assertEqual('test', init_data_extraction._extract_properties('test', 'test'))

    def test_map_extracted_properties_ok_type(self):
        init_data_extraction = DataExtraction('test', {"test": 'test'}, 'en_core_web_sm')
        self.assertEqual(str, type(init_data_extraction.map_extracted_properties()))
