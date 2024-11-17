import requests

baseurl = 'http://api.icndb.com/jokes/random'
response = requests.get(baseurl, params={'limitTo': ['nerdy']})
print(response.raise_for_status())
outputs = response.json()

print(outputs)