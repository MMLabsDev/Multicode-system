#importar librerías........................................................................................................................... 
import random
import os
import pyperclip
from rich.console import Console
from rich.table import Table

#hacer menú principal.........................................................................................................................
console = Console()

tabla = Table(title="""   Traductor de código \n M.MLabs.Dev   """)
tabla.add_column("Función")
tabla.add_column("Herramienta")

tabla.add_row("  [1]","ASCII")
tabla.add_row("  [2]","Binario")
tabla.add_row("  [3]","Hexadecimal")
tabla.add_row("  [4]","Unicode")
tabla.add_row("  [5]","Detector de código(Beta)")
tabla.add_row("  [6]","Chatbot")
tabla.add_row("  [7]","Cerrar Programa")

#tabla ASCII---------------------------------------------------------------

tabla1 = Table(title="""   Seleccione el tipo de traducción""")
tabla1.add_column("Función")
tabla1.add_column("Traductor")

tabla1.add_row("  [1]","Español - ASCII")
tabla1.add_row("  [2]","ASCII - Español")
tabla1.add_row("  [3]","Regresar")
#tabla de binario----------------------------------------------------------------
tabla2 = Table(title="""   Seleccione el tipo de traducción""")
tabla2.add_column("Función")
tabla2.add_column("Traductor")

tabla2.add_row("  [1]","Español - Binario")
tabla2.add_row("  [2]","Binario - Español")
tabla2.add_row("  [3]","Regresar")
#tabla hexadecimal---------------------------------------------------------------
tabla3 = Table(title=""" Selecione el tipo de traducción""")
tabla3.add_column("Función")
tabla3.add_column("Traductor")

tabla3.add_row("  [1]","Epañol - Hexadecimal")
tabla3.add_row("  [2]","Hexadecimal - Español")
tabla3.add_row("  [3]","Regresar")
#tabla Unicode---------------------------------------------------------------
tabla4 = Table(title=""" Selecione el tipo de traducción""")
tabla4.add_column("Función")
tabla4.add_column("Traductor")

tabla4.add_row("  [1]","Epañol - Unicode")
tabla4.add_row("  [2]","Unicode - Español")
tabla4.add_row("  [3]","Regresar")
#tabla Chatbot--------------------------------------------------------------
tabla5 = Table(title="[bold lightblue]Mia[/bold lightblue]")
tabla5.add_column("[italic]Multicode Intelligent Assistant[/italic]")
tabla5.add_row("Hola Usuario!, soy Mia (Multicode intelligent Assistant), Estoy aquí para ayudarte con tus dudas, de momento soy una versión beta, así que de momento no esperes demasiado de mí. Si queres salir de la conversación solo dime 'salir' que yo te entnderé")
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

    else:
        return "Texto normal"


saludos = ["Hola usuario","¿Hey, Qué ondas?", "Bienvenido usuario", "Hello"]
saludo = random.choice(saludos)

bienvenidas = ["¿En qué puedo ayudarte?: ","¿Qué haremos hoy?: ","Dime: ","¿Qué pasó?"]
bienvenida = random.choice(bienvenidas)
#Sistema operativo-----------------------------------------------------------
while True:
    limpiar()
    console.print(tabla)
    console.rule("[bold lightblue]Multicode-System • V.2.0[/bold lightblue]")

    try:
        seleccion = int(input("Seleccione función: "))

        if seleccion == 1:
            console.print(tabla1)

            while True:
                funcion = int(input("#:"))

                if funcion == 1:
                    resultado = palabra_a_ASCII()
                    option = input("\n¿Copiar? (s/n): ")

                    if option.lower() == "s":
                        pyperclip.copy(resultado)
                        console.print(":white_check_mark: Copiado.")

                    elif option.lower() == "n":
                        continue
                    
                elif funcion == 2:
                    traduccion = ASCII_a_palabra()
                    option = input("\n¿Copiar? (s/n): ")
                    if option.lower() == "s":
                        pyperclip.copy(traduccion)
                        console.print(":white_check_mark: Copiado.")

                    elif option.lower() == "n":
                        continue
                    
                elif funcion == 3:
                    limpiar()
                    console.print(tabla)
                    break


        elif seleccion == 2:
            console.print(tabla2)

            while True:
                funcion = int(input("#: "))

                if funcion == 1:
                    resultado_bin = Palabra_a_Binario()
                    option = input("\n¿Copiar? (s/n): ")

                    if option.lower() == "s":
                        pyperclip.copy(resultado_bin)
                        console.print(":white_check_mark: Copiado.")


                    elif option.lower() == "n":
                        continue

                elif funcion == 2:
                    traduccion = Binario_a_Palabra()
                    option = input("\n¿Copiar? (s/n): ")

                    if option.lower() == "s":
                        pyperclip.copy(traduccion)
                        console.print(":white_check_mark: Copiado.")

                    elif option.lower() == "n":
                        continue

                elif funcion == 3:
                    limpiar()
                    console.print(tabla)
                    break
                
            
        elif seleccion == 3:
            console.print(tabla3)

            while True:
                funcion = int(input("#: "))

                if funcion == 1:
                    traduccion = palabra_a_hexadecimal()
                    option = input("\n¿Copiar? (s/n): ")

                    if option.lower() == "s":
                        pyperclip.copy(traduccion)
                        console.print(":white_check_mark: Copiado.")

                    elif option.lower() == "n":
                        continue

                elif funcion == 2:
                    traduccion = hexadecimal_a_palabra()
                    option = input("\n¿Copiar? (s/n): ")

                    if option.lower == "s":
                        pyperclip.copy(traduccion)
                        console.print(":white_check_mark: Copiado.")


                    elif option.lower == "n":
                        continue

                elif funcion == 3:
                    limpiar()
                    console.print(tabla)
                    break


        elif seleccion == 4:
            console.print(tabla4)

            while True:
                funcion = int(input("#: "))

                if funcion == 1:
                    traduccion = palabra_a_unicode()
                    option = input("\n¿Copiar? (s/n): ")

                    if option.lower() == "s":
                        pyperclip.copy(traduccion)
                        console.print(":white_check_mark: Copiado.")


                    elif option.lower() == "n":
                        continue

                elif funcion == 2:
                    traduccion = unicode_a_palabra()
                    option = input("\n¿Copiar? (s/n): ")

                    if option.lower() == "s":
                        pyperclip.copy(traduccion)
                        console.print(":white_check_mark: Copiado.")


                    elif option.lower() == "n":
                        continue

                elif funcion == 3:
                    limpiar()
                    console.print(tabla)
                    break

           
        elif seleccion == 5:
            while True:
                print("\n Escribe exit<> para salir del modo detector")
                texto = input("Ingrese el código: ")
                resultado = detectar(texto)
                print("Formato detectado:", resultado)

                if texto.lower() == "exit<>":
                    break

        elif seleccion == 6:
            console.print(tabla5)
            while True:
                usuario = input("Así que dime...En qué te puedo ayudar hoy?")

                if usuario.lower() == "salir":
                    break
                elif usuario.lower() == "ascii":
                    print("Sí, sé hablar ASCII también, dime, qué quieres traducir?")
                elif usuario.lower() == "binario":
                    print("Sí, sé hablar Binario también, dime, qué quieres traducir?")
                else:
                    print("ehh...lo siento, no entiendo eso aún")

        elif seleccion == 7:
            break

        else:
            console.print("[bold red]Opción inválida[/bold red]")
            continue


    except ValueError:
        console.print("[bold red]Ingrese un número válido[/bold red]")
        continue
