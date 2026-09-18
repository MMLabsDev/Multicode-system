from multicode.cli.tables import crear_tabla

LOGO = r"""
███╗   ███╗███╗   ███╗██╗      █████╗ ██████╗ ███████╗
████╗ ████║████╗ ████║██║     ██╔══██╗██╔══██╗██╔════╝
██╔████╔██║██╔████╔██║██║     ███████║██████╔╝███████╗
██║╚██╔╝██║██║╚██╔╝██║██║     ██╔══██║██╔══██╗╚════██║
██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║██████╔╝███████║
╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
             MULTICODE-SYSTEM • V3.0
                         by M.MLabs.Dev
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

OPCIONES_PRINCIPALES = [
    (" [1]", "ASCII"),
    (" [2]", "Binario"),
    (" [3]", "Base64"),
    (" [4]", "Hexadecimal"),
    (" [5]", "Unicode"),
    (" [6]", "Detector de código (Beta)"),
    (" [7]", "Chatbot"),
    (" [8]", "Cerrar Programa"),
]


def menu() -> str:
    """Muestra el logo y la tabla de opciones, y devuelve la selección del usuario."""
    print(LOGO)
    crear_tabla(OPCIONES_PRINCIPALES)
    return input("\nSelecciona una opción: ")
