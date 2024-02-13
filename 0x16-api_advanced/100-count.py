#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""

import requests


def count_words(subreddit, word_list, after="", word_dict={}):
    """
    A recursive function that queries the Reddit API,
    parses the title of all hot articles, and prints a
    sorted count of given keywords
    """

    word_list = map(lambda x: x.lower(), word_list)
    word_list = list(set(word_list))

    url = "https://reddit.com/r/{}/hot/.json".format(subreddit)
    userAgent = "ApiAdvanced Morabet"

    data = requests.get(
            url, headers={"user-agent": userAgent},
            params={"after": after}
            )

    if not data:
        return None

    result = data.json().get('data').get('children')
    for obj in result:
        title = obj.get('data').get('title').lower()
        for word in word_list:
            if word in title:
                count = title.count(word)
                word_dict[word] = word_dict.get(word, 0) + count

    after = data.json().get('data').get('after')
    if after is not None:
        return count_words(subreddit, word_list, after, word_dict)

    word_dict = sorted(word_dict.items(), key=lambda item: item[0])

    [print("{}: {}".format(k, v)) for k, v in word_dict]
