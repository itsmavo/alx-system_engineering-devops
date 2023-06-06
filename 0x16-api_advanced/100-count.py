#!/usr/bin/python3
""" Count Keywords with Subreddits """
from requests import get
from sys import argv

hotlist = []
after = None


def count_all(hotlist, word_list):
    count_word = {word.lower(): 0 for word in word_list}
    for title in hotlist:
        words = title.split(' ')
        for word in words:
            if count_word.get(word) is not None:
                count_word[word] += 1

    for key in sorted(count_word, key=count_word.get, reverse=True):
        if count_word.get(key):
            for sth in word_list:
                if key == sth.lower():
                    print("{}: {}".format(sth, count_word[key]))


def count_words(subreddit, word_list):
    global hotlist
    global after
    """ Checking with API """
    header = {'User-Agent': 'Kusimi Ate'}
    if after:
        cnt = get('https://www.reddit.com/r/{}/hot.json?after={}'.format(
            subreddit, after), headers=header).json().get('data')
    else:
        cnt = get('https://www.reddit.com/r/{}/hot.json?'.format(
            subreddit), headers=header).json().get('data')
    hotlist += [dic.get('data').get('title').lower()
            for dic in cnt.get('children')]
    after = cnt.get('after')
    if after:
        return count_words(subreddit, word_list)
    return count_all(hotlist, word_list)

if __name__ == "__main__":
    count_words(argv[1], argv[2].split(' '))
