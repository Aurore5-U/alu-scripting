#!/usr/bin/python3
"""Print the titles of the first 10 hot posts of a subreddit"""
import requests


def top_ten(subreddit):
    """Fetch and print titles of top 10 hot posts"""
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    
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
        data = json_data.get('data', {}).get('children', [])
        
        if not data:
            print("None")
            return
            
        for post in data:
            title = post.get('data', {}).get('title')
            if title:
                print(title)
                
    except (ValueError, KeyError, TypeError):
        print("None")
        return
