# SageSpark Core

SageSpark Core is an original AI companion designed to provide helpful, honest and harmless assistance with a human‑like tone. It exposes a simple chat interface and stores useful memories (with user consent) so that conversations can continue over time. The system uses a **Python FastAPI backend** for the AI brain and a **Next.js frontend** for the user interface.

## Features
* **Three Modes:** Chatting, Coding and Thinking modes determine how the AI responds to different kinds of requests.
* **Hybrid Reasoning:** Incoming messages are passed through an intent detector, mode selector, memory retriever, safety checker and reasoning planner before a response is generated.
* **Memory System:** User conversations are stored (with permission) in JSON files. The memory system can be replaced with a database such as Supabase.
* **Frontend:** A simple React/Next.js interface with a text box and message display makes it easy to chat with the assistant.

## Project Structure
```
sagespark/
├─ README.md
├─ backend/
│  ├─ requirements.txt
│  └─ app/
│     ├─ __init__.py
│     ├─ main.py
│     ├─ brain.py
│     ├─ modes.py
│     ├─ memory.py
│     └─ safety.py
└─ frontend/
   ├─ package.json
   ├─ next.config.js
   └─ pages/
      ├─ index.js
      └─ api/
         └─ chat.js
```

## Running Locally

**Backend:** 
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Backend runs on port 8000 by default.

**Frontend:** 
```bash
npm install
npm run dev
```
Requires Node.js. During development the frontend proxies `/api/*` to localhost:8000.

## Note: The AI logic is stubbed

The AI logic in `brain.py` echoes messages. Replace `generate_response` with calls to a model API (OpenAI, Anthropic) or your own local model.
