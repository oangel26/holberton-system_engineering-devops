#!/usr/bin/python3
""" Query subs on Reddit """
import json
import requests


def number_of_subscribers(reddit):
    user = {"User-Agent": "No se"}
    request = requests.get("https://www.reddit.com/r/{}/about.json"
                           .format(reddit), headers=user)
    if request.status_code == 200:
        return request.json().get("data").get("subscribers")
    else:
        return 0
