import requests

# 請改成你自己的 API 金鑰
API_KEY = "AIzaSyCr-yS_-UfTrpBXXXtaTuEddnZekgLyyvI"
SEARCH_QUERY = "Python tutorial"
MAX_RESULTS = 5

url = "https://www.googleapis.com/youtube/v3/search"

params = {
    "part": "snippet",
    "q": SEARCH_QUERY,
    "type": "video",
    "maxResults": MAX_RESULTS,
    "key": API_KEY
}

response = requests.get(url, params=params)
data = response.json()

for item in data["items"]:
    title = item["snippet"]["title"]
    video_id = item["id"]["videoId"]
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    print(f"🎬 {title}\n🔗 {video_url}\n")
