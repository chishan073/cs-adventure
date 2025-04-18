import requests

url = "https://cataas.com/cat/says/Hi"
response = requests.get(url)

with open("hi_cat.jpg", "wb+") as f:
    f.write(response.content)

print("🐱 hi_cat.jpg 已建立（使用 wb+）")