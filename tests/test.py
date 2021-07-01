
import json
import sys
import os
import platform
if platform.system() == 'Windows':
    separator = '\\'
else:
    separator = '/'
sys.path.insert(0, '/'.join(os.path.dirname(os.path.realpath(__file__)).split(separator)[:-1]))

import function_error_handling
from function_error_handling import validators

import unittest
import requests
from requests.exceptions import MissingSchema


VALID_JSON = 'https://jsonplaceholder.typicode.com/posts'
VALID_XML = 'https://www.cs.utexas.edu/~mitra/csFall2015/cs329/lectures/xml/xslplanes.1.xml.txt'
VALID_RSS = 'https://www.feedforall.com/sample.xml'


class testFunctionErrorHandling(unittest.TestCase):

    def test_decotator(self):

        @function_error_handling.wrap(time_to_sleep=1, number_of_attempts=2, validator= validators.requests_json_validator)
        def test(url):
            return requests.get(url)
        
        self.assertRaises(MissingSchema, test, 'f')
        self.assertRaises(json.decoder.JSONDecodeError, test, VALID_RSS)
        test(VALID_JSON)



    def test_wrap(self):
        requests.get = function_error_handling.wrap(requests.get, time_to_sleep=1, validator= validators.requests_xml_validator)
        try:
            requests.get(VALID_XML)
        except:
            self.fail("function should not have failed")


    def test_context_manager(self):
        with function_error_handling.context_wrap(requests.get, validator=validators.requests_json_validator, time_to_sleep=1) as get:
            self.assertRaises(MissingSchema, get, 'f')
            self.assertRaises(json.decoder.JSONDecodeError, get, VALID_RSS)
            try:
                get(VALID_JSON)
            except:
                self.fail("function should not have failed")


if __name__ == '__main__':
    unittest.main()
