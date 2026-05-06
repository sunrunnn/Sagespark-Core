from .memory import store_interaction, retrieve_recent
from .safety import check_safety
from .modes import CHAT_MODE, CODE_MODE, THINK_MODE

def generate_response(user_id: str, content: str, mode: str) -> str:
    """
    Generate a response given user_id, content and mode.
    This is a stub that simply echoes the input.
    Replace with integration to a language model of your choice.
    """
    if not check_safety(content):
        return "I'm sorry, but I can't assist with that request."

    history = retrieve_recent(user_id)

    # simple mode-based responses
    if mode == CODE_MODE:
        response = f"Let's work through the code question: {content}"
    elif mode == THINK_MODE:
        response = f"Here's my thought process: {content}"
    else:
        response = f"I understand. {content}"

    store_interaction(user_id, {"role": "user", "content": content})
    store_interaction(user_id, {"role": "assistant", "content": response})

    return response
