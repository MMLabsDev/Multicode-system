import base64


def encode(text: str) -> str:
    #"""Convierte texto a Base64."""
    return base64.b64encode(text.encode()).decode()


def decode(text: str) -> str:
    #"""Convierte Base64 a texto."""
    return base64.b64decode(text).decode()