#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """Returns a list of titles of all hot posts on a given subreddit."""

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
        hot_list.append(obj.get('data').get('title'))

    after = data.json().get('data').get('after')
    if after is not None:
        return recurse(subreddit, hot_list, after)

    return hot_list
