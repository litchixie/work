# coding:utf-8
import requests
import json



def token():
    s = requests.session()
    r = s.get("http://192.168.14.228:1337/api/v1/token")
    toekn = r.text
    toekn = r.json()["token"]
    return toekn

