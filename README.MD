# Chatbot Gemini - Práctico

Este proyecto es un chatbot en Python que utiliza la API de **Gemini (Google Generative AI)**.  
Permite interactuar en consola con diferentes roles relacionados a **entrenamiento, motivación y bienestar**.

---

## 🚀 Funcionalidades
- Memoria de conversación (guarda últimos mensajes del chat).
- Cambio dinámico de roles con el comando `:rol`.
- Reinicio de conversación con `:reset`.
- Salida del programa con `:salir`.
- Roles predefinidos:
  - 🏋️ Coach de Entrenamiento  
  - 💪 Coach Motivacional  
  - 🥗 Chef Fitness  
  - 🥑 Nutricionista  
  - 🧘 Mindfulness  
  - ⚕️ Médico Deportivo  

---

## 📂 Estructura del Proyecto
chatbot-gemini-practico/
─ config.py # Configuración y lectura de variables .env
─ memory.py # Manejo de la memoria de la conversación
─ prompts.py # Construcción de system prompts
─ roles.py # Definición de roles disponibles
─ llm_client.py # Cliente Gemini con reintentos
─ chat_service.py # Orquestador: integra memoria, roles y Gemini
─ main.py # Interfaz de consola
─ requirements.txt # Dependencias del proyecto
─ .env.example # Plantilla de variables de entorno
─ README.md # Documentación del proyecto