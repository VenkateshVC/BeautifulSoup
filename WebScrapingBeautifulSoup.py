#This Program, extracts all the HyperLinks in a webpage and stores in a List.

import requests
from bs4 import BeautifulSoup

#Program requests the user to enter the website name whose links are sought.

InputWebsiteName = str(input("Enter Website Name")).strip()

if not InputWebsiteName.startswith("http"):
    InputWebsiteName = "http://"+InputWebsiteName

try:
    result = requests.get(InputWebsiteName)
except Exception as e:
    print("Exception occurred " + e.__str__())
    exit(-1)

print("Connection Status Code is {}".format(result.status_code))

#Output is written into the following File - WebsiteLinks.txt
outFileName = "OutputWebLinks.txt"
outFileHandle = open(outFileName,"w")
outFileHandle.write("Accessing the HREF Links from " + InputWebsiteName + "\n")
outFileHandle.write("*".center(80,"*") + "\n")

ContentSource = result.content
#soup = BeautifulSoup(ContentSource, features="html.parser")
soup = BeautifulSoup(ContentSource, "lxml")
#Find All the lines with Hyperlinks in the page and save to a List.
ListofHyperLinks = soup.find_all("a")

HrefLinks = [] #Create a list to just save the weblinks after parsing thru the <a> tags

for Link in ListofHyperLinks:
    LinkElements = str(Link).split() #Split each Link from anchor tag by spaces and save in a list

    for LinkItem in LinkElements:
        strLinkItem = str(LinkItem)

        #Parse each Link item and extract the website link

        if strLinkItem.startswith("href="):
            startIndex = strLinkItem.index('"')
            endIndex = strLinkItem.rindex('"')
            LinkValue = strLinkItem[startIndex+1:endIndex]
            if LinkValue.startswith("https:"):
                HrefLinks.append(LinkValue)

#Write all the web Links into a FIle.
for x in HrefLinks:
    outFileHandle.write(x + "\n")
outFileHandle.write("*".center(80,"*"))
outFileHandle.close()