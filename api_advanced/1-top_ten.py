#!/usr/bin/python3
"""
Reddit API: Print top 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Prints the top 10 hot posts for a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'MyRedditBot/0.1'}

    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
    except requests.RequestException:
        print(None)
        return

    # Handle invalid subreddit or redirect
    if response.status_code != 200:
        print(None)
        return

    try:
        posts = response.json().get("data", {}).get("children", [])
        if not posts:
            print(None)
            return

        for post in posts:
            print(post.get("data", {}).get("title"))
    except Exception:
        print(None)

