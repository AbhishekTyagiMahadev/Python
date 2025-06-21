import requests
response = requests.get("https://www.google.com")
# print(response.text)

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
print(response.text)

data = {
    "title": 'Abhishek',
    "body": 'Hii, How are you.',
    "userId": 12,
  }
headers =  {
    'Content-type': 'application/json; charset=UTF-8',
  }
response = requests.post(url, headers=headers, json=data)

print(response.text)
