import os

def limpiar_pantalla():
    if os.name == "Windows":
        os.system("cls")
    else:
        os.system("clear") or os.system("cls")
