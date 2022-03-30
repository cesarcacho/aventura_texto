#aventura de texto https://www.youtube.com/watch?v=NIkXMrVjhiY

import time
import os


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # Si el sistema es Windows, se usa cls
        command = 'cls'
    os.system(command)

def sala1 ():
    clearConsole()
    print("Estás en la sala 1")
    print("Ves puertas en el Norte, Sur, Este y Oeste")
    print("¿ En que dirección quieres ir ?")
    direc = input((" N, S, E o O"))
    if direc == "N":
        sala5()
    elif direc == "S":
        entrada()
    elif direc == "E":
        sala3()
    elif direc == "O":
        sala2()

def sala2 ():
    clearConsole()

def sala3 ():
    clearConsole()

def sala4 ():
    clearConsole()

def sala5 ():
    clearConsole()

def sala6 ():
    clearConsole()

def entrada():
    clearConsole()
    print("Estás dentro")
    print("Ves puertas al norte y sur")
    print("¿Por cual quieres pasar ?")
    print("")
    print("___/___")
    print("|      |")
    print("|  E   |")
    print("|__/___|")
    direc = input((" N ó S"))
    if direc == "N":
        sala1()
    elif direc == "S":
        print("Cobarde!!!!! Juuuurrrllll")



clearConsole()

for num in range (10):
    time.sleep(0.5)
    clearConsole()
    if num % 2 == 0:
        print("The quest for directasa, The Videojocco")
        print("     X X    ")
        print("      X     ")
        print("     X X    ")
    else:
        print("The quest for directasa, The Videojocco")
        print("      X     ")
        print("     X X    ")
        print("      X     ")


for num in range (5):
    print("The quest for directasa, The Videojocco")
    bolita = "x"
    espacio = " "
    for desliz in range (25):
        if desliz == 0:
            mostrar = espacio + bolita 
        else:
            mostrar = espacio + mostrar
        print(mostrar)
        time.sleep(0.1)
        clearConsole()

print("La DIRECTASA LA ROBÓ UN MANDRIL LUNAR")
print("La ha escondido en el fondo de una mazmorra")
print("¿ Quieres ir a buscarla ?")

respuesta = input(("si/no " ))
if respuesta == "S":
    print("Adelante")
    entrada()
elif respuesta == "N":
    print("Cobarde!!!!! Juuuurrrllll")

