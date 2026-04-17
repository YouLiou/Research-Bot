from google import genai
from google.genai import types
import requests
import json

# 1. 設定你的 API 金鑰
GEMINI_API_KEY = "AIzaSyD5Hl17j--TviLAhwR0k7gC-in3Hx-NP5Q"
SERPER_API_KEY = "9704f2a1ea1e6720ecdb4c96528e425371d7320c"

client = genai.Client(api_key=GEMINI_API_KEY)

# 2. 定義搜尋工具函式 (這就是 AI 的「眼睛」)
def search_web(query: str):
    """當使用者問的問題需要最新資訊或 AI 不知道的事情時，呼叫此工具進行網路搜尋。"""
    url = "https://google.serper.dev/search"
    payload = json.dumps({"q": query})
    headers = {
        'X-API-KEY': SERPER_API_KEY,
        'Content-Type': 'application/json'
    }
    
    print(f"\n[系統動作]：AI 正在搜尋 '{query}'...")
    response = requests.request("POST", url, headers=headers, data=payload)
    results = response.json()
    
    # 只回傳前 3 筆有機搜尋結果的摘要給 AI
    snippets = []
    if "organic" in results:
        for item in results["organic"][:3]:
            snippets.append(f"標題: {item.get('title')}\n內容: {item.get('snippet')}")
    
    return "\n\n".join(snippets) if snippets else "找不到相關搜尋結果。"

# 3. 建立工具清單
tools = [search_web]

def run_research_bot():
    print("--- 🤖 智慧型研究機器人 (Agent) 已上線 ---")
    user_query = input("請輸入您的研究問題：")

    # 4. 核心邏輯：讓 AI 決定是否使用工具
    # 我們開啟 'tools' 並設定 automatic_function_calling
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=user_query,
        config=types.GenerateContentConfig(
            tools=tools,
            automatic_function_calling_cb=None # 設為 None 代表讓 SDK 自動處理呼叫
        )
    )

    print("\n--- 📝 AI 研究總結 ---")
    print(response.text)

if __name__ == "__main__":
    run_research_bot()