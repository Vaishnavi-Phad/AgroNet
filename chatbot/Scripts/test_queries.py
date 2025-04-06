import os
import json
import requests

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "sample_farming_queries.json")

with open(file_path, "r") as f:
    queries = json.load(f)

for q in queries:
    response = requests.post("http://127.0.0.1:8000/chat", json={"message": q["user"]})
    try:
        print("User:", q["user"])
        print("Bot:", response.json()["response"])
    except KeyError:
        print("Full API response:", response.json())
        print("Failed to parse response: 'response'")
        print("Raw response text:", response.text)
    print("-" * 50)
