import json

f = open("bittrex_markets.txt", "r")
markets = json.load(f)
f.close()
type(markets)			 # el tipo deberia ser 'dict' si se cargo bien
						 # <class 'dict'>
m = markets["result"]
for i in m:
  if i["MarketName"][0:3] == 'BTC':
    print(i["MarketName"])

for i in m:
  if i["MarketName"][0:3] == 'ETH':
    print(i["MarketName"])

for i in m:
  if i["MarketName"][0:3] == 'USD':
    print(i["MarketName"])

