#!/usr/bin/env python3
"""
Test Module for the file client.py
"""
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from client import GithubOrgClient
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """Class for unit testing the class GithubOrgClient"""

    @parameterized.expand([
        ("google", {"org": "google"}),
        ("abc", {"org": "abc"})
    ])
    @patch("client.get_json")
    def test_org(
        self,
        org_name: str,
        expected: Dict,
        mock_get_json: MagicMock
    ):
        """Testing the org method of GithubOrgClient class"""
        mock_get_json.return_value = expected
        client = GithubOrgClient(org_name)
        result = client.org
        mock_get_json.assert_called_once_with(
            client.ORG_URL.format(org=org_name)
        )
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
