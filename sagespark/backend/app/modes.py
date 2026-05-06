# Definitions of possible modes
CHAT_MODE = "chat"
CODE_MODE = "code"
THINK_MODE = "think"

def detect_mode(content: str) -> str:
    """
    Simple heuristic to detect the mode based on keywords.
    Replace with a real intent classifier if needed.
    """
    lowered = content.lower()
    if any(keyword in lowered for keyword in ["def ", "class ", "function ", "code", "script"]):
        return CODE_MODE
    if any(keyword in lowered for keyword in ["think", "plan", "idea", "reason"]):
        return THINK_MODE
    return CHAT_MODE
