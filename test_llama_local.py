import requests

url = "http://127.0.0.1:8080/completion"

payload = {
    "prompt": "سلام خوبی؟",
    "n_predict": 80
}

res = requests.post(url, json=payload)
print(res.json())
