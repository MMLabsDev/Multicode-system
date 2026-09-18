def encode(text: str) -> str:

    unicode_text = ""

    for letra in text:
        unicode_text += f"U+{ord(letra):04X} "

    return unicode_text.strip()


def decode(text: str) -> str:

    traduccion = ""

    for char in text.split():
        codigo = char.replace("U+", "")
        traduccion += chr(int(codigo, 16))

    return traduccion