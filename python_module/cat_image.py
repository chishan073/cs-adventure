import requests

# API 端點
url = "https://api.thecatapi.com/v1/images/search"

# 發送 GET 請求
response = requests.get(url)

# 解析 JSON 回應
if response.status_code == 200:
    data = response.json()
    image_url = data[0]["url"]
    print("🐱 Here's a random cat image:")
    print(image_url)
else:
    print("⚠️ 無法取得圖片，請檢查網路或 API 狀態")

# 下載圖片並存成 cat.jpg
img_data = requests.get(image_url).content
with open('cat.jpg', 'wb') as f:
    f.write(img_data)
    print("✅ 已儲存圖片為 cat.jpg")
