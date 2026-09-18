from multicode.codecs import ascii as ascii_codec
from multicode.codecs import binary
from multicode.codecs import base64 as base64_codec
from multicode.codecs import hexadecimal
from multicode.codecs import unicode as unicode_codec


class EncodeError(Exception):
    """Se lanza cuando un texto no puede codificarse con el codec pedido."""


class DecodeError(Exception):
    """Se lanza cuando un código no puede decodificarse a texto original."""


CODECS = {
    "ascii": ascii_codec,
    "binary": binary,
    "hexadecimal": hexadecimal,
    "base64": base64_codec,
    "unicode": unicode_codec,
}


def encode(text: str, codec: str) -> str:
    if codec not in CODECS:
        raise EncodeError(f"Codec desconocido: {codec!r}")
    try:
        return CODECS[codec].encode(text)
    except Exception as error:
        raise EncodeError(f"No se pudo codificar con {codec}: {error}") from error


def decode(text: str, codec: str) -> str:
    if codec not in CODECS:
        raise DecodeError(f"Codec desconocido: {codec!r}")
    try:
        return CODECS[codec].decode(text)
    except Exception as error:
        raise DecodeError(f"Entrada inválida para {codec}: {error}") from error
