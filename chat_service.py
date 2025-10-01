# chat_service.py
from typing import Optional
from config import settings
from memory import ConversationMemory
from prompts import build_system_prompt, collapse_history
from roles import RolesPresent, ROLES_SYSTEM_PROMPT
from llm_client import GeminiClient

class ChatService:
    def __init__(self, role: RolesPresent = RolesPresent.MOTIVACIONAL):
        self.client = GeminiClient()
        self.memory = ConversationMemory(max_messages=settings.max_history_messages)
        self.role = role

    def set_role(self, role: RolesPresent):
        """Cambia el rol activo del chatbot"""
        if role in ROLES_SYSTEM_PROMPT:
            self.role = role
            print(f"[INFO] Rol cambiado a: {role.value}")
        else:
            print(f"[WARN] Rol {role} no está definido, se mantiene el actual.")

    def reset(self):
        """Reinicia la memoria de la conversación"""
        self.memory.clear()
        print("[INFO] Memoria de conversación reiniciada.")

    def ask(self, user_message: str) -> str:
        """Procesa un mensaje del usuario y devuelve la respuesta del modelo"""
        self.memory.add_user(user_message)

        role_instructions = ROLES_SYSTEM_PROMPT[self.role]
        system_prompt = build_system_prompt(role_instructions)

        # Historial de mensajes + prompt inicial
        # Ahora (correcto para Gemini)
        history = [{"role": "user", "parts": [{"text": system_prompt}]}] + collapse_history(self.memory.get())


        response = self.client.generate(history)

        self.memory.add_model(response)
        return response
