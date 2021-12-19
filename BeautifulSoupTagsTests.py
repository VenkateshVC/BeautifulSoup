#This is a Beautiful Soup Program to test all the Tags and the BS Functions

import requests
from bs4 import BeautifulSoup

InputWebsiteName = "https://www.google.com"

try:
    result = requests.get(InputWebsiteName)
except Exception as e:
    print("Exception occurred " + e.__str__())
    exit(-1)

ContentSource = result.content
soup = BeautifulSoup(ContentSource, features="html.parser")

tag = soup.find_all(["a","b"])
print(tag)
for tag_items in tag:
    print(tag_items.text)
#for key,value in tag.attrs.items():
#    print("The Attribute: {}, has the Value {}".format(key,value))


