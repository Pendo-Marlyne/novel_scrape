import requests
from bs4 import BeautifulSoup
import pandas as pd 
url = "http://books.toscrape.com/index.html"

response = requests.get(url)
all_scraped_books = []
print(response.status_code)

 #print(response.content)

soup = BeautifulSoup(response.content, 'html.parser')
print(soup.prettify())
cards = soup.select('article.product_pod')
#print(cards[0]) #prints the first card
for card in cards:
    title = card.select_one('h3 a').text
    price = card.select_one('p.price_color').text
    # print(f"{title} - {price}")

    book_item ={
        'title': title,
        'price': price.replace('£', '')
    }

    all_scraped_books.append(book_item)

df = pd.DataFrame(all_scraped_books)
df.to_csv("scraped_books.csv" ,index=False) #to save the data to a csv file
print(df.head())
df.to_excel("scraped_books.xlsx", index=False) #to save the data to an excel file
print(df.head())