import requests
import json

url = "https://zenquotes.io/api/random"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    quote = data[0]['q']
    author = data[0]['a']
    print(f'"{quote}" — {author}')
else:
    print(f"Error: {response.status_code}")
