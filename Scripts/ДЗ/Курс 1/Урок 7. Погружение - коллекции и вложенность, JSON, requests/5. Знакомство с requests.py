# noinspection PyUnresolvedReferences
import requests
import json
response = requests.get('https://jsonkeeper.com/b/O2SV')

test = response.text
states = json.loads(test)
print(test)