# llm_client.py
import google.generativeai as genai
from config import settings
import time

class GeminiClient:
    def __init__(self):
        genai.configure(api_key=settings.api_key)
        self.model = genai.GenerativeModel(settings.model)

    def generate(self, messages, max_retries=None):
        retries = 0
        max_retries = max_retries or settings.max_retries

        while retries < max_retries:
            try:
                chat = self.model.start_chat(history=messages)
                response = chat.send_message(
                    messages[-1]["parts"][0]["text"],  # último mensaje del usuario
                    request_options={"timeout": settings.timeout_seconds}
                )

                # ✅ forma correcta de acceder al texto
                if response and response.candidates:
                    return response.candidates[0].content.parts[0].text.strip()

                return "No recibí respuesta del modelo."
            except Exception as e:
                retries += 1
                print(f"[WARN] Error con Gemini (intento {retries}/{max_retries}): {e}")
                time.sleep(2)

        return "Lo siento, no pude procesar tu solicitud después de varios intentos."
