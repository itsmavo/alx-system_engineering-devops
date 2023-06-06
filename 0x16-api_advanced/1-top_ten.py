#!/usr/bin/python3
""" Get top ten posts on a subreddit """
from requests import get
from sys import argv


def top_ten(subreddit):
    """ Limit the results to ten posts """
    header = {'User-Agent': 'Kusimi Ate'}
    try: 
        posts = get('https://www.reddit.com/r/{}/hot.json?count=10'.format(
            subreddit), headers=header).json().get('data').get('children')
        print('\n'.join([dic.get('data').get('title')
            for dic in posts][:10]))
    except:
        print('None')

if __name__ == "__main__":
    top_ten(argv[1])
