import hashlib

import requests

hash = hashlib.md5(("GetToken/" + "9b7453b5-1fd8-452b-84c0-2f068f53f395" + "200001" + "Peon-1" + "EUR" + "TNBZEKNK").encode('utf-8')).hexdigest()

url = "https://partner.k8s-prod.slots.lan/partnersV2/GetToken"

body = {
  "clientGuid": "9b7453b5-1fd8-452b-84c0-2f068f53f395",
  "gameId": 200001,
  "userId": "Peon-1",
  "currency": "EUR",
  "lang": "EN",
  "demoMode": False,
  "hash": hash
}

response = requests.post(url=url, json=body, verify=False)
print(response.json())
