import funcion_csv
import seleccion_personaje
import random
from Personajes.Gregg import Gregg
from Personajes.Huigh import Huigh
from Personajes.Arbutus import Arbutus
from Personajes.Stewie import Stewie
from Personajes.Willy import Willy
from Personajes.Froggy import Froggy

def basico(mini, maxi):
    "genera el valor de daño de un basico basandose en el daño maximo y miniomo posible"
    dmg = random.randint(mini,maxi)
    return dmg 


def importarpersonaje(jugador):
    "Genera las estadisticas del personaje que se elige"
    seleccion_personaje.select_character(jugador)
    stats=funcion_csv.leer_csv("load.txt")
    return stats

def seleccionarhabilidad(name, func, ability):
    "Selecciona la habilidad que se quiere utilizar y devuelve los cambios en hp, st"
    turno = True
    while turno:
        turno = False
        if ability != 0:
            
            ability = int(input("Ingresar movimiento: atk, 1, 2, 3"))
            while ability not in (1, 2, 3, "atk"):
                ability = int(input("Movimiento? NO VALIDO, porfavor volver a ingresar ;). (1, 2, 3, atk)"))
            if ability in (1,2,3):
                ability += 4
            else:
                ability = 8
        else:
            ability=random.randint(5,6,7,8)
        if ability == 5:
            changes = func.habilidad1(name[4])
        elif ability == 6:
            changes = func.habilidad2(name[4])
        elif ability == 7:
            changes = func.habilidad3(name[4])
        elif ability == 6:
            changes = [basico(func[0], func[1]), 0, 0]
        if changes[0]+changes[1]+changes[2] <= 0:
            turno = True
    return changes
        
        


def batalla(oc, enemy):
    "Batallaepica: Sistema de turnos hasta que la vida de alguno de los dos personajes pierda toda la vida"
    import importar_personaje
    ocdet = importar_personaje.importar_pj(oc)
    enemydet = importar_personaje.importar_pj(enemy)
    egame = enemy
    ingame= oc
    while ingame[2] > 0 and enemy[2] > 0
        print("Empieza un duelo legendario entre estos 2 adversarios por el destino de la humanidad..... y los otros")
        changes = seleccionarhabilidad(oc, ocdet, 1)
        echanges = seleccionarhabilidad(enemy, enemydet, 0)
        #Cambios en personaje principal
        ingame[2] += (changes[1] - changes[0])
        ingame[3] = changes[2]

        egame[2] += (changes[1] - changes[0])
        egame = changes[2]
    print("Fin")

def generarenemigos(n):
    list=[]
    for i in range(n):
        x= random.randint(1, 6)
        if i == n-1:
            

        en = importarpersonaje(0, x)
        list.append(en)
    




def pelea():
    personaje = importarpersonaje(1, 0)
    lista_Enemigos = generarenemigos(4)
    for i in range(4):
        batalla(personaje,)  
        format_oc(personake[4])



