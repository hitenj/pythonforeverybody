import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input('Enter the URL')

data=urllib.request.urlopen(url, context=ctx).read()

print('Retrieved ',len(data),' characters')

tree=ET.fromstring(data)

comment=tree.findall('.//comment')
print('Count: ',len(comment))

sum1=0

for item in comment:
    sum1+=int(item.find('count').text)

print(sum1)

