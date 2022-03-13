from bs4 import BeautifulSoup
import requests

url = 'https://coinmarketcap.com/nft/'

result = requests.get(url)
doc = BeautifulSoup(result.text, 'html.parser')
tbody = doc.find("tbody").contents
nfts = []
for trs in tbody:
    information = {}
    rank, name, price = trs.find_all('td')[0:3]
    information["rank"] = rank.string
    information["name"] = name.span.string
    information["price"] = price.div.contents[0]
    nfts.append(information)

print(nfts)
