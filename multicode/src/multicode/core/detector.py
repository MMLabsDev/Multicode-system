"""Detector heurístico de formato (beta).

Migrado desde el script original. La versión previa tenía un bug real:
comprobaba si cada carácter estaba "en" el string literal de un patrón de
regex (p. ej. ``c in r'^[A-Za-z0-9+/]+={0,2}$'``), lo cual nunca evalúa
la regex — solo compara contra los caracteres sueltos del patrón. Aquí se
usan expresiones regulares reales con ``re.fullmatch``.

Nota: la detección es heurística y ambigua por naturaleza (p. ej. "72 101"
podría ser tanto ASCII como una casualidad numérica). El orden de los
chequeos importa: se va de lo más específico a lo más genérico.
"""

import re

_UNICODE_MARCADOR = "U+"
_BINARIO = re.compile(r"[01\s]+")
_ASCII = re.compile(r"[0-9\s]+")
_HEXADECIMAL = re.compile(r"[0-9A-Fa-f\s]+")
_BASE64 = re.compile(r"[A-Za-z0-9+/]+={0,2}")


def detectar(texto: str) -> str:
    """Intenta adivinar en qué formato está codificado ``texto``."""
    texto = texto.strip()

    if not texto:
        return "Texto normal"

    if _UNICODE_MARCADOR in texto:
        return "Unicode"

    if _BINARIO.fullmatch(texto):
        return "Binario"

    if _ASCII.fullmatch(texto):
        return "ASCII"

    if _HEXADECIMAL.fullmatch(texto):
        return "Hexadecimal"

    if _BASE64.fullmatch(texto):
        return "Base64"

    return "Texto normal"
