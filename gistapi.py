import requests
import json

BASE_URL = 'https://api.github.com'
Link_URL = 'https://gist.github.com'
username = 'falseneutral'
api_token = 'f52a37144e8e0a627eb4df17b547324049e87166'
header = { 'X-Github-Username': '%s' % username,
           'Content-Type': 'application/json',
           'Authorization': 'token %s' % api_token,
           }
url = '/gists'
data = {
    "description": "the description for this gist",
    "public": True,
    "files": {
        "file1.txt" : {
        "content": "String file contents"
        }
    }
}

r = requests.post('%s%s' % (BASE_URL, url),
                  headers=header,
                  data=json.dumps(data))
print r.json()['url']
