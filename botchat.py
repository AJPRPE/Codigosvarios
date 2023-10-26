import nltk
from nltk.chat.util import Chat, reflections

# Configura las reglas de chat
pares = [
    [
        r"mi nombre es (.*)",
        ["Hola %1, ¿cómo puedo ayudarte hoy?"]
    ],
    [
        r"(¿Qué es|Explícame) (.*)",
        ["%2 es algo que puedes buscar en Internet."]
    ],
    [
        r"(Hola|Hola!)",
        ["¡Hola! ¿En qué puedo ayudarte?"]
    ],
    [
        r"(Adiós|Chao)",
        ["¡Hasta luego!"]
    ],
    [
        r"(.*)(ayuda|ayúdame|necesito ayuda)(.*)",
        ["Estoy aquí para ayudarte. ¿En qué puedo asistirte?"]
    ],

]

# Crea el chatbot
def chatbot():
    print("¡Hola! Soy un bot de chat. Puedes preguntarme cualquier cosa.")
    chat = Chat(pares, reflections)
    chat.converse()

if __name__ == "__main__":
    nltk.download('punkt')
    chatbot()
