import json
import os
import platform
import sys

if platform.system() == "Windows":
    separator = "\\"
else:
    separator = "/"
sys.path.insert(
    0, "/".join(os.path.dirname(os.path.realpath(__file__)).split(separator)[:-1])
)

import unittest

import requests
import trython
from requests.exceptions import MissingSchema
import trython_validators

VALID_JSON = "https://jsonplaceholder.typicode.com/posts"
VALID_XML = (
    "https://www.cs.utexas.edu/~mitra/csFall2015/cs329/lectures/xml/xslplanes.1.xml.txt"
)
VALID_RSS = "https://www.feedforall.com/sample.xml"


class testFunctionErrorHandling(unittest.TestCase):
    def test_decotator(self):
        @trython.wrap(
            time_to_sleep=1,
            number_of_attempts=2,
            validator=trython_validators.requests_json_validator,
        )
        def test(url):
            return requests.get(url)

        self.assertRaises(MissingSchema, test, "f")
        self.assertRaises(json.decoder.JSONDecodeError, test, VALID_RSS)
        test(VALID_JSON)

    def test_wrap(self):
        requests.get = trython.wrap(
            requests.get,
            time_to_sleep=1,
            validator=trython_validators.requests_xml_validator,
        )
        try:
            requests.get(VALID_XML)
        except:
            self.fail("function should not have failed")

    def test_context_manager(self):
        with trython.context_wrap(
            requests.get,
            validator=trython_validators.requests_json_validator,
            time_to_sleep=1,
        ) as get:
            self.assertRaises(MissingSchema, get, "f")
            self.assertRaises(json.decoder.JSONDecodeError, get, VALID_RSS)
            try:
                get(VALID_JSON)
            except:
                self.fail("function should not have failed")

    def test_on_exception_callback(self):
        def raising_error(exception: Exception, message: str):
            raise exception(message)

        def check_if_hello_world(e, attempt_number):
            self.count += 1
            if str(e) == "hello world":
                pass
            else:
                raise e

        with trython.context_wrap(
            raising_error,
            number_of_attempts=3,
            time_to_sleep=1,
            on_exception_callback=check_if_hello_world,
        ) as func:
            try:
                self.count = 0
                func(Exception, "hello world")
            except:
                assert self.count == 3

            try:
                self.count = 0
                func(Exception, "something else")
            except:
                assert self.count == 1

    def test_overwrite(self):
        def on_exception(e, attempt_number, result):
            self.count += 1

        self.count = 0
        with trython.context_wrap(
            requests.get,
            number_of_attempts=3,
            validator=trython_validators.requests_json_validator,
            time_to_sleep=2,
            on_validation_failure_callback=on_exception,
            overwrite=True,
            overwrite_path="requests",
        ):
            try:
                requests.get(VALID_XML)
            except:
                assert self.count == 3


if __name__ == "__main__":
    unittest.main()
