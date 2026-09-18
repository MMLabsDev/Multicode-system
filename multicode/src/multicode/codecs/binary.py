def encode(text: str) -> str:
    #"""Convierte texto a binario."""

    binary_text = ""

    for char in text:
        binary_text += format(ord(char), "08b") + " "

    return binary_text.strip()


def decode(binary_text: str) -> str:
    #"""Convierte binario a texto."""

    numbers = binary_text.split()
    text = ""

    for number in numbers:
        text += chr(int(number, 2))

    return text