#!/usr/bin/python3
""" Function that gets all hot articles within 
    a subreddit"""
from requests import get
from sys import argv

def recurse(subreddit, hot_list=[], after=None):
    """ Recursively check for hot topics in Subreddits"""
    header = {'User-Agent': 'Kusimi Ate'}
    try:
        if after:
            hot_post = get('https://www.reddit.com/r/{}/hot.json?after={}'.format(
                subreddit, after), headers=header).json().get('data')
        else:
            hot_post = get('https://www.reddit.com/r/{}/hot.json'.format(
                subreddit), headers=header).json().get('data')
        hot_list += [dic.get('data').get('title')
                for dic in hot_post.get('children')]
        if hot_post.get('after'):
            return recurse(subreddit, hot_list, after=hot_post.get('after'))
        return hot_list
    except:
        return None


if __name__ == "__main__":
    recurse(argv[1])

