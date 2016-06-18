import os
import sys
from bs4 import BeautifulSoup
import urllib2


url= 'https://www.facebook.com/search/top/?q=light_prayer89%40hotmail.com'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())

print soup
