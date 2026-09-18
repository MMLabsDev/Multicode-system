import time
def crear_tabla(opciones):
    # ─────────────────────────────────────
    # Calcular el ancho de cada columna
    # ─────────────────────────────────────

    ancho_funcion = max(
        len("Función"),
        max(len(funcion) for funcion, _ in opciones)
    )

    ancho_herramienta = max(
        len("Herramienta"),
        max(len(herramienta) for _, herramienta in opciones)
    )

    # Espacios internos
    ancho_funcion += 2
    ancho_herramienta += 2

    # ─────────────────────────────────────
    # Bordes
    # ─────────────────────────────────────

    superior = (
        "╔" +
        "═" * ancho_funcion +
        "╦" +
        "═" * ancho_herramienta +
        "╗"
    )

    separador = (
        "╠" +
        "═" * ancho_funcion +
        "╬" +
        "═" * ancho_herramienta +
        "╣"
    )

    inferior = (
        "╚" +
        "═" * ancho_funcion +
        "╩" +
        "═" * ancho_herramienta +
        "╝"
    )

    # ─────────────────────────────────────
    # Tabla
    # ─────────────────────────────────────

    print(superior)

    print(
        f"║ {'Función':<{ancho_funcion - 1}}"
        f"║ {'Herramienta':<{ancho_herramienta - 1}}║"
    )

    print(separador)

    for funcion, herramienta in opciones:
        print(
            f"║ {funcion:<{ancho_funcion - 1}}"
            f"║ {herramienta:<{ancho_herramienta - 1}}║"
        )

        time.sleep(0.05)

    print(inferior)