#!/usr/bin/python3
"""Script that returns the numbers of
subscribers"""

import requests


def number_of_subscribers(subreddit):
    """Function that returns the numbers of
    subscribers"""

    url = "https://reddit.com/r/{}/about.json".format(subreddit)
    userAgent = "ApiAdvanced Morabet"

    data = requests.get(url, headers={"user-agent": userAgent})
    if not data:
        return 0
    result = data.json().get('data').get('subscribers')
    if result:
        return result
    else:
        return 0
