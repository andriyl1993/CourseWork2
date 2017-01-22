import requests
import json

def request_get(url, data={}):
    r = requests.get(url, params=data)
    return r

def request_post(request, url, data={}):
    r = requests.post(url,data)
    return json.loads(r.text)