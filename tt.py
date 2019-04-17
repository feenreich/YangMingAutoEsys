from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys

name = sys.argv[1]
url = "https://twitter.com/" + name
content = urlopen(url).read()
soup = BeautifulSoup(content, 'html.parser')

list = soup.select('.js-tweet-text-container')
filename = name + ".txt"
f = open(filename, "w", encoding = 'UTF-8', newline = '')
for x in list:
	f.write(x.getText() + '\n')
f.close()