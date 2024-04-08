#!/usr/bin/env python3
"""
Test Module for the file client.py
"""
import unittest
from unittest.mock import patch, MagicMock, PropertyMock
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
        org: str,
        expected: Dict,
        mock_get_json: MagicMock
    ):
        """Testing the org method of GithubOrgClient class"""
        mock_get_json.return_value = expected
        client = GithubOrgClient(org)
        result = client.org
        mock_get_json.assert_called_once_with(
            client.ORG_URL.format(org=org)
        )
        self.assertEqual(result, expected)

    def test_public_repos_url(self):
        """Testing the _public_repos_url method of GithubOrgClient class"""
        with patch.object(
            GithubOrgClient,
            "org",
            new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = {"repos_url": "payload"}
            client = GithubOrgClient("test")
            self.assertEqual(client._public_repos_url, "payload")

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock):
        """Testing the public_repos method of GithubOrgClient class"""
        test_payload = {
            "repos_url": "https://api.github.com/users/alx/repos",
            "repos": [{"name": "repo_1"}, {"name": "repo_2"}]
            }
        mock_get_json.return_value = test_payload["repos"]
        with patch.object(
            GithubOrgClient,
            "_public_repos_url",
            new_callable=PropertyMock
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload["repos_url"]
            client = GithubOrgClient("alx")
            result = client.public_repos()
            self.assertEqual(result, ["repo_1", "repo_2"])
            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()


if __name__ == "__main__":
    unittest.main()
