import requests
from config import YANDEXGPT_API_KEY, YANDEX_FOLDER_ID

def call_yandexgpt(system_prompt: str, user_query: str) -> str:
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Authorization": f"Api-Key {YANDEXGPT_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "modelUri": f"gpt://{YANDEX_FOLDER_ID}/yandexgpt-lite/latest",
        "completionOptions": {
            "temperature": 0.3,
            "maxTokens": "500"
        },
        "messages": [
            {"role": "system", "text": system_prompt},
            {"role": "user", "text": user_query}
        ]
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()["result"]["alternatives"][0]["message"]["text"]
        else:
            return f"Ошибка LLM: {response.status_code}, {response.text}"
    except Exception as e:
        return f"Ошибка подключения к LLM: {str(e)}"