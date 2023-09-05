#!/usr/bin/python3
"""
script that lists 10 commits (from most recent to oldest) of a repository.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 3:
        repository_name = sys.argv[1]
        owner_name = sys.argv[2]

        url = (
            f"https://api.github.com/repos/{owner_name}/{repository_name}"
            "/commits"
        )

        try:
            # Make a GET request to the GitHub API
            response = requests.get(url)

            # Check if the request was successful
            if response.status_code == 200:
                commits = response.json()

                # Print the most recent 10 commits
                for commit in commits[:10]:
                    sha = commit["sha"]
                    author_name = commit["commit"]["author"]["name"]
                    print(f"{sha}: {author_name}")
            else:
                print("Error: Unable to fetch commits")
        except requests.exceptions.RequestException as e:
            print("Error: Unable to connect to GitHub API")
    else:
        print("Usage: ./100-github_commits.py <repository_name> <owner_name>")
