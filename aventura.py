# aventura de texto https://www.youtube.com/watch?v=NIkXMrVjhiY

import time
import os
import random

jugador = {}
contJug = 0


def clearConsole1():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # Si el sistema es Windows, se usa cls
        command = 'cls'
    os.system(command)
#     statusJugador()


def statusJugador(contJug):
    # contJug = contJug + 1
    command = 'clear'
    if os.name in ('nt', 'dos'):  # Si el sistema es Windows, se usa cls
        command = 'cls'
    os.system(command)
    if contJug % 2 == 0:
        jugador["vida"] = jugador["vida"] - 1
    print("Jugador: ", jugador["nombre"])
    print("Vida: ", jugador["vida"])
    print("Fuerza: ", jugador["fuerza"],
          "           Escudo: ", jugador["escudo"])
    print("Monedas: ", jugador["monedas"],
          "         Llave: ", jugador["llave"])

    if jugador["vida"] <= 3:
        print("Estás muy débil, si no comes procederas a la MORISION")
    elif jugador["vida"] == 0:
        print("MORISIÓN COMPLETADA.... (Será que no te avisé)")
        print("El MANDRIL LUNAR se quedará con la switch y jugará a toda tu biblioteca de juegos")
        exit()

    time.sleep(2)


def baul():
    listaBaul = ["vida", "moneda", "vida", "escudo", "fuerza", "vida", ""]
    print("Hay un baúl en la habitación")
    print("¿Quieres abrirlo?")
    respuesta = input((" Si o No "))
    if respuesta == "S":
        objeto = listaBaul[random.randint(0, 6)]
        if objeto == "vida":
            print("Has obtenido un corazón de vida")
            jugador["vida"] = jugador["vida"] + 3
        elif objeto == "moneda":
            print("Has obtenido un doblón de oro")
            jugador["monedas"] = jugador["monedas"] + 1
        elif objeto == "escudo":
            print("Has obtenido un remache de acero para el escudo")
            jugador["escudo"] = jugador["escudo"] + 1
        elif objeto == "fuerza":
            print("Has obtenido un bote de fideos chinos")
            jugador["fuerza"] = jugador["fuerza"] + 1
        else:
            print("El baúl está vacío")

    time.sleep(2)


def BOSS():
    dadosEne = random.randint(1, 6)
    dadosEne = dadosEne + random.randint(1, 6)
    if (jugador["fuerza"] + jugador["escudo"]) > 15:
        dadosJug = random.randint(1, 6)
        dadosJug = dadosJug + random.randint(1, 6)
    else:
        dadosJug = random.randint(1, 6)
    print(jugador["nombre"], " = ", dadosJug, " VS Enemigo = ", dadosEne)
    if dadosJug > dadosEne:
        print("Has ganado !!!!")
        print("Has conseguido recuperar la SWITCH")
        switch()
    elif dadosEne > dadosJug:
        print("Has PERDIDO!!!!")
        print("Te quita un corazón de vida")
        jugador["vida"] = jugador["vida"] - 1
    elif dadosEne == dadosJug:
        print("EMPATE!!!! Ha sido una lucha encarnizada")
        print("Has sufrido daño, bajas un punto de fuerza, escudo y vida")
        jugador["fuerza"] = jugador["fuerza"] - 1
        jugador["escudo"] = jugador["escudo"] - 1
        jugador["vida"] = jugador["vida"] - 1
        time.sleep(5)


def enemigo():
    print("Un enemigo en la sala !!!!!")
    print("¿Quieres enfrentarte a él?")
    respuesta = input((" Si o No"))
    if respuesta == "S":
        dadosEne = random.randint(1, 6)
        if (jugador["fuerza"] + jugador["escudo"]) > 10:
            dadosJug = random.randint(1, 6)
            dadosJug = dadosJug + random.randint(1, 6)
        else:
            dadosJug = random.randint(1, 6)
        print(jugador["nombre"], " = ", dadosJug, " VS Enemigo = ", dadosEne)
        if dadosJug > dadosEne:
            print("Has ganado !!!!")
            print("Has conseguido una moneda")
            jugador["monedas"] = jugador["monedas"] + 1
            jugador["vida"] = jugador["vida"] + 1
        elif dadosEne > dadosJug:
            print("Has PERDIDO!!!!")
            print("Te quita un corazón de vida")
            jugador["vida"] = jugador["vida"] - 1
        elif dadosEne == dadosJug:
            print("EMPATE!!!! Ha sido una lucha encarnizada")
            print("Has sufrido daño, bajas un punto de fuerza, escudo y vida")
            jugador["fuerza"] = jugador["fuerza"] - 1
            jugador["escudo"] = jugador["escudo"] - 1
            jugador["vida"] = jugador["vida"] - 1
    else:
        print("Sal corriendoooo!!!!!")
    time.sleep(3)


def sala1():
    statusJugador(contJug)
    print("Estás en la sala 1")
    print("")
    # print("Hay un baúl en la sala, ¿quieres abrirlo?")
    # respuesta = input((" Si o No : "))
    # if respuesta == "S":
    baul()
    statusJugador(contJug)
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


def sala2():
    statusJugador(contJug)
    print("Estás en la sala 2")
    print("")
    enemigo()
    statusJugador(contJug)
    print("Ves puertas en el Norte y Este ")
    print("¿ En que dirección quieres ir ?")
    direc = input((" N o E"))
    if direc == "N":
        sala4()
    elif direc == "E":
        sala1()


def sala3():
    statusJugador(contJug)
    print("Estás en la sala 3")
    print("")
    enemigo()
    baul()
    print("Ves puertas en el Norte y Oste ")
    print("¿ En que dirección quieres ir ?")
    direc = input((" N o O"))
    if direc == "N":
        sala6()
    elif direc == "O":
        sala1()


def sala4():
    statusJugador(contJug)
    print("Estás en la sala 4")
    print("")
    enemigo()
    print("Ves puertas en el Este, Norte o Sur ")
    print("¿ En que dirección quieres  ir ?")
    direc = input((" E, N o S"))
    if direc == "E":
        sala5()
    elif direc == "N":
        sala7()
    elif direc == "S":
        sala2()


def sala5():
    statusJugador(contJug)
    print("Estás en la sala 5")
    print("")
    baul()
    print("Ves puertas en el Este, Oeste o Sur ")
    print("¿ En que dirección quieres  ir ?")
    direc = input((" E, O o S"))
    if direc == "E":
        sala6()
    elif direc == "O":
        sala4()
    elif direc == "S":
        sala1()


def sala6():
    statusJugador(contJug)
    print("Estás en la sala 6")
    print("")
    llave()
    print("Ves puertas en el Oeste y Sur ")
    print("¿ En que dirección quieres ir ?")
    direc = input((" O o S"))
    if direc == "O":
        sala5()
    elif direc == "S":
        sala3()


def sala7():
    statusJugador(contJug)
    print("Estás en la sala 7")
    print("")
    enemigo()
    baul()
    print("Ves puertas en el Este y Sur ")
    print("¿ En que dirección quieres ir ?")
    direc = input((" E o S"))
    if direc == "E":
        sala8()
    elif direc == "S":
        sala4()


def sala8():
    statusJugador(contJug)
    print("Estás en la sala 8")
    print("")
    print("Ves puertas en el Oeste, Norte y Este ")
    print("¿ En que dirección quieres ir ?")
    direc = input((" O, N o E"))
    if direc == "E":
        sala9()
    elif direc == "O":
        sala7()
    elif direc == "N":
        print("Sala del foso")
        print("OOOOHHHHHH")
        print("¡¡¡¡ CASPITA !!!!! He caído en un foso y me encuentro en la ENTRADA")
        time.sleep(3)
        entrada()


def sala9():
    statusJugador(contJug)
    print("Estás en la sala 9")
    print("Ves puertas en el Oste y Norte ")
    print("¿ En que dirección quieres ir ?")
    direc = input((" O o N"))
    if direc == "O":
        sala8()
    elif direc == "N":
        salaBOSS()


def salaBOSS():
    statusJugador(contJug)
    print("Has llegado a la guarida del mandril Jefaso")
    print("Hay una puerta cerrada con llave")
    if jugador["llave"] == True:
        print("Veo que tienes una llave en tu bolsillo")
        print("Eres un maquinilla y puedes pasar a verte las caras con él")
        BOSS()


def entrada():
    # statusJugador()
    print("Estás dentro")
    print("Ves puertas al norte y sur")
    print("¿Por cual quieres pasar ?")
    print("")
    print("___/___")
    print("|      |")
    print("|  E   |")
    print("|__/___|")
    print("")
    direc = input((" N ó S"))
    if direc == "N":
        sala1()
    elif direc == "S":
        print("Cobarde!!!!! Juuuurrrllll")


def eleccion_jugador(respuesta):
    correcto = False
    while correcto == False:
        if respuesta == "Alex":
            jugador["nombre"] = "Alex el CRACK"
            jugador["vida"] = 10
            jugador["fuerza"] = 10
            jugador["escudo"] = 10
            jugador["monedas"] = 0
            jugador["llave"] = False
            correcto = True
        elif respuesta == "Cesar":
            jugador["nombre"] = "Cesar el gordito"
            jugador["vida"] = 10
            jugador["fuerza"] = 8
            jugador["escudo"] = 12
            jugador["monedas"] = 0
            jugador["llave"] = False
            correcto = True
        elif respuesta == "Marta":
            jugador["nombre"] = "Martis the BOSS"
            jugador["vida"] = 10
            jugador["fuerza"] = 12
            jugador["escudo"] = 8
            jugador["monedas"] = 0
            jugador["llave"] = False
            correcto = True
        else:
            respuesta = input("Alex, Cesar o Marta ")


def llave():
    print("Has encontrado una llave tirada en el suelo")
    print("¿Para que leches será?")
    print("¿La quieres pillar para la buchaca")
    respuesta = input((" Si o No "))
    if respuesta == "S":
        jugador["llave"] = True
        statusJugador(contJug)
    else:
        print("Tú veras... si quieres la switch.. yo no digo nahh")


def switch():
    print("       %(//////( ##############(#################################################### *//////#(      ")
    print("    %/(((((((((/%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%((%(((((((/%   ")
    print("   ((((((((((((/%%@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@%&((((((((((((#  ")
    print("  ,((((@&#@%(((/%%@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@%%(((((%%&(((((  ")
    print("  *(((&%%%%%&((/&%@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@&&(#%%@(((%#%((  ")
    print("  *(((##@@@##((/&&@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@&%(((((%*&(((((  ")
    print("  *((((((((((((/&&@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@&&(((((((((((((  ")
    print("  *(((((%&%(((((&&@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@&&((((((#(((((#  ")
    print("  *((%#&(((%%%(/&&@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@&&(((%%%%%&#((#  ")
    print("  *((#%((#((%#((&&@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@&&(((%%&&@@#((#  ")
    print("  *(((((%&&(((((&&@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@&&((((##%##(((#  ")
    print("  *(((((((#%#(((&&@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@&&(((&&#((((((#  ")
    print("  *(((((((((((((&&@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@&&(((%%(((((((#  ")
    print("  .#((((((((((((&&@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@&&((((((((((((#  ")
    print("   %(((((((((((/&&@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@&&(((((((((((#/  ")
    print("     &#(((((((((&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&(((((((((#&    ")

# clearConsole()


for num in range(1, 5):
    time.sleep(1)
    clearConsole1()
    if num % 2 == 0:
        print("       XXXXXX   XXXXX   XXXXX   XXXXXX  ")
        print("        X   X   X   X   X   X   X   X   ")
        print("        X   XXXXX   XXXXX   XXXXX   X   ")
        print("        X                           X   ")
        print("        X                           X   ")
        print("         X                         X    ")
        print("          X                       X     ")
        print("           X                     X      ")
        print("           X       ******       X       ")
        print("    O      X      *  **  *      X       ")
        print("   /X\     X     *   **   *     X       ")
        print("  / X \    X     *   **   *     X       ")
        print("    X      X     *   **   *     X       ")
        print("   / \     X     *   **   *     X       ")
    else:
        print("       XXXXXX   XXXXX   XXXXX   XXXXXX  ")
        print("        X   X   X   X   X   X   X   X   ")
        print("        X   XXXXX   XXXXX   XXXXX   X   ")
        print("        X                           X   ")
        print("        X                           X   ")
        print("         X                         X    ")
        print("          X                       X     ")
        print("           X                     X      ")
        print("           X       ******       X       ")
        print("  \ O /    X      *  **  *      X       ")
        print("   \X/     X     *   **   *     X       ")
        print("    X      X     *   **   *     X       ")
        print("    X      X     *   **   *     X       ")
        print("   / \     X     *   **   *     X       ")


# for num in range (3):
#     bolita = "******"
#     espacio = " "
#     for desliz in range (30):
#         print("The quest for directasa, The Videojocco")
#         if desliz == 0:
#             mostrar = espacio + bolita
#         else:
#             mostrar = espacio + mostrar
#         print(mostrar)
#         time.sleep(0.05)
#         clearConsole()

print("La switch la robó un MANDRIL LUNAR")
print("La ha escondido en el fondo de una mazmorra")
print("¿Que personaje quieres ser? ")
print("")
respuesta = input("Alex, Cesar o Marta ")
eleccion_jugador(respuesta)
# print(jugador)

print("¿ Quieres ir a buscarla, ", jugador["nombre"], "?")
respuesta = input((" S / N "))
if respuesta == "S":
    print("Adelante")
    entrada()
elif respuesta == "N":
    print("Cobarde!!!!! Juuuurrrllll")
