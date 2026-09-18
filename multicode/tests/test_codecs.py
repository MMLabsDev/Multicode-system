import pytest

from multicode.codecs import ascii as ascii_codec
from multicode.codecs import base64 as base64_codec
from multicode.codecs import binary
from multicode.codecs import hexadecimal
from multicode.codecs import unicode as unicode_codec
from multicode.core.detector import detectar
from multicode.core.translator import DecodeError, EncodeError, decode, encode

CODECS_A_PROBAR = [ascii_codec, binary, base64_codec, hexadecimal, unicode_codec]


@pytest.mark.parametrize("codec", CODECS_A_PROBAR)
def test_round_trip(codec):
    texto = "Hola Mundo"
    codificado = codec.encode(texto)
    assert codec.decode(codificado) == texto


def test_translator_encode_decode():
    resultado = encode("Hola", "binary")
    assert decode(resultado, "binary") == "Hola"


def test_translator_codec_desconocido():
    with pytest.raises(EncodeError):
        encode("Hola", "morse")


def test_translator_decode_invalido():
    with pytest.raises(DecodeError):
        decode("esto no es binario valido", "binary")


@pytest.mark.parametrize(
    "texto, esperado",
    [
        ("U+0048 U+006F", "Unicode"),
        ("01001000 01101111", "Binario"),
        ("72 111", "ASCII"),
        ("48 6f", "Hexadecimal"),
        ("SG9sYQ==", "Base64"),
        ("Hola Mundo", "Texto normal"),
    ],
)
def test_detectar(texto, esperado):
    assert detectar(texto) == esperado
