from rich.console import Console
from rich.table import Table
print("""
               ╔══════════════╗
              ╱              ╱║
             ╱              ╱ ║
            ╱══════════════╱  ║
            ║              ║  ║
            ║   Multicode  ║  ║
            ║              ║  ║
            ║      by      ║  ║
            ║              ║ ╱
            ║    M.MLabs   ║╱v.1
            ╚══════════════╝

""")



console = Console()

tabla = Table(title="   Traductor de código      ")
tabla.add_column("Función")
tabla.add_column("Herramienta")

tabla.add_row("1","Palabra / Español-ASCII")
tabla.add_row("2","Palabra / ASCII-Español")
tabla.add_row("3","Palabra / Español-Binario")
tabla.add_row("4","Palabra / Binario-Español")
tabla.add_row("5","Cerrar programa")
console.print(tabla)



def palabra_a_ASCII():
    palabra = input("Palabra: ")
    for letra in palabra:
        print(ord(letra), end=" ")

    print()

def ASCII_a_palabra():
    codigo_ascii = input("ASCII: ")

    numeros = codigo_ascii.split()
    traduccion = ""

    for n in numeros:
        traduccion += chr(int(n))

    print(traduccion)

def Palabra_a_Binario():
    traduccion = input("Palabra: ")

    for letra in traduccion:
        print(format(ord(letra),"08b"), end=" ")

def Binario_a_Palabra():
    binario = input("Binario: ")
    traduccion = ""
    for b in binario.split():
            traduccion += chr(int(b, 2))
    print(traduccion)
            

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
            break

        else:
            print("Opción inválida")
            continue


    except ValueError:
        print("Ingrese un número válido")
        continue
