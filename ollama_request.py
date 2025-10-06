#!/usr/bin/env python3
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

api = os.getenv('OLLAMA_API')

def sendRequest(query):
    if not query:
        raise ValueError("Query must contain at least one character.")

    payload = {
        "model": os.getenv('MODEL'),
        "messages": [{"role": "user", "content": query}],
    }
    response = requests.post(api, json=payload, stream=True)

    if response.status_code == 200:
        for line in response.iter_lines(decode_unicode=True):
            if line:
                try:
                    json_data = json.loads(line)
                    if "message" in json_data and "content" in json_data["message"]:
                        print(json_data["message"]["content"], end="")
                except json.JSONDecodeError:
                    print('failed')
        print()
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
