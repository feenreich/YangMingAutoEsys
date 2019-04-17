#pylab inline
from urllib.request import urlopen
import time
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

url = "https://twitter.com/WoodenHarp"
content = urlopen(url).read()
soup = BeautifulSoup(content, 'html.parser')


#img=mpimg.imread('your_image.png')
#imgplot = plt.imshow(img)
#plt.show()