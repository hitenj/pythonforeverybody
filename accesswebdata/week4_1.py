from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url= input('Enter a URL')
html= urlopen(url, context=ctx).read()
soup= BeautifulSoup(html, "lxml")

sum1=0
count=0

number=soup('span')
for numb in number:
    count+=1
    sum1+=int(numb.contents[0])

print(count)
print(sum1)

