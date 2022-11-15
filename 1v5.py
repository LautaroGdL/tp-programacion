import funcion_csv
import seleccion_personaje
import random


def importarpersonaje():
    "Provoca 5 peleas entre tu personaje y 5 aleatorios; desp de cada pelea se resetea la vida del personajes"
    seleccion_personaje()
    stats=funcion_csv.leer_csv("load.txt")
    return stats

def seleccionarhabilidad(name):
    "Selecciona la habilidad que se quiere utilizar y devuelve los cambios en hp, st"
    turno = True
    while turno:
        ability = int(input("Ingresar habilidad a lanzar(1,2,3)")
        while 1<ability>3


def batalla(oc, enemy):
    "Batallaepica: Sistema de turnos hasta que la vida de alguno de los dos personajes pierda toda la vida"
    while oc[2] > 0 and enemy1[2] > 0:
        print("Empieza un duelo legendario entre estos 2 adversarios por el destino de la humanidad..... y los otros")









importarpersonaje()


