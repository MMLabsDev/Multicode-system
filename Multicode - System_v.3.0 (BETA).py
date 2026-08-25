#importar librerías.......................................................
import base64
import time
import random
import os
import re
import pyperclip
#-------------------------------------------------------------------------
def menu():
    print("""
███╗   ███╗███╗   ███╗██╗      █████╗ ██████╗ ███████╗®
████╗ ████║████╗ ████║██║     ██╔══██╗██╔══██╗██╔════╝
██╔████╔██║██╔████╔██║██║     ███████║██████╔╝███████╗
██║╚██╔╝██║██║╚██╔╝██║██║     ██╔══██║██╔══██╗╚════██║
██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║██████╔╝███████║
╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        MULTICODE-SYSTEM • V3.0 "BETA"
          by M.MLabs.Dev
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

menu()

    #--------------------------------------
    # funciones
    #--------------------------------------
def escribir(texto, velocidad=0.01):
    for caracter in texto:
        print(caracter, end="", flush=True)
        time.sleep(velocidad)
    print()


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


# ─────────────────────────────────────────────
# Opciones
# ─────────────────────────────────────────────

opciones = [
    (" [1]", "ASCII"),
    (" [2]", "Binario"),
    (" [3]", "Base64"),
    (" [4]", "Hexadecimal"),
    (" [5]", "Unicode"),
    (" [6]", "Detector de código (Beta)"),
    (" [7]", "Chatbot"),
    (" [8]", "Cerrar Programa")
]
# ─────────────────────────────────────────────
# Título
# ─────────────────────────────────────────────
option_ascii =[
("  [1]","Español - ASCII"),
("  [2]","ASCII - Español"),
("  [3]","Regresar")]
#tabla de binario----------------------------------------------------------------
option_bin = [
("  [1]","Español - Binario"),
("  [2]","Binario - Español"),
("  [3]","Regresar")
]
#tabla hexadecimal---------------------------------------------------------------
option_hex = [
("  [1]","Epañol - Hexadecimal"),
("  [2]","Hexadecimal - Español"),
("  [3]","Regresar")]
#tabla Unicode---------------------------------------------------------------
option_uni = [
("  [1]","Epañol - Unicode"),
("  [2]","Unicode - Español"),
("  [3]","Regresar")]
#Tabla base64---------------------------------------------------------------
option_base = [
("  [1]","Español - Base64"),
("  [2]","Base64 - Español"),
("  [2]","Regresar")]
#tabla Chatbot--------------------------------------------------------------
chat_menu = [
("[italic]Multicode Intelligent Assistant[/italic]"),
("Hola Usuario!, soy Mia (Multicode intelligent Assistant), Estoy aquí para ayudarte con tus dudas, de momento soy una versión beta, así que de momento no esperes demasiado de mí. Si queres salir de la conversación solo dime 'salir' que yo te entenderé")]
#Crear funciones..................................................................................................................................................

def limpiar():
    os.system("cls")
    
def palabra_a_ASCII():
    palabra = input("Texto: ")

    ascii_texto = ""

    for letra in palabra:
        ascii_texto += str(ord(letra)) + " "

    print("ASCII:", ascii_texto)

    return ascii_texto

def ASCII_a_palabra():
    codigo_ascii = input("ASCII: ")

    numeros = codigo_ascii.split()
    traduccion = ""

    for n in numeros:
        traduccion += chr(int(n))

    print("Traducción: ", traduccion)

    return traduccion

def Palabra_a_Binario():
    traduccion = input("Texto: ")
    traduccion_bin = ""

    for letra in traduccion:
        traduccion_bin += format(ord(letra),"08b") + " "

    print("Binario: ", traduccion_bin)

    return traduccion_bin

def Binario_a_Palabra():
    binario = input("Binario: ")
    traduccion = ""
    for b in binario.split():
            traduccion += chr(int(b, 2))

    print("Traducción: ",traduccion)
    return traduccion

def palabra_a_hexadecimal():
    texto = input("Texto: ")

    hexadecimal = texto.encode("utf-8").hex()

    print("Hexadecimal: ", hexadecimal)
    return hexadecimal

def hexadecimal_a_palabra():
    texto = input("Hexadecimal: ")

    palabra = bytes.fromhex(texto).decode("utf-8")

    print("Traducción: ", palabra)
    return palabra

def palabra_a_base64():
    texto = input("Texto: ")

    codificado = base64.b64encode(texto.encode()).decode()

    print(codificado)
    return codificado

def base64_a_palabra():
    texto = input("Base64: ")

    original = base64.b64decode(texto).decode()

    print(original)
    return original

def palabra_a_unicode():
    texto = input("Texto: ")

    unicode_texto = ""

    for letra in texto:
        unicode_texto += f"U+{ord(letra):04X} "

    print("Unicode:", unicode_texto)
    return unicode_texto

def unicode_a_palabra():
    texto = input("Unicode: ")

    traduccion = ""

    for codigo in texto.split():
        codigo = codigo.replace("U+", "")
        traduccion += chr(int(codigo, 16))

    print("Traducción:", traduccion)
    return traduccion

def detectar(texto):


    if "U+" in texto:
        return "Unicode"

    elif set(texto) <= {"0","1"," "}:
        return "Binario"

    elif all(c in "0123456789 " for c in texto):
        return "ASCII"

    elif all(c in "0123456789ABCDEFabcdef" for c in texto):
        return "Hexadecimal"

    elif all(c in r'^[A-Za-z0-9+/]+={0,2}$' for c in texto):
        return "Base 64"

    else:
        return "Texto normal"


#Sistema ---------------------------------------------------------------------
while True:
    limpiar()
    menu()
    crear_tabla(opciones)
    
    try:
        seleccion = int(input("Seleccione función: "))

        if seleccion == 1:
            crear_tabla(option_ascii)

            while True:
                funcion = int(input("#:"))

                if funcion == 1:
                    resultado = palabra_a_ASCII()
                    option = input("\n¿Copiar? (s/n): ")

                    if option.lower() == "s":
                        pyperclip.copy(resultado)
                        print("Copiado✓")

                    elif option.lower() == "n":
                        continue
                    
                elif funcion == 2:
                    traduccion = ASCII_a_palabra()
                    option = input("\n¿Copiar? (s/n): ")
                    if option.lower() == "s":
                        pyperclip.copy(traduccion)
                        print("Copiado✓")

                    elif option.lower() == "n":
                        continue
                    
                elif funcion == 3:
                    limpiar()
                    crear_tabla(opciones)
                    break


        elif seleccion == 2:
            crear_tabla(option_bin)

            while True:
                funcion = int(input("#: "))

                if funcion == 1:
                    resultado_bin = Palabra_a_Binario()
                    option = input("\n¿Copiar? (s/n): ")

                    if option.lower() == "s":
                        pyperclip.copy(resultado_bin)
                        print("Copiado✓")


                    elif option.lower() == "n":
                        continue

                elif funcion == 2:
                    traduccion = Binario_a_Palabra()
                    option = input("\n¿Copiar? (s/n): ")

                    if option.lower() == "s":
                        pyperclip.copy(traduccion)
                        print("Copiado✓")

                    elif option.lower() == "n":
                        continue

                elif funcion == 3:
                    limpiar()
                    crear_tabla(opciones)
                    break
                

        elif seleccion == 3:
            crear_tabla(option_base)

            while True:
                funcion = int(input("#: "))

                if funcion == 1:
                    codificado = palabra_a_base64()
                    option = input("\n¿Copiar? (s/n): ")

                    if option.lower() == "s":
                        pyperclip.copy(codificado)
                        print("Copiado✓")

                    elif option.lower() == "n":
                        continue

                elif funcion == 2:
                    original = base64_a_palabra()
                    option = input("\n¿Copiar? (s/n): ")

                    if option.lower() == "s":
                        pyperclip.copy(original)
                        print("Copiado✓")

                    elif option.lower() == "n":
                        continue

                elif funcion == 3:
                    limpiar()
                    crear_tabla(opciones)
                    break
                    
        elif seleccion == 4:
            crear_tabla(option_hex)

            while True:
                funcion = int(input("#: "))

                if funcion == 1:
                    traduccion = palabra_a_hexadecimal()
                    option = input("\n¿Copiar? (s/n): ")

                    if option.lower() == "s":
                        pyperclip.copy(traduccion)
                        print("Copiado✓")

                    elif option.lower() == "n":
                        continue

                elif funcion == 2:
                    traduccion = hexadecimal_a_palabra()
                    option = input("\n¿Copiar? (s/n): ")

                    if option.lower() == "s":
                        pyperclip.copy(traduccion)
                        print("Copiado.")


                    elif option.lower == "n":
                        continue

                elif funcion == 3:
                    limpiar()
                    crear_tabla(opciones)
                    break


        elif seleccion == 5:
            crear_tabla(option_uni)

            while True:
                funcion = int(input("#: "))

                if funcion == 1:
                    traduccion = palabra_a_unicode()
                    option = input("\n¿Copiar? (s/n): ")

                    if option.lower() == "s":
                        pyperclip.copy(traduccion)
                        print("Copiado✓")


                    elif option.lower() == "n":
                        continue

                elif funcion == 2:
                    traduccion = unicode_a_palabra()
                    option = input("\n¿Copiar? (s/n): ")

                    if option.lower() == "s":
                        pyperclip.copy(traduccion)
                        print("Copiado✓")


                    elif option.lower() == "n":
                        continue

                elif funcion == 3:
                    limpiar()
                    crear_tabla(opciones)
                    break

           
        elif seleccion == 6:
            while True:
                print("\n Escribe exit<> para salir del modo detector")
                texto = input("Ingrese el código: ")
                resultado = detectar(texto)
                print("Formato detectado:", resultado)
                print("El detector puede cometer errores")

                if texto.lower() == "exit<>":
                    break

        elif seleccion == 7:
            crear_tabla(chat_menu)
            print("Así que dime...")
            
            while True:
                usuario = input("En qué te puedo ayudar?")
                
                
                if "adiós" in usuario.lower() or "adios" in usuario.lower():
                    user = input("Adiós usuario, ¿deseas salir? [s/n]")

                    if user.lower() == "n" or "no":
                        print("No hay problema")
                        usuario = input("¿Qué sigue?")

                    elif user.lower() == "s" or "si":
                        print("Okey, adiós usuario")
                        time.sleep(1)
                        break

                elif "hola" in usuario.lower():
                    print("¡Hola usuario!, sigo aquí, dime...¿qué necesitas?")

                elif "gracias" in usuario.lower() or "muchas gracias" in usuario.lower():
                    print("Un gusto :)")

                elif "qué puedes hacer" in usuario.lower() or "que puedes hacer" in usuario.lower():
                    print("Puedo detectar el código que me digas, traducir yo misma lo que quieras y te puedo asesorar aquí en Multicode-System ;)")

                elif "como te llamas" in usuario.lower() or "cómo te llamas" in usuario.lower() or "cuál es tu nombre" in usuario.lower() or "cual es tu nombre" in usuario.lower():
                    print("Me llamo Mia, soy la abreviación de 'Multicode intelligent asistant'")

                elif usuario.lower() == "ascii":
                    print("Sí, sé hablar ASCII también, dime, qué quieres traducir?")

                elif "qué es el lenguaje binario" in usuario.lower() or "que es el lenguaje binario" in usuario.lower() or "hablame sobre el lenguaje binario" in usuario.lower():
                    print("El sistema binario es un sistema de numeración que utiliza únicamente dos dígitos: 0 y 1. Este sistema es la base de la informática moderna, ya que los ordenadores y dispositivos electrónicos procesan y almacenan información utilizando combinaciones de estos dos dígitos. Cada dígito en el sistema binario se denomina bit (contracción de 'binary digit'). Por ejemplo, el número binario 1001 representa un número de 4 bits \n ¿Deseas hacer una traducción?")

                elif usuario.lower() == "binario":
                    print("Sí, sé hablar Binario también, dime, qué quieres traducir?")

                elif usuario.lower() == "salir":
                    print("Cerrando chatbot...")
                    break

                else:
                    print("ehh...lo siento, no entiendo eso aún")

        elif seleccion == 8:
            break

        else:
            print("Opción inválida✕")
            continue


    except ValueError:
        print("Ingrese un número válido")
        continue
