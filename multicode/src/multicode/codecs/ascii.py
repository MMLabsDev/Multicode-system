def encode(text: str) -> str:
    """Convierte texto a valores ASCII separados por espacios."""
    ascii_text = ""
    for char in text:
        ascii_text += str(ord(char)) + " "
    return ascii_text.strip()


def decode(ascii_text: str) -> str:
    """Convierte valores ASCII separados por espacios a texto."""
    numbers = ascii_text.split()
    text = ""
    for number in numbers:
        text += chr(int(number))
    return text
