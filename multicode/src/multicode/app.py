"""Orquestador principal.

Antes, `cli/` (presentación) y `core/`+`codecs/` (lógica) existían por
separado sin nada que los conectara: no había ningún punto de entrada real
que tomara la opción elegida en el menú y la pasara al traductor. Este
módulo es ese punto de unión.
"""

from multicode.cli.menu import menu
from multicode.cli.tables import crear_tabla
from multicode.core.chatbot import responder
from multicode.core.detector import detectar
from multicode.core.translator import DecodeError, EncodeError, decode, encode

try:
    import pyperclip

    _CLIPBOARD_DISPONIBLE = True
except ImportError:
    _CLIPBOARD_DISPONIBLE = False


CODEC_POR_OPCION = {
    "1": "ascii",
    "2": "binary",
    "3": "base64",
    "4": "hexadecimal",
    "5": "unicode",
}

SUBMENU = [
    (" [1]", "Codificar (texto → código)"),
    (" [2]", "Decodificar (código → texto)"),
    (" [3]", "Regresar"),
]


def _copiar_si_se_quiere(resultado: str) -> None:
    respuesta = input("\n¿Copiar al portapapeles? (s/n): ").strip().lower()
    if respuesta != "s":
        return
    if _CLIPBOARD_DISPONIBLE:
        pyperclip.copy(resultado)
        print("Copiado ✓")
    else:
        print("pyperclip no está instalado; no se pudo copiar.")


def _menu_codec(codec: str) -> None:
    while True:
        crear_tabla(SUBMENU)
        opcion = input("#: ").strip()

        if opcion == "1":
            texto = input("Texto: ")
            try:
                resultado = encode(texto, codec)
            except EncodeError as error:
                print(f"Error: {error}")
                continue
            print(f"{codec.capitalize()}: {resultado}")
            _copiar_si_se_quiere(resultado)

        elif opcion == "2":
            codigo = input(f"{codec.capitalize()}: ")
            try:
                resultado = decode(codigo, codec)
            except DecodeError as error:
                print(f"Error: {error}")
                continue
            print(f"Traducción: {resultado}")
            _copiar_si_se_quiere(resultado)

        elif opcion == "3":
            break

        else:
            print("Opción inválida ✕")


def _menu_detector() -> None:
    print("\nEscribe 'salir' para volver al menú principal.")
    while True:
        texto = input("Ingrese el código: ")
        if texto.strip().lower() == "salir":
            break
        print("Formato detectado:", detectar(texto))
        print("El detector puede cometer errores.")


def _menu_chatbot() -> None:
    print("Así que dime...")
    while True:
        entrada = input("En qué te puedo ayudar? ")
        salida, continuar = responder(entrada)
        print(salida)
        if not continuar:
            break


def run() -> None:
    while True:
        opcion = menu().strip()

        if opcion in CODEC_POR_OPCION:
            _menu_codec(CODEC_POR_OPCION[opcion])
        elif opcion == "6":
            _menu_detector()
        elif opcion == "7":
            _menu_chatbot()
        elif opcion == "8":
            print("Cerrando Multicode-System...")
            break
        else:
            print("Opción inválida ✕")


if __name__ == "__main__":
    run()
