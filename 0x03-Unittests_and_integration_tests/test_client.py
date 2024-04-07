#!/usr/bin/env python3
"""
Test Module for client.py
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Class for unit testing the class GithubOrgClient"""

    @parameterized.expand([
        ("google"), ("abc")
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test GithubOrgClient.org method"""
        mock_get_json.return_value = {"org": org_name}
        client = GithubOrgClient(org_name)
        result = client.org
        mock_get_json.assert_called_once_with(
            client.ORG_URL.format(org=org_name)
        )
        self.assertEqual(result, {"org": org_name})


if __name__ == "__main__":
    unittest.main()
