# use newsapi to get the top headlines for the US and print the title of each article

import requests

query = input("what do you want to search for? ")
news = requests.get(f'https://newsapi.org/v2/everything?q={query}&apiKey=YOUR_API_KEY')

r = news.json()
articles = r['articles']
for article in articles:
    print(article['title'])

    

