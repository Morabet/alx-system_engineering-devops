#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""

import requests


def top_ten(subreddit):
    """Return the total number of subscribers on a given subreddit."""

    url = "https://reddit.com/r/{}/hot.json".format(subreddit)
    userAgent = "ApiAdvanced Morabet"

    data = requests.get(
            url, headers={"user-agent": userAgent},
            params={"limit": 10}
            )

    if not data:
        print('None')
        return
    result = data.json().get('data').get('children')
    for obj in result:
        print(obj.get('data').get('title'))

    return
