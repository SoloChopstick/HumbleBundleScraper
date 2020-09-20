#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests

print("hello World!")

url="https://www.humblebundle.com/games/better-futures?hmb_source=navbar&hmb_medium=product_tile&hmb_campaign=tile_index_7"
r = requests.get(url)

soup = BeautifulSoup(r, 'lxml')
print(soup.prettify())

match = soup.title.text
print(match)
