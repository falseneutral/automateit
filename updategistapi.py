import requests
import json

BASE_URL = 'https://api.github.com'
Link_URL = 'https://gist.github.com'

username = 'falseneutral'
api_token = '3132b993033079d077396e3347ad83dfc01f63bd'
gist_id = 'fc4cee21f20ef9642ac4e797f1cc16d1'

header = { 'X-Github-Username': '%s' % username,
           'Content-Type': 'application/json',
           'Authorization': 'token %s' % api_token,
           }
data = {
    "description": "updating the description for this gist",
    "public": True,
    "files": {
        "file1.txt" : {
        "content": "Updating file contents..."
        }
    }
}

url = '/gists/%s' % gist_id

r = requests.patch('%s%s' % (BASE_URL, url),
                  headers=header,
                   data=json.dumps(data)
                  )
print r.json()
