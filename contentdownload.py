from bs4 import BeautifulSoup
import re
import urllib2
import os

image_type = "Project"
movie = "Avatar"
url = "https://www.google.com/search?q="+movie+"&source=hp&tbm=isch"

header = {'|User-Agent':'Mozilla/5.0'}
soup = BeautifulSoup(urllib2.urlopen(urllib2.Request(url, headers=header)))

images = [a['src'] for a in soup.find_all("img", {"src":re.compile("gstatic.com")})][:5]

for img in images:
    print "Image Source:", img