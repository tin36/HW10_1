import requests

for i in range(10):
  response = requests.get('https://onvolga.ru/online/zapros-site.html')

  print(response)
  #print(f"{i+1} - {response.json()['fact']}")
