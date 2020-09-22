#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

url="https://www.humblebundle.com/games/better-futures?hmb_source=navbar&hmb_medium=product_tile&hmb_campaign=tile_index_7"
req = requests.get(url).text

#open a CSV file to write to
csv_file = open('HumbleBunder_Scrape.csv', 'w')
csv_writer = csv.writer(csv_file)

soup = BeautifulSoup(req, 'html.parser')
#print(soup.prettify().encode("utf-8"))
#print(soup.title)


#get tiernames and add to csv
#Bundle tiers class: (price and tier)
tier_headlines = soup.select(".dd-header-headline")
#print (tier_headlines)
stripped_tier_headlines = []
for tier in tier_headlines:
    stripped_tier_headlines.append(tier.text.strip())
    print(tier.text.strip())
csv_writer.writerow(stripped_tier_headlines)


#General tiers
tiers = soup.select(".dd-game-row")
#print(tiers)
all_products = []
for tier in tiers:
    #Product Names
    product_names = tier.select(".front-page-art-image-text")
    stripped_product_names = []
    for product in product_names:
        stripped_product_names.append(product.text.strip())
    print(stripped_product_names)
    all_products.append(stripped_product_names)

df = pd.DataFrame(list(zip(*all_products))).add_prefix('Col')
df.to_csv('file.csv', index=False)
#csv_writer.writerows(ans)
#price = [name.split()[1] for name in stripped_tiernames if name.startswith("Pay")]
#print(price)

csv_file.close()
