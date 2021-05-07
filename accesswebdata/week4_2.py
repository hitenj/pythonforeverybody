import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input('Enter URL')
pos=int(input('Enter position'))
count=int(input('Enter count'))

print(url)

for i in range(0,count):
    html=urllib.request.urlopen(url, context=ctx).read()
    soup=BeautifulSoup(html, "lxml")

    c=0
    links=soup('a')
    for link in links:
        c+=1
        if c==pos:
            print(link.get("href", None))
            url=str(link.get("href", None))
            c=0
            break

