import unittest
from unittest.mock import patch
import requests
from github_api import get_user_repos_commits


class MockResponse:
    """Mock API response"""

    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.exceptions.HTTPError(f"{self.status_code} Error")


class TestGitHubAPI(unittest.TestCase):

    @patch('github_api.requests.get')
    def test_valid_user_with_repos(self, mock_get):
        mock_get.side_effect = [
            MockResponse([{'name': 'repo1'}, {'name': 'repo2'}], 200),
            MockResponse([{}, {}, {}], 200),  # 3 commits
            MockResponse([{}, {}, {}, {}], 200)  # 4 commits
        ]
        result = get_user_repos_commits('testuser')
        self.assertEqual(result, [('repo1', 3), ('repo2', 4)])

    @patch('github_api.requests.get')
    def test_valid_user_no_repos(self, mock_get):
        mock_get.return_value = MockResponse([], 200)
        result = get_user_repos_commits('testuser')
        self.assertEqual(result, "User 'testuser' has no public repositories.")

    @patch('github_api.requests.get')
    def test_invalid_user(self, mock_get):
        mock_get.return_value = MockResponse({"message": "Not Found"}, 404)
        result = get_user_repos_commits('invaliduser')
        self.assertIn("HTTP error", result)

    @patch('github_api.requests.get')
    def test_api_failure(self, mock_get):
        mock_get.return_value = MockResponse({"message": "Server Error"}, 500)
        result = get_user_repos_commits('testuser')
        self.assertIn("HTTP error", result)


if __name__ == '__main__':
    unittest.main()