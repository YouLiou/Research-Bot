from google import genai
import sys

# 建議讓 API Key 透過 input 輸入，避免寫死在代碼中導致安全性檢查失敗
api_key = input("Please enter your Gemini API Key: ")

try:
    client = genai.Client(api_key=api_key)
    
    # Task 要求：Take user input and display LLM response
    user_question = input("\nAsk the AI a question: ")
    
    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents=user_question
    )

    print("\n--- AI Response ---")
    print(response.text)

except Exception as e:
    print(f"Error occurred: {e}")
    sys.exit(1)