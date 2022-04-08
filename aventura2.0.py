import random
import time
from weakref import finalize

jugador = {}

def enemigo(vida, fuerza):
    print("Hay un enemigo en la sala!!!! con ", vida, " de vida")
    print("Preparate para luchar o salir corriendo")
    respuesta = ""
    while respuesta != 'S' and respuesta != 'N':
        respuesta = input("¿Quieres luchar con él? Si o No?")
    if respuesta == 'S':
        
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
            tiradas = max(dadosE,dadosJ)
            print("tiradas", tiradas)
            finalJ = 0
            finalE = 0
            
            for num in range (1, tiradas):
                if dadosJ >= num:
                    finalJ += random.randint(1,6)
                if dadosE >= num:
                    finalE += random.randint(1,6)
            print("Tu jugada con ", dadosJ, " es un total de: ", finalJ)
            print("Jugada Enemigo con ", dadosE, " es un total de: ", finalE)
            time.sleep(5)
            if finalJ == finalE:
                print("Empate, se restará 3 puntos a cada uno (escudo,fuerza o vida")
                restaPuntos(3,"A",vida,fuerza)
            elif finalJ > finalE:
                print("Has Ganado, Le quitas 5 puntos (vida)")
                restaPuntos(3,"E",vida,fuerza)
            else:
                print("Has perdido, te resta 5 puntos (escudo, fuerza o vida")
                restaPuntos(3,"J",vida,fuerza)
            vida = 0
        return
    else:
        print("cobarde!!!!!! sales huyendo de mi")

def restaPuntos(puntos, quien, vida, fuerza):
    if quien == "E":
        vida -= puntos
        jugador["escudo"] -= puntos
    elif quien == "J":
        jugador["escudo"] -= puntos
    else:
        vida -= puntos

def entrada():
    print("Estás en la entrada")
    vida = random.randint(6,15)
    print(vida)
    if vida % 2 == 0:
        fuerza = random.randint(1,10)
        enemigo(vida, fuerza)

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
