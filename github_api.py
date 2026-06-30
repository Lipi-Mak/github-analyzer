import requests

def fetch_repositories(username):
    username = username.strip()
    if not username:
        return None

    url = f"https://api.github.com/users/{username}/repos"

    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()