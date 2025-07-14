#!/usr/bin/python3
"""Print the titles of the first 10 hot posts of a subreddit"""
import requests


def top_ten(subreddit):
    """Fetch and print titles of top 10 hot posts"""
    if not subreddit:
        print("None")
        return

    headers = {'User-Agent': 'AuroreRedditScript/1.0'}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
    except requests.RequestException:
        print("None")
        return

    if response.status_code != 200:
        print("None")
        return

    try:
        json_data = response.json()
        data = json_data.get("data")
        if not data:
            print("None")
            return
        
        children = data.get("children", [])
        if not children:
            print("None")
            return
            
        for post in children:
            post_data = post.get("data", {})
            title = post_data.get("title")
            if title:
                print(title)
                
    except (ValueError, KeyError, TypeError):
        print("None")
        return
