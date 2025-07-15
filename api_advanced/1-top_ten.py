#!/usr/bin/python3
"""
Reddit API: Print top 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Prints the top 10 hot posts for a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'MyRedditBot/0.1'}

    try:
        response = requests.get(
            url, headers=headers, allow_redirects=False, timeout=10)
    except requests.RequestException:
        return

    if response.status_code != 200:
        return

    try:
        posts = response.json().get("data", {}).get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title"))
    except Exception:
        return

