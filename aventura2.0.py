import random
import time
import os
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap

jugador = {}

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # Si el sistema es Windows, se usa cls
        command = 'cls'
    os.system(command)

def baul():
    num = random.randint(1,20)
    if num % 2 == 0:
        listaBaul = ["vida", "moneda", "vida", "escudo", "fuerza", "vida", ""]
        print("Hay un baúl en la habitación")
        print("¿Quieres abrirlo?")
        respuesta = input((" Si o No "))
        if respuesta == "S":
            objeto = listaBaul[random.randint(0, 6)]
            if objeto == "vida":
                print("Has obtenido un corazón de vida")
                jugador["vida"] = jugador["vida"] + 1
            elif objeto == "moneda":
                print("Has obtenido un doblón de oro")
                jugador["monedas"] = jugador["monedas"] + 1
            elif objeto == "escudo":
                print("Has obtenido un remache de acero para el escudo")
                jugador["escudo"] = jugador["escudo"] + 1
            elif objeto == "fuerza":
                print("Has obtenido un bote de fideos chinos, estás más fuerte")
                jugador["fuerza"] = jugador["fuerza"] + 1
            else:
                print("El baúl está vacío")

        time.sleep(2)

def enemigo():
    vida = random.randint(10,25)
    fuerza = random.randint(1,15)
    if vida % 2 == 0:
        clearConsole()        
        print("Hay un enemigo en la sala!!!! con ", vida, " de vida")
        print("Preparate para luchar o salir corriendo")
        respuesta = ""
        while respuesta != 'S' and respuesta != 'N':
            respuesta = input("¿Quieres luchar con él? Si o No?")
        if respuesta == 'S':
            clearConsole()
            print("vida enemiga: ", vida, " Vida jugador: ", jugador["fuerza"])
            dadosJ = 0
            dadosE = 0
            if jugador["escudo"] > 0:
                dadosJ = int(jugador["escudo"] / 2)
            if jugador["fuerza"] > 0:
                dadosJ += jugador["fuerza"]
            dadosE = fuerza 
                
            print("juegas con: ", dadosJ, "y el bicho juega con: ", dadosE)
            
            while vida > 0 and jugador["vida"] > 0:
                clearConsole()
                print("Vida enemiga: ", vida, "fuerza enemigo:", fuerza )
                print("Vida jugador: ", jugador["vida"], "fuerza Jugador: ", jugador["fuerza"])
                print("")
                tiradas = max(dadosE,dadosJ)
                # print("tiradas", tiradas)
                finalJ = 0
                finalE = 0
                
                for num in range (1, tiradas):
                    if dadosJ >= num:
                        finalJ += random.randint(1,6)
                    if dadosE >= num:
                        finalE += random.randint(1,6)
                print("Tu jugada con ", dadosJ, " es un total de: ", finalJ)
                print("Jugada Enemigo con ", dadosE, " es un total de: ", finalE)
                time.sleep(3)
                if finalJ == finalE:
                    print("Empate, se restará 3 puntos a cada uno (escudo,fuerza o vida")
                    # restaPuntos(3,"A",vida,fuerza)
                    vida -= 3
                    if jugador["escudo"] > 0:
                        jugador["escudo"] -= 3
                        if jugador["escudo"] < 0:
                            jugador["vida"] -= (jugador["escudo"] * (-1))
                    else:
                        jugador["vida"] -= 3        
                elif finalJ > finalE:
                    print("Has Ganado, Le quitas 5 puntos (vida)")
                    # restaPuntos(5,"E",vida,fuerza)
                    vida -= 5
                else:
                    print("Has perdido, te resta 5 puntos (escudo, fuerza o vida")
                    # restaPuntos(5,"J",vida,fuerza)
                    if jugador["escudo"] > 0:
                        jugador["escudo"] -= 5
                        if jugador["escudo"] < 0:
                            jugador["vida"] -= (jugador["escudo"] * (-1))
                    else:
                        jugador["vida"] -= 5 
                time.sleep(3)
            # print("vida enemiga: ", vida, " Vida jugador: ", jugador["vida"], "fuerza Jugador: ", jugador["fuerza"])
            if jugador["vida"] <= 0:
                print("Has perdido, has causado morisión por el BichoBó")
                exit
            else:
                print("Has ganado a BichoBó, te llevas una recompensa de 3 monedas")
                jugador["monedas"] += 3

        else:
            print("cobarde!!!!!! sales huyendo de mi")
        time.sleep(5)
    clearConsole()

def BOSS():
    vidaBOSS = random.randint(15,25)
    fuerzaBOSS = random.randint(1,10)
    armas = ["Palo","Piedra","Espada"]
    defensas = ["Escudo","Esquivar"]
    num = 0
    while vidaBOSS > 0 and jugador["vida"] > 0:
        estadoJugador()
        num += 1
        if num % 2 == 0:
            arma = armas[random.randint(1,3)]
            print("El BOSS ataca con un ", arma )
            defiendes = defensas[random.randint(1,2)]
            print(jugador["nombre"], " se defiende con : ", defiendes)

            if arma == "Palo":
                if defiendes == "Escudo":
                    jugador["vida"] -= 1
                else:
                    print("Has esquivado el ataque!!!")
            elif arma == "Piedra":
                if defiendes == "Escudo":
                    jugador["vida"] -= 2
                else:
                    print("Has esquivado el ataque!!!")
            elif arma == "Espada":
                if defiendes == "Escudo":
                    jugador["vida"] -= 3
                else:
                    print("Has esquivado el ataque!!!")
        
        else:
            arma = armas[random.randint(1,3)]
            print(jugador["nombre"], "ataca con un ", arma )
            defiendes = defensas[random.randint(1,2)]
            print("El BOSS se defiende con : ", defiendes)
            if arma == "Palo":
                if defiendes == "Escudo":
                    jugador["vida"] -= 1
                else:
                    print("El BOSS a esquivado el ataque!!!")
            elif arma == "Piedra":
                if defiendes == "Escudo":
                    jugador["vida"] -= 2
                else:
                    print("El BOSS a esquivado el ataque!!!")
            elif arma == "Espada":
                if defiendes == "Escudo":
                    jugador["vida"] -= 3
                else:
                    print("El BOSS a esquivado el ataque!!!")

    if jugador["vida"] <= 0:
        print("Has sido MORISIONADO por el BOSS")
        print("Te has quedado sin la SWITCH y el mamotreco se hinchará a jugar a tu costa")
        exit
    else:
        print("Has salido VENSEDOR del combate... se acereca tu momento")
        print("Estás preparado para recoger tu switch?")
        time.sleep(4)
        switch() 
        


def estadoJugador():
    clearConsole()
    print("Vida: ", jugador["vida"], "fuerza: ", jugador["fuerza"], "escudo: ", jugador["escudo"], "monedas: ", jugador["monedas"])

def entrada():
    estadoJugador()
    print("Estás en la entrada")
    print("Estás dentro")
    print("Ves puertas al norte y sur")
    print("¿Por cual quieres pasar ?")
    print("")
    print("___/___")
    print("|      |")
    print("|  E   |")
    print("|__/___|")
    print("")
    direc = ""
    while direc != "N" and direc != "S":
        direc = input((" N ó S"))
        if direc == "N":
            sala1()
        elif direc == "S":
            print("Cobarde!!!!! Juuuurrrllll")

def sala1():
    print("")
    baul()
    enemigo()
    estadoJugador()
    if jugador["vida"] <= 0:
        exit
    #statusJugador(contJug)
    else:
        estadoJugador()
        print("Estás en la sala 1")
        print("Ves puertas en el Norte, Sur, Este y Oeste")
        print("¿ En que dirección quieres ir ?")
        direc = ""
        while direc != "N" and direc != "S" and direc != "E" and direc != "O":
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
    #statusJugador(contJug)
    print("")
    baul()
    enemigo()
    estadoJugador()
    if jugador["vida"] <= 0:
        exit
    #statusJugador(contJug)
    else:
        estadoJugador()
        print("Estás en la sala 2")
        print("Ves puertas en el Norte y Este ")
        print("¿ En que dirección quieres ir ?")
        direc = ""
        while direc != "N" and direc != "E":
            direc = input((" N o E"))
            if direc == "N":
                sala4()
            elif direc == "E":
                sala1()


def sala3():
    #statusJugador(contJug)
    print("")
    enemigo()
    estadoJugador()
    if jugador["vida"] <= 0:
        exit
    else:
        baul()
        estadoJugador()
        print("Estás en la sala 3")
        print("Ves puertas en el Norte y Oste ")
        print("¿ En que dirección quieres ir ?")
        direc = ""
        while direc != "N" and direc != "O":
            direc = input((" N o O"))
            if direc == "N":
                sala6()
            elif direc == "O":
                sala1()


def sala4():
    #statusJugador(contJug)
    print("")
    baul()
    enemigo()
    estadoJugador()
    if jugador["vida"] <= 0:
        exit
    else:
        estadoJugador()
        print("Estás en la sala 4")
        print("Ves puertas en el Este, Norte o Sur ")
        direc = ""
        while direc != "E" and direc != "N" and direc != "S":
            print("¿ En que dirección quieres  ir ?")
            direc = input((" E, N o S"))
            if direc == "E":
                sala5()
            elif direc == "N":
                sala7()
            elif direc == "S":
                sala2()


def sala5():
    #statusJugador(contJug)
    print("")
    baul()
    enemigo()
    estadoJugador()
    if jugador["vida"] <= 0:
        exit
    else:
        estadoJugador()
        print("Estás en la sala 5")
        print("Ves puertas en el Este, Oeste o Sur ")
        print("¿ En que dirección quieres  ir ?")
        direc = ""
        while direc != "E" and direc != "S" and direc != "O":
            direc = input((" E, O o S"))
            if direc == "E":
                sala6()
            elif direc == "O":
                sala4()
            elif direc == "S":
                sala1()


def sala6():
    #statusJugador(contJug)
    print("")
    llave()
    estadoJugador()
    print("Estás en la sala 6")
    print("Ves puertas en el Oeste y Sur ")
    print("¿ En que dirección quieres ir ?")
    direc = ""
    while direc != "O" and direc != "S":
        direc = input((" O o S"))
        if direc == "O":
            sala5()
        elif direc == "S":
            sala3()


def sala7():
    #statusJugador(contJug)
    print("")
    enemigo()
    estadoJugador()
    if jugador["vida"] <= 0:
        exit
    else:
        baul()
        estadoJugador()
        print("Estás en la sala 7")
        print("Ves puertas en el Este y Sur ")
        print("¿ En que dirección quieres ir ?")
        direc = ""
        while direc != "E" and direc != "S":
            direc = input((" E o S"))
            if direc == "E":
                sala8()
            elif direc == "S":
                sala4()


def sala8():
    #statusJugador(contJug)
    print("")
    baul()
    enemigo()
    estadoJugador()
    if jugador["vida"] <= 0:
        exit
    else:
        estadoJugador()
        print("Estás en la sala 8")
        print("Ves puertas en el Oeste, Norte y Este ")
        print("¿ En que dirección quieres ir ?")
        direc = ""
        while direc != "N" and direc != "O" and direc != "E":
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
    #statusJugador(contJug)
    clearConsole()
    print("Estás en la sala 9")
    print("Ves puertas en el Oste y Norte ")
    print("¿ En que dirección quieres ir ?")
    direc = ""
    while direc != "N" and direc != "S":
        direc = input((" S o N"))
        if direc == "S":
            sala8()
        elif direc == "N":
            salaBOSS()


def salaBOSS():
    #statusJugador(contJug)
    clearConsole()
    print("Has llegado a la guarida del mandril Jefaso")
    print("Hay una puerta cerrada con llave y al lado un monedero que pone...")
    print("INSERT 5 COIN")
    respuesta = input(("¿Tienes 5 monedas?"))
    if respuesta == "S" and jugador["llave"] == True:
        print("Veo que tienes una llave en tu bolsillo")
        print("Eres un maquinilla y puedes pasar a verte las caras con él")
        time.sleep(3)
        BOSS()
    else:
        print("Esto es cosa de mayores... vuelve cuando estés preparado")
        sala9()


def llave():
    if jugador["llave"] == False:
        print("Hay un tabernero que nos ofrece una llave por 4 monedas")
        print("¿Para que leches será?")
        print("¿Quieres comprarla por si acaso?")
        respuesta = input((" Si o No "))
        if respuesta == "S":
            print("Son 4 MONEDAS muchacho!!!!")
            if jugador["monedas"] >= 4:
                print("Aquí las tienes viejo borracho!!!")
                jugador["llave"] = True
                jugador["monedas"] -= 4
                time.sleep(3)
                print("BIEN!!!! has cogido la llave, para que será??")
            else:
                print("Pequeño ruiseñor... no tienes ni para el llavero.. ")
                print("Vuelve cuando consigas algo de dinerillo")
        else:
            print("Tú veras... si quieres la switch.. yo no digo nahh")
    else:
        print("El tabernero nos da las buenas tardes y se echa a dormir..zzzzz")

def switch():
    clearConsole()
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
    time.sleep(10)

def eleccion_jugador(respuesta):
    correcto = False
    while correcto == False:
        if respuesta == "Alex":
            jugador["nombre"] = "Alex the CRACK"
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
            respuesta = input("Pon bien el nombre: Alex, Cesar o Marta ")

clearConsole()

for num in range(1, 5):
    time.sleep(1)
    if num % 2 == 0:
        clearConsole()
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
        clearConsole()
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

clearConsole()
print("La SWITCH la robó un MANDRIL LUNAR")
print("La ha escondido en el fondo del laberinto")
print("¿Que personaje quieres ser? ")
print("")
respuesta = input("Alex, Cesar o Marta ")
eleccion_jugador(respuesta)

print("¿ Quieres ir a buscarla, ", jugador["nombre"], "?")
respuesta = input((" S / N "))
if respuesta == "S":
    print("Adelante")
    entrada()
elif respuesta == "N":
    print("Cobarde!!!!! Juuuurrrllll")