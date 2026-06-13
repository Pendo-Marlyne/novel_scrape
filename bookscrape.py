import requests
from bs4 import BeautifulSoup

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
        'price': price
    }

    all_scraped_books.append(book_item)

print(all_scraped_books)