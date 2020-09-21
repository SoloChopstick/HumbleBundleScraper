#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests

url="https://www.humblebundle.com/games/better-futures?hmb_source=navbar&hmb_medium=product_tile&hmb_campaign=tile_index_7"
req = requests.get(url).text

soup = BeautifulSoup(req, 'html.parser')
#print(soup.prettify().encode("utf-8")
#print(soup.title)

# Datastructure, empty dictionary
tiers_dict = {}

#Bundle tiers
tiers = soup.select(".dd-game-row")
for tier in tiers:
    #if has a headline
    if tier.select(".dd-head-headline"):
        #Grab tier name and price
        tiername = tier.select(".dd-head-headline")[0].text.strip()

        #Grab tier product names
        product_names = tier.select(".front-page-art-image-text")
        product_names = [prodname.text.strip() for prodname in product_names]

        # Add
        tier_dict[tiername] = {"products": product_names}

for tiername, tierinfo in tiers_dict.items():
    print(tiername)
    print("priced at", tierinfo['price'])
    print("products:")
    print(", ".join(tierinfo['products']))
    print("\n")

#Bundle tiers class: (price and tier)
#tier_headlines = soup.select(".dd-header-headline")

#stripped_tiernames = []
#for tier in tier_headlines:
#    stripped_tiernames.append(tier.text.strip())
    #print(tier.text.strip())

#Product Names
#product_names = soup.select(".front-page-art-image-text")
#stripped_product_names = []
#for product in product_names:
#    stripped_product_names.append(product.text.strip())
    #print(product.text.strip())

#price = [name.split()[1] for name in stripped_tiernames if name.startswith("Pay")]
#print(price)

#Dictionary datastructure to store info
#tiers = {
#    "tier1": {
#        "price": 500,
#        "products": [
#            "name1",
#            "name2"
#        ]
#    },
#    "tier2": {
#        "price": 500,
#        "products": [
#            "name1",
#            "name2"
#        ]
#    }
#}
