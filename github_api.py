import requests


def get_user_repos_commits(user_id):
    """
    Fetch repositories for a GitHub user and count the number of commits in each repo.
    """
    repos_url = f"https://api.github.com/users/{user_id}/repos"

    try:
        repos_response = requests.get(repos_url)
        repos_response.raise_for_status()
        repos = repos_response.json()

        if not repos:
            return f"User '{user_id}' has no public repositories."

        repo_commit_counts = []
        for repo in repos:
            repo_name = repo['name']
            commits_url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"

            commits_response = requests.get(commits_url)
            commits_response.raise_for_status()
            commits = commits_response.json()

            repo_commit_counts.append((repo_name, len(commits)))

        return repo_commit_counts

    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error: {http_err}"
    except Exception as err:
        return f"Error: {err}"


if __name__ == "__main__":
    user_id = input("Enter a GitHub username: ")
    print(get_user_repos_commits(user_id))