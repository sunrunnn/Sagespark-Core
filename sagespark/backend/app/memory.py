import json
from pathlib import Path
from typing import List, Dict

# store data in ./backend/data
DATA_DIR = Path(__file__).resolve().parent / ".." / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

def _get_user_file(user_id: str) -> Path:
    return DATA_DIR / f"{user_id}.json"

def store_interaction(user_id: str, message: Dict[str, str]) -> None:
    """Append a message to the user's conversation history."""
    file_path = _get_user_file(user_id)
    history = []
    if file_path.exists():
        history = json.loads(file_path.read_text())
    history.append(message)
    file_path.write_text(json.dumps(history, indent=2))

def retrieve_recent(user_id: str, limit: int = 20) -> List[Dict[str, str]]:
    """Retrieve the most recent interactions for context."""
    file_path = _get_user_file(user_id)
    if not file_path.exists():
        return []
    history = json.loads(file_path.read_text())
    return history[-limit:]
