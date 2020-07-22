# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import petstore_api
from petstore_api.model.additional_properties_array import AdditionalPropertiesArray


class TestAdditionalPropertiesArray(unittest.TestCase):
    """AdditionalPropertiesArray unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAdditionalPropertiesArray(self):
        """Test AdditionalPropertiesArray"""
        # can make model without additional properties
        model = AdditionalPropertiesArray()

        # can make one with additional properties
        import datetime
        some_val = []
        model = AdditionalPropertiesArray(some_key=some_val)
        assert model['some_key'] == some_val
        some_val = [True, datetime.date(1970,1,1), datetime.datetime(1970,1,1), {}, 3.1, 1, [], 'hello']
        model = AdditionalPropertiesArray(some_key=some_val)
        assert model['some_key'] == some_val

        # type checking works on additional properties
        with self.assertRaises(petstore_api.ApiTypeError) as exc:
            model = AdditionalPropertiesArray(some_key='some string')


if __name__ == '__main__':
    unittest.main()
