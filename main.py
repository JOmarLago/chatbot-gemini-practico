# main.py
from chat_service import ChatService
from roles import RolesPresent

def mostrar_roles():
    print("\nRoles disponibles:")
    for role in RolesPresent:
        print(f"- {role.value}")
    print()

def main():
    print("=== Chatbot Gemini - Práctico ===")
    print("Comandos: :rol, :reset, :salir\n")

    chat = ChatService(role=RolesPresent.MOTIVACIONAL)  # rol por defecto
    mostrar_roles()

    while True:
        user_input = input("Tú: ").strip()

        if not user_input:
            continue

        if user_input.startswith(":"):
            comando = user_input[1:].lower()

            if comando == "salir":
                print("👋 ¡Chau! Nos vemos pronto.")
                break

            elif comando == "reset":
                chat.reset()

            elif comando == "rol":
                mostrar_roles()
                nuevo_rol = input("Elegí un rol: ").strip().lower()
                try:
                    role_enum = RolesPresent(nuevo_rol)
                    chat.set_role(role_enum)
                except ValueError:
                    print(f"[WARN] Rol '{nuevo_rol}' no existe.")

            else:
                print(f"[WARN] Comando desconocido: {comando}")

        else:
            respuesta = chat.ask(user_input)
            print(f"🤖 {respuesta}\n")

if __name__ == "__main__":
    main()
