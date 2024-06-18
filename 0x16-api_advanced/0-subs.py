#!/usr/bin/python3
"""
queries the Reddit API and returns the number
of subscribers (not active users, total subscribers)
for a given subreddit. If an invalid subreddit is given,
the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """returns number of total subscribers"""
    url = ("https://api.reddit.com/r/{}/about".format(subreddit))
    headers = {'User-Agent': 'CustomClient/1.0'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status() 
    except requests.RequestException:
        return 0
    
    try:
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    except ValueError:
        return 0

