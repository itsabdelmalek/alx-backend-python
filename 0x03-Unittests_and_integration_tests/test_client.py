#!/usr/bin/env python3
"""
Unit test test for client.py
"""


import unittest
from urllib import response
from parameterized import parameterized, parameterized_class
from unittest import mock
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    Tests for githuborgclient classs
    """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, data, mock_json):
        """
        Test the org method of GithubOrgClient.
        """
        end_point = 'https://api.github.com/orgs/{}'.format(data)
        specs = GithubOrgClient(data)
        specs.org()
        mock_json.assert_called_once_with(end_point)

    @parameterized.expand([
        ('random_url', {'repos_url': 'http://some_url.com'})
    ])
    def test_public_repos_url(self, org_name, result):
        """
        Test the _public_repos_url property of GithubOrgClient.
        """
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=result)):
            response = GithubOrgClient(org_name)._public_repos_url
            self.assertEqual(response, result.get('repos_url'))

    @patch('client.get_json')
    def test_public_repos(self, mock_pub_repos):
        """
        Test the public_repos method of GithubOrgClient.
        """
        payload = [{"name": "Google"}, {"name": "TT"}]
        mock_pub_repos.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mocked_public:

            mocked_public.return_value = "world"
            response = GithubOrgClient('test').public_repos()

            self.assertEqual(response, ["Google", "TT"])

            mocked_public.assert_called_once()
            mock_pub_repos.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, licence_key, expect_result):
        """
        Test the has_license method of GithubOrgClient.
        """
        result = GithubOrgClient.has_license(repo, licence_key)
        self.assertEqual(result, expect_result)


@parameterized_class(['org_payload', 'repos_payload',
                      'expected_repos', 'apache2_repos'], TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration tests for the GithubOrgClient class.
    """
    @classmethod
    def setUpClass(cls):
        """
        Set up the test class.
        """
        cls.get_patcher = patch('requests.get', side_effect=[
            cls.org_payload, cls.repos_payload
        ])
        cls.mocked_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """
        Tear down the test class.
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test the public_repos method of GithubOrgClient in an
        integration test.
        """

    def test_public_repos_with_license(self):
        """
        Test the public_repos method of GithubOrgClient with a specific
        license filter.
        """


if __name__ == '__main__':
    unittest.main()
