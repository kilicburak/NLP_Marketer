import unittest

from werkzeug import exceptions

from Python.src.constants import PAYLOAD_NOT_FOUND_ERROR
from Python.src.request import Request

response_type = '400 Bad Request: '
init_request = Request()


class TestRequest(unittest.TestCase):
    def test_check_payload_fail(self):
        with self.assertRaisesRegex(exceptions.BadRequest, response_type + PAYLOAD_NOT_FOUND_ERROR):
            init_request._check_file_payload('')

    def test_check_payload_pass(self):
        self.assertEqual('test', init_request._check_file_payload('test'))
