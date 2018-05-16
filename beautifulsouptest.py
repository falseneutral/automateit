import bs4
myfile = open('python.html')
soup = bs4.BeautifulSoup(myfile, 'lxml')

print "Beautiful Soup Object:", type(soup)

print soup.find_all('a')
print soup.find_all('strong')

print soup.find('div', {"id":"inventor"})

print soup.select('#inventor')

print soup.select('.wow')

print "Facebook URL: ", soup.find_all('a')[0]['href']
print "Inventor: ", soup.find('div', {"id":"inventor"}).text
print "Span Content: ", soup.select('span')[0].getText()