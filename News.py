import requests
import json

query = input("What type of news are you interested in? ")
url = f" https://newsapi.org/v2/everything?q={query}&from=2024-10-07&sortBy=popularity&apiKey=1234e3e8024142ef92109e5761146432"
r = requests.get(url)
news = json.loads(r.text)
# print(news, type(news))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("--------------------------------------")
