#!/usr/bin/env python3
"""
unit test cases for utils.py
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Tests for the access_nested_map function.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_reults):
        """
        Test access_nested_map for various inputs..
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_reults)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test access_nested_map for exception handling.
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Tests for the get_json function.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test get_json for various inputs.
        """
        class Mocked(Mock):
            """
            class that inherits from Mock
            """

            def json(self):
                """
                json returning a payload
                """
                return test_payload

        with patch("requests.get") as MockClass:
            MockClass.return_value = Mocked()
            self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """
    Tests for the memoize decorator.
    """

    def test_memoize(self):
        """
        Test the memoize decorator.
        """

        class TestClass:
            """
            Test class with a memoized property.
            """

            def a_method(self):
                """
                A simple method.
                """
                return 42

            @memoize
            def a_property(self):
                """
                A memoized property.
                """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mocked:
            specs = TestClass()
            specs.a_property
            specs.a_property
            mocked.asset_called_once()
