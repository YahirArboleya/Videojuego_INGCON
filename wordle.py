import random
import tkinter as tk
from tkinter import messagebox

# Cargar palabras desde archivos
def cargar_palabras(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return [line.strip().lower() for line in f.readlines()]
    except FileNotFoundError:
        messagebox.showerror("Error", f"No se encontró el archivo {archivo}")
        return []

# Función para elegir dificultad
def elegir_dificultad(dificultad, archivo):
    global palabra_secreta, intentos_restantes
    lista_palabras = cargar_palabras(archivo)
    
    if not lista_palabras:
        return
    
    palabra_secreta = random.choice(lista_palabras)
    intentos_restantes = 5
    
    ventana_dificultad.destroy()  # Cierra la ventana de selección
    iniciar_juego()  # Inicia el juego

# Crear ventana para elegir dificultad
def ventana_seleccion():
    global ventana_dificultad
    ventana_dificultad = tk.Tk()
    ventana_dificultad.title("Seleccionar Dificultad")
    
    tk.Label(ventana_dificultad, text="Elige una dificultad:", font=("Arial", 14)).pack(pady=10)
    
    tk.Button(ventana_dificultad, text="Fácil (5 letras)", command=lambda: elegir_dificultad("Fácil", "facil.txt")).pack(pady=5)
    tk.Button(ventana_dificultad, text="Normal (6 letras)", command=lambda: elegir_dificultad("Normal", "normal.txt")).pack(pady=5)
    tk.Button(ventana_dificultad, text="Difícil (8-10 letras)", command=lambda: elegir_dificultad("Difícil", "dificil.txt")).pack(pady=5)
    
    ventana_dificultad.mainloop()

# Función para procesar la palabra ingresada
def verificar_palabra():
    global intentos_restantes
    palabra = entrada.get().lower()
    
    if len(palabra) != len(palabra_secreta):
        messagebox.showwarning("Advertencia", f"La palabra debe tener {len(palabra_secreta)} letras.")
        return

    # Limpia la entrada
    entrada.delete(0, tk.END)
    
    resultado = []
    
    for i in range(len(palabra_secreta)):
        if palabra[i] == palabra_secreta[i]:
            resultado.append(("green", palabra[i]))  # Letra correcta y bien ubicada
        elif palabra[i] in palabra_secreta:
            resultado.append(("blue", palabra[i]))  # Letra en la palabra, pero mal ubicada
        else:
            resultado.append(("black", palabra[i]))  # Letra incorrecta

    mostrar_resultado(resultado)

    if palabra == palabra_secreta:
        messagebox.showinfo("¡Ganaste!", f"¡Correcto! La palabra era {palabra_secreta}")
        ventana_juego.destroy()
        return

    intentos_restantes -= 1
    if intentos_restantes == 0:
        messagebox.showerror("Perdiste", f"Se acabaron los intentos. La palabra era {palabra_secreta}")
        ventana_juego.destroy()

# Función para mostrar el resultado en etiquetas de colores
def mostrar_resultado(resultado):
    for widget in marco_palabra.winfo_children():
        widget.destroy()

    for color, letra in resultado:
        lbl = tk.Label(marco_palabra, text=letra.upper(), font=("Arial", 18, "bold"), width=3, height=2)
        lbl.config(bg=color, fg="white")
        lbl.pack(side=tk.LEFT, padx=2)

# Iniciar juego con ventana
def iniciar_juego():
    global ventana_juego, entrada, marco_palabra
    
    ventana_juego = tk.Tk()
    ventana_juego.title("Wordle - Juego")
    
    tk.Label(ventana_juego, text="Introduce una palabra:", font=("Arial", 14)).pack(pady=10)
    
    entrada = tk.Entry(ventana_juego, font=("Arial", 14))
    entrada.pack(pady=5)
    
    tk.Button(ventana_juego, text="Verificar", command=verificar_palabra).pack(pady=5)
    
    marco_palabra = tk.Frame(ventana_juego)
    marco_palabra.pack(pady=10)

    ventana_juego.mainloop()

# Iniciar la selección de dificultad
ventana_seleccion()
