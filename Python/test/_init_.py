import os
import sys
from unittest import TestLoader, TextTestRunner, TestSuite



sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                "../..")))
from Python.test.data_extraction_test import TestDataExtraction
from Python.test.preprocessor_text import TestPreprocessor
from Python.test.request_test import TestRequest

if __name__ == "__main__":
    loader = TestLoader()
    tests = [
        loader.loadTestsFromTestCase(test)
        for test in
        (TestDataExtraction, TestPreprocessor, TestRequest)
    ]
    suite = TestSuite(tests)
    runner = TextTestRunner(verbosity=3)
    runner.run(suite)
