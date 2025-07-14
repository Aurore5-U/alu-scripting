#!/usr/bin/python3
"""Print the titles of the first 10 hot posts of a subreddit"""
import requests


def top_ten(subreddit):
    """Fetch and print titles of top 10 hot posts"""
    headers = {'User-Agent': 'AuroreRedditScript/1.0'}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
    except requests.RequestException:
        print(None)
        retur

