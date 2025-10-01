# memory.py
from collections import deque
from typing import Deque, Dict, List

class ConversationMemory:
    """
    Memoria simple en cola: guarda últimos 12 turnos (usuario/modelo).
    Compatible con el formato de Gemini (role + parts).
    """
    def __init__(self, max_messages: int = 12):
        self._messages: Deque[Dict] = deque(maxlen=max_messages)

    def add_user(self, content: str):
        self._messages.append({"role": "user", "parts": [{"text": content}]})

    def add_model(self, content: str):
        self._messages.append({"role": "model", "parts": [{"text": content}]})

    def get(self) -> List[Dict]:
        return list(self._messages)

    def clear(self):
        self._messages.clear()
