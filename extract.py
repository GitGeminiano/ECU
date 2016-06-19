import os
import sys
from bs4 import BeautifulSoup
import urllib2

email = "light_prayer89@hotmail.com"
email_url = email.replace("@", "%40")
prefix = "https://www.facebook.com/search/top/?q="
url= prefix + email_url
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
soup_string = str(soup)
index_div_name = soup_string.find("_5d-5")
if index_div_name != - 1:
  name = ""
  offset = 7
  while not soup_string[index_div_name+offset] == "<":
    name += soup_string[index_div_name+offset]
    offset = offset + 1
  print(name)

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
