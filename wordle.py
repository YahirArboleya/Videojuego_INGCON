import random

class Colors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'

def verde(pos):
    return Colors.OKGREEN + pos + Colors.ENDC

def azul(pos):
    return Colors.OKBLUE + pos + Colors.ENDC

def cargar_palabras(nombre_archivo):
    """Carga palabras desde un archivo de texto."""
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            return [line.strip().lower() for line in f.readlines()]
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}.")
        return []

def elegir_dificultad():
    """Solicita al usuario elegir una dificultad."""
    dificultades = {
        "1": ("Fácil", "facil.txt"),
        "2": ("Normal", "normal.txt"),
        "3": ("Difícil", "dificil.txt")
    }
    while True:
        print("\nElige una dificultad:")
        print("1 - Fácil (5 letras)")
        print("2 - Normal (6 letras)")
        print("3 - Difícil (8-10 letras)")
        opcion = input("Selecciona 1, 2 o 3: ")
        if opcion in dificultades:
            return dificultades[opcion]
        print("Opción no válida, intenta de nuevo.")

# Bucle principal del juego
resp = "S"
while resp.upper() == "S":
    dificultad, archivo = elegir_dificultad()
    lista_palabras = cargar_palabras(archivo)

    if not lista_palabras:
        print("No hay palabras disponibles para esta dificultad.")
        break

    palabra_secreta = random.choice(lista_palabras)
    
    print(f"\nModo {dificultad} seleccionado.")
    print("\nREGLAS:")
    print("1- Si la letra es verde, está en la posición correcta.")
    print("2- Si la letra es azul, está en la palabra pero en otra posición.")
    print("3- Si no tiene color, no está en la palabra.")
    print("4- Tienes 5 intentos.\n")

    intentos = 5

    for intento in range(intentos):
        while True:
            palabra_usuario = input(f"Dame una palabra de {len(palabra_secreta)} letras: ").lower()
            if len(palabra_usuario) == len(palabra_secreta):
                break
            print(f"La palabra debe contener {len(palabra_secreta)} letras.")

        if palabra_usuario == palabra_secreta:
            print(verde(palabra_usuario))
            print("¡Felicidades! Adivinaste la palabra.")
            break
        else:
            resultado = ""
            for i in range(len(palabra_secreta)):
                if palabra_usuario[i] == palabra_secreta[i]:
                    resultado += verde(palabra_usuario[i])
                elif palabra_usuario[i] in palabra_secreta:
                    resultado += azul(palabra_usuario[i])
                else:
                    resultado += palabra_usuario[i]

            print(resultado)

    else:
        print(f"Se han acabado los intentos. La palabra correcta era: {palabra_secreta}")

    resp = input("¿Quieres volver a jugar? (S/N): ").upper()
    while resp not in ["S", "N"]:
        resp = input("Introduce S o N: ").upper()

print("Adiós")

