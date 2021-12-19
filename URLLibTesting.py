import urllib.request

response = urllib.request.urlopen('http://data.pr4e.org/page1.htm')
for html in response:
    print(html.decode().strip())