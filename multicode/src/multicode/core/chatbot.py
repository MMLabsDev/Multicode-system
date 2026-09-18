"""Mia: chatbot muy simple (beta), migrado desde el script original.

El original tenía condiciones del tipo::

    elif user.lower() == "s" or "si":

que en Python siempre son verdaderas (un string no vacío como "si" ya es
verdadero por sí solo), sin importar lo que haya escrito el usuario. Aquí
se usan comparaciones explícitas contra una tupla de valores válidos.
"""

_RESPUESTAS_POR_PALABRA_CLAVE = {
    "gracias": "Un gusto :)",
    "que puedes hacer": (
        "Puedo detectar el código que me digas, traducir yo misma lo que "
        "quieras y asesorarte aquí en Multicode-System ;)"
    ),
    "como te llamas": "Me llamo Mia, soy la abreviación de 'Multicode Intelligent Assistant'.",
    "cual es tu nombre": "Me llamo Mia, soy la abreviación de 'Multicode Intelligent Assistant'.",
    "que es el lenguaje binario": (
        "El sistema binario es un sistema de numeración que utiliza únicamente "
        "dos dígitos: 0 y 1. Es la base de la informática moderna: los "
        "ordenadores procesan y almacenan información combinando estos dos "
        "dígitos, llamados bits. ¿Deseas hacer una traducción?"
    ),
}

_ACENTOS = {"í": "i", "ó": "o", "á": "a", "é": "e", "ú": "u"}


def _normalizar(texto: str) -> str:
    texto = texto.lower().strip()
    for acentuada, simple in _ACENTOS.items():
        texto = texto.replace(acentuada, simple)
    return texto


def responder(entrada: str) -> tuple[str, bool]:
    """Devuelve (mensaje_de_respuesta, continuar_conversacion)."""
    texto = _normalizar(entrada)

    if texto == "salir":
        return "Cerrando chatbot...", False

    if texto in ("adios", "adiós"):
        return "¿Quieres salir? Escribe 'salir' para cerrar, o sigue escribiendo si no.", True

    if "hola" in texto:
        return "¡Hola usuario!, sigo aquí, dime... ¿qué necesitas?", True

    if texto == "ascii":
        return "Sí, sé hablar ASCII también, dime, ¿qué quieres traducir?", True

    if texto == "binario":
        return "Sí, sé hablar Binario también, dime, ¿qué quieres traducir?", True

    for clave, respuesta in _RESPUESTAS_POR_PALABRA_CLAVE.items():
        if clave in texto:
            return respuesta, True

    return "Ehh... lo siento, no entiendo eso aún.", True
