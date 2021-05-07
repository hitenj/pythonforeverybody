import urllib.request, urllib.parse, urllib.error
import json

key='http://py4e-data.dr-chuck.net/json?'
api_key=42

address = input('Enter location: ')

parms = dict()
parms['address'] = address
parms['key'] = api_key

url = key + urllib.parse.urlencode(parms)

print("Retrieving ", url)

uh = urllib.request.urlopen(url).read().decode()
print('Retrieved', len(uh), 'characters')

try:
    data = json.loads(uh)
except:
    data = None

Id = data['results'][0]['place_id']
print('Place id', Id)