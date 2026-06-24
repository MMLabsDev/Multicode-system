from rich.console import Console
from rich.table import Table



console = Console()

tabla = Table(title="""   Traductor de código \n M.MLabs.Dev   """)
tabla.add_column("Función")
tabla.add_column("Herramienta")

tabla.add_row("1","Español-ASCII")
tabla.add_row("2","ASCII-Español")
tabla.add_row("3","Español-Binario")
tabla.add_row("4","Binario-Español")
tabla.add_row("5","Español-Hexadecimal")
tabla.add_row("6","Hexadecimal-Español")
tabla.add_row("7","Cerrar programa")

console.print(tabla)
console.rule("[bold blue]M.MLabs.Dev • V.1.2")

def palabra_a_ASCII():
    palabra = input("Texto: ")

    ascii_texto = ""

    for letra in palabra:
        ascii_texto += str(ord(letra)) + " "

    print("ASCII:", ascii_texto)

def ASCII_a_palabra():
    codigo_ascii = input("ASCII: ")

    numeros = codigo_ascii.split()
    traduccion = ""

    for n in numeros:
        traduccion += chr(int(n))

    print("Traducción: ", traduccion)

def Palabra_a_Binario():
    traduccion = input("Texto: ")
    traduccion_bin = ""

    for letra in traduccion:
        traduccion_bin += format(ord(letra),"08b") + " "

    print("Binario: ", traduccion_bin)

def Binario_a_Palabra():
    binario = input("Binario: ")
    traduccion = ""
    for b in binario.split():
            traduccion += chr(int(b, 2))

    print("Traducción: ",traduccion)

def palabra_a_hexadecimal():
    texto = input("Texto: ")

    hexadecimal = texto.encode("utf-8").hex()

    print("Hexadecimal: ", hexadecimal)

def hexadecimal_a_palabra():
    texto = input("Hexadecimal: ")

    palabra = bytes.fromhex(texto).decode("utf-8")

    print("Traducción: ", palabra)
    
            

while True:
    try:
        
        seleccion = int(input("Seleccione función: "))

        if seleccion == 1:
            palabra_a_ASCII()

        elif seleccion == 2:
            ASCII_a_palabra()

        elif seleccion == 3:
            Palabra_a_Binario()

        elif seleccion == 4:
            Binario_a_Palabra()

        elif seleccion == 5:
            palabra_a_hexadecimal()

        elif seleccion == 6:
            hexadecimal_a_palabra()

        elif seleccion == 7:
            break

        else:
            print("Opción inválida")
            continue


    except ValueError:
        print("Ingrese un número válido")
        continue

