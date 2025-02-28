import unittest
from unittest.mock import patch, Mock
from github_api import get_user_repos_commits


class TestGitHubAPI(unittest.TestCase):

    @patch('github_api.requests.get')
    def test_valid_user_with_repos(self, mock_get):
        # Mock responses for repos and commits
        mock_get.side_effect = [
            Mock(status_code=200, json=Mock(return_value=[{'name': 'repo1'}, {'name': 'repo2'}])),
            Mock(status_code=200, json=Mock(return_value=[{}, {}, {}])),  # 3 commits
            Mock(status_code=200, json=Mock(return_value=[{}, {}, {}, {}]))  # 4 commits
        ]
        result = get_user_repos_commits('testuser')
        self.assertEqual(result, [('repo1', 3), ('repo2', 4)])

    @patch('github_api.requests.get')
    def test_valid_user_no_repos(self, mock_get):
        # Mock response for no repositories
        mock_get.return_value = Mock(status_code=200, json=Mock(return_value=[]))
        result = get_user_repos_commits('testuser')
        self.assertEqual(result, "User 'testuser' has no public repositories.")

    @patch('github_api.requests.get')
    def test_invalid_user(self, mock_get):
        # Mock response for invalid user
        mock_get.return_value = Mock(status_code=404, json=Mock(return_value={"message": "Not Found"}))
        result = get_user_repos_commits('invaliduser')
        self.assertIn("HTTP error", result)

    @patch('github_api.requests.get')
    def test_api_failure(self, mock_get):
        # Mock response for API failure
        mock_get.return_value = Mock(status_code=500, json=Mock(return_value={"message": "Server Error"}))
        result = get_user_repos_commits('testuser')
        self.assertIn("HTTP error", result)


if __name__ == '__main__':
    unittest.main()