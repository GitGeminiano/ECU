import os
import sys
from bs4 import BeautifulSoup
import urllib2


url= 'https://www.facebook.com/search/top/?q=light_prayer89%40hotmail.com'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
soup_string = str(soup)
name = soup_string.find("_5d-5")
i = 7
while not soup_string[name+i] == "<":

    print soup_string[name+i]
    i = i+1


print name
#name = soup.find()
#rank = soup.find({"class": "5d-4"}).contents
#soup.find_all("a", class_="sister")
#soup.find("div", class_="_5d-4")
#body = soup.body.div
#source_code_string = str(body)

#page = urllib2.urlopen(url)
#soup = BeautifulSoup(page.read())
#soup_string = str(soup)
#name = re.search("_5d-5", soup_string).group(0)
