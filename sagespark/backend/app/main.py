from fastapi import FastAPI
from pydantic import BaseModel
from .brain import generate_response
from .modes import detect_mode

app = FastAPI()

class Message(BaseModel):
    user_id: str
    content: str
    mode: str | None = None

@app.post("/chat")
async def chat_endpoint(message: Message):
    """
    Chat endpoint. Accepts user_id, content and optional mode.
    Determines mode if not provided, generates response and returns it.
    """
    mode = message.mode or detect_mode(message.content)
    response = generate_response(message.user_id, message.content, mode)
    return {"mode": mode, "response": response}
