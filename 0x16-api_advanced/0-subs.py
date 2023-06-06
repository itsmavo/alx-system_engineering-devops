#!/usr/bin/python3
""" Get subscribers from subbreddits """
from requests import get
from sys import argv

def number_of_subscribers(subreddit):
    """Number of subs """
    header = {'User-Agent': 'Kusimi Ate'}
    count = get('https://www.reddit.com/r/{}/about.json'.format(
        subreddit), headers=header).json()
    try:
        return count.get('data').get('subscribers')
    except:
        return 0

if __name__ == "__main__":
    number_of_subscribers(argv[1])
