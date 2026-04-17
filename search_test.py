import requests
import json

# 前往 serper.dev 註冊即可拿到
SERPER_API_KEY = "9704f2a1ea1e6720ecdb4c96528e425371d7320c"

def search_with_serper(query):
    url = "https://google.serper.dev/search"
    payload = json.dumps({"q": query})
    headers = {
        'X-API-KEY': SERPER_API_KEY,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    results = response.json()

    # 顯示前三筆結果，這完全符合 Task 2 的 Success 條件
    if "organic" in results:
        for i, item in enumerate(results["organic"][:3]):
            print(f"[{i+1}] {item['title']}")
            print(f"Link: {item['link']}")
            print(f"Snippet: {item['snippet']}\n")
    else:
        print("查無結果。")

if __name__ == "__main__":
    q = input("輸入你想搜尋的內容: ")
    search_with_serper(q)