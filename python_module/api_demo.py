import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

try:
    response = requests.get(url)
    response.raise_for_status()  # 若失敗會丟出錯誤

    data = response.json()
    print("任務 ID:", data["id"])
    print("標題:", data["title"])
    print("是否完成:", "✅" if data["completed"] else "❌")

except requests.exceptions.RequestException as e:
    print("⚠️ 發生錯誤：", e)
