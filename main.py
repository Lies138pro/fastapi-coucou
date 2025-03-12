from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Coucou"}

@app.post("/send-message")
def send_message(msg: Message):
    return {"response": f"Tu as envoyé : {msg.text}"}