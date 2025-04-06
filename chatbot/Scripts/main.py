from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# ✅ Add proper CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict to your frontend URL later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "Hello from FastAPI"}

@app.post("/chat")
def chat_endpoint(msg: Message):
    print("Received message:", msg.message)
    return {"response": f"You asked about: {msg.message}. Here's a helpful response."}
