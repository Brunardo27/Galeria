from random import randint as r
import tkinter as tk
from PIL import Image, ImageTk
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import sys
import pygame

os.chdir(os.path.dirname(__file__))

def recurso(ruta):
    if getattr(sys, "frozen", False):
        base = sys._MEIPASS
    else:
        base = os.path.dirname(__file__)

    return os.path.join(base, ruta)

pygame.mixer.init()
pygame.mixer.music.load(recurso("recursos/CCC.mp3"))
pygame.mixer.music.play(-1)

contador = 0
maximo = 0

def crear_ventana():
    global contador

    v = tk.Toplevel()

    v.title("Jijijija")

    imagen = Image.open(recurso(f"recursos/img/{r(1, 15)}.png"))
    alto = 500
    ancho = imagen.width * alto // imagen.height

    imagen = imagen.resize((ancho, alto))
    imagen = ImageTk.PhotoImage(imagen)

    ancho_p = v.winfo_screenwidth() // 2
    alto_p = v.winfo_screenheight() // 2

    v.geometry(f"{ancho}x{alto}+{ancho_p - 400 + r(-300, 300)}+{alto_p - 300 + r(-200, 200)}")

    label = tk.Label(v, image=imagen)
    label.pack()

    label.image = imagen

    if not maximo or contador <= maximo:
        v.after(300, crear_ventana)

    contador += 1

root = tk.Tk()
root.withdraw()

crear_ventana()

root.mainloop()
