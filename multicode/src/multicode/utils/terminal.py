import time


def escribir(texto, velocidad=0.01):
    for caracter in texto:
        print(caracter, end="", flush=True)
        time.sleep(velocidad)

    print()