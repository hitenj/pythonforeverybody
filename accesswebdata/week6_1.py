import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input('Enter Location:')

print('Retrieving ',url)

uh=urllib.request.urlopen(url, context=ctx).read()

print('Retrieved ',len(uh),' characters')

data=json.loads(uh)

sum1=0
c=0

for items in data['comments']:
    c+=1
    sum1+=int(items["count"])

print('count: ',c)
print('sum: ',sum1)

