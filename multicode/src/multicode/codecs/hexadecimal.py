def encode(text: str) -> str:
    #"""Convierte texto a hexadecimal."""
    return text.encode("utf-8").hex()


def decode(hexadecimal: str) -> str:
    #"""Convierte hexadecimal a texto."""
    return bytes.fromhex(hexadecimal).decode("utf-8")