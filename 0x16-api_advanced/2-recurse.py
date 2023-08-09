#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[], after=None):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Your User Agent'}  # Replace with your user agent
    
    if after:
        params = {'after': after}
    else:
        params = None
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 404:
        return None
    
    data = response.json()
    
    if 'data' in data and 'children' in data['data']:
        children = data['data']['children']
        for child in children:
            hot_list.append(child['data']['title'])
        
        if data['data']['after']:
            recurse(subreddit, hot_list, data['data']['after'])
    
    return hot_list

subreddit_name = 'python'  # Replace with the subreddit you want to query
hot_articles = recurse(subreddit_name)
if hot_articles is not None:
    for idx, title in enumerate(hot_articles, start=1):
        print(f"{idx}. {title}")
else:
    print(f"Subreddit '{subreddit_name}' not found or invalid.")
