import random
import time

jugador = {}

def enemigo(num):
    print("Hay un enemigo en la sala!!!! con ", num, " de vida")
    print("Preparate para luchar o salir corriendo")
    respuesta = ""
    while respuesta != 'S' and respuesta != 'N':
        respuesta = input("¿Quieres luchar con él? Si o No?")
    if respuesta == 'S':
        while num > 0 and jugador["fuerza"] > 0:
            print("vida enemiga: ", num, " Vida jugador: ", jugador["fuerza"])
            respuesta = input(("Quieres atacar o rendirte?"))
            if respuesta == 'atacar':
                if (jugador["fuerza"] + jugador["escudo"]) > num:
                    num -= jugador["fuerza"]
                else:
                    jugador["monedas"] = jugador["monedas"] - 1
                print("vida enemiga: ", num, " Vida jugador: ", jugador["fuerza"])
                time.sleep(1)
            else:
                print("Uff por los pelos")
    else:
        print("cobarde!!!!!! sales huyendo de mi")

def entrada():
    print("Estás en la entrada")
    num = random.randint(6,15)
    print(num)
    if num % 2 == 0:
        enemigo(num)

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
