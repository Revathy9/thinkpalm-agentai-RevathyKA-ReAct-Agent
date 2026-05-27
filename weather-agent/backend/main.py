import os
import json
from fastapi import FastAPI
from pydantic import BaseModel
from agents.coordinator import CoordinatorAgent
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

agent = CoordinatorAgent()

class ChatRequest(BaseModel):

    message: str

from fastapi.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
def home():
    backend_dir = os.path.dirname(os.path.abspath(__file__))
    index_path = os.path.join(backend_dir, "index.html")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as file:
            return HTMLResponse(content=file.read())
    return HTMLResponse(content="<h1>Agentic AI Backend Running (index.html not found)</h1>")


@app.get("/memory")
def get_memory():
    backend_dir = os.path.dirname(os.path.abspath(__file__))
    memory_path = os.path.join(backend_dir, "memory.json")
    if os.path.exists(memory_path):
        try:
            with open(memory_path, "r") as file:
                return json.load(file)
        except Exception:
            return {}
    return {}

@app.post("/chat")
def chat(request: ChatRequest):

    result = agent.process(request.message)

    return {
        "response": result
    }

