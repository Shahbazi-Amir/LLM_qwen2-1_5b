# English comments only

from fastapi import FastAPI
from pydantic import BaseModel
import requests

# create FastAPI app
app = FastAPI()

LLAMA_SERVER_URL = "http://127.0.0.1:8080/completion"


@app.get("/ping")
def ping():
    return {"status": "ok"}


class ChatRequest(BaseModel):
    prompt: str


@app.post("/chat")
def chat(req: ChatRequest):
    payload = {
        "prompt": req.prompt,
        "n_predict": 200
    }
    r = requests.post(LLAMA_SERVER_URL, json=payload, timeout=60)
    return r.json()
