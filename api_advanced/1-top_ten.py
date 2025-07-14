#!/usr/bin/python3
"""Print the titles of the first 10 Hot Posts for a subreddit"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts from a subreddit"""
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return

        data = response.json().get('data', {})
        children = data.get('children', [])

        for post in children[:10]:
            print(post.get('data', {}).get('title'))
    except Exception:
        print(None)
