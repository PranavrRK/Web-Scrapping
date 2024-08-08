import requests
from bs4 import BeautifulSoup
import pandas as pd
current_page = 1

url = "https://webscraper.io/test-sites/e-commerce/allinone"

page = requests.get(url)

soup = BeautifulSoup(page.text , 'html.parser')

proceed = True

all_items = []
while(proceed):
    
    if soup.title.text == "404 Not Found":
        proceed = False

    else:
        all_products = soup.find_all("div",class_="thumbnail")
        for product in all_products:

            items ={}

            items['Title'] = product.find("a",class_="title").text
            items['Price'] = product.find("h4",class_="price float-end card-title pull-right").text
            items["Specifications"] = product.find("p",class_="description card-text").text
            items["Reviews"] = product.find("p",class_ = "review-count float-end").text
            stars = product.find_all("span", class_="ws-icon ws-icon-star")
            items["Rating"] = len(stars)
            
            all_items.append(items)
    
    current_page += 1
    proceed = False

data = pd.DataFrame(all_items)
data.to_excel("web_scraping.xlsx", index=False)
print("Data has been saved to web_scraping.xlsx")
print(data)