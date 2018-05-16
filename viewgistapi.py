import requests
import json

BASE_URL = 'https://api.github.com'
Link_URL = 'https://gist.github.com'

username = 'falseneutral'
api_token = '98e11ab93a350d690ad55b89a4503fb7092835d8'
gist_id = 'fc4cee21f20ef9642ac4e797f1cc16d1'

header = { 'X-Github-Username': '%s' % username,
           'Content-Type': 'application/json',
           'Authorization': 'token %s' % api_token,
           }
url = '/gists/%s' % gist_id

r = requests.get('%s%s' % (BASE_URL, url),
                  headers=header
                  )
print r.json()
