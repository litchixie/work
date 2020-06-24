# coding:utf-8
import requests
import json



def token():
    s = requests.session()
    r = s.get("URL")
    toekn = r.text
    toekn = r.json()["token"]
    return toekn

