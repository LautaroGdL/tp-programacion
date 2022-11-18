import random
import funcion_csv
import seleccion_personaje
import importar_personaje
import bars
import tools
from Personajes.Arbutus import Arbutus
from Personajes.Froggy import Froggy
from Personajes.Gregg import Gregg
from Personajes.Huigh import Huigh
from Personajes.Stewie import Stewie
from Personajes.Willy import Willy


def basico(mini, maxi):
    '''Genera el valor de daño de un basico basandose en el daño maximo y miniomo posible'''
    dmg = random.randint(int(mini),int(maxi))
    return dmg 


def importarjugador(jugador, nro):
    '''Genera las estadisticas del personaje que se elige'''
    seleccion_personaje.select_character(jugador, nro)
    stats=funcion_csv.leer_ascii("load.txt")
    stats = stats[0].split(',')
    return stats

def importarenemigo(jugador, nro):
    '''Genera las estadisticas del personaje que se elige'''
    seleccion_personaje.select_character(jugador, nro)
    stats=funcion_csv.leer_ascii("enemy.txt")
    stats = stats[0].split(',')
    return stats

def importarlonsi(jugador, nro):
    '''Genera las estadisticas del personaje que se elige'''
    seleccion_personaje.select_character(jugador, nro)
    stats=funcion_csv.leer_ascii("lonsi.txt")
    stats = stats[0].split(',')
    return stats

def seleccionarhabilidad(name, ability):
    '''Selecciona la habilidad que se quiere utilizar y devuelve los cambios en hp, st, energy'''
    func=importar_personaje.importar_pj(name[4])
    turno = True
    changes = []
    jugador = ability
    while turno:
        turno = True
        if ability != 0:
            
            ability = print("|Ataque  =   1||Habilidad = 2|\n|Habilidad = 3||Habilidad = 4| ")
            ability = input(">")
            while ability not in ("1", "2", "3", "4"):
                ability = print("Movimiento no valido, porfavor volver a seleccionar movimiento:\n|Ataque  =   1||Habilidad = 2|\n|Habilidad = 3||Habilidad = 4|")
                ability = input(">")
            if ability in ("2","3","4"):
                ability = int(ability)
                ability += 4
            else:
                ability = 8
        else:
            ability=random.randint(5, 8)
        changes1, changes2, changes1 = 0, 0, 0
        '''Mantiene en bucle hasta que se seleccione una habilidad que puedas tirar '''
        if ability == 5:
            changes1, changes2, changes3 = func.habilidad1(name[2], name[3])
            changes.append(changes1)
            changes.append(changes2)
            changes.append(changes3)
            if changes[1] == 0 and changes[0] == 0 and jugador == 1:
                print("No tiene suficiente energia, selecciona otra habilidad. ")
        elif ability == 6:
            changes1, changes2, changes3 = func.habilidad2(name[2], name[3])
            changes.append(changes1)
            changes.append(changes2)
            changes.append(changes3)
            if changes[1] == 0 and changes[0] == 0 and jugador == 1:
                print("No tiene suficiente energia, selecciona otra habilidad. ")
        elif ability == 7:
            changes1, changes2, changes3 = func.habilidad3(name[2], name[3])
            changes.append(changes1)
            changes.append(changes2)
            changes.append(changes3)
            if changes[1] == 0 and changes[0] == 0 and jugador == 1:
                print("No tiene suficiente energia, selecciona otra habilidad. ")
        elif ability == 8:
            x = basico(name[0], name[1])
            changes = [x, 0, name[3]+60]
        if changes[0] != 0 or changes[1] != 0:
            turno = False
    return changes


def batalla(ingame, enemy):
    Battle = True
    '''Batallaepica: Sistema de turnos hasta que la vida de alguno de los dos personajes pierda toda la vida'''
    print("Enemigo: ", enemy[4] )
    ingame[2], ingame[3] = int(ingame[2]), int(ingame[3])
    enemy[2], enemy[3] = int(enemy[2]), int(enemy[3])
    print("Empieza un duelo legendario entre estos 2 adversarios por el destino de la humanidad..... y los otros")
    while Battle:
        funcion_csv.personaje_txt(enemy[4])

        '''Inicio de la batalla'''
        enebar = bars.gen_barras(enemy[2], enemy[3])
        bars.mostrar_barras(enebar)
        print("vida: ", enemy[2], "|energia: ",  enemy[3])
        print("TU:")
        tubar = bars.gen_barras(ingame[2], ingame[3])
        bars.mostrar_barras(tubar)
        print("vida: ", ingame[2], "|energia: ", ingame[3])
        
        while ingame[2] >= 0 and enemy[2] >= 0:
            #Turno del jugador
            #Seleccion de habilidad del Own Character, y la pc
            changes = seleccionarhabilidad(ingame, 1)
            echanges = seleccionarhabilidad(enemy, 0)
            
            tools.clear()
            funcion_csv.personaje_txt(enemy[4])
            #Display de daño
            print()
            print("Daño realizado: ", changes[0]) 
            print("Daño recibido: ", echanges[0])
            print()
            print("ENEMIGO:")
            enebar = bars.gen_barras(enemy[2], enemy[3])
            bars.mostrar_barras(enebar)
            print("vida: ", enemy[2], "|energia: ",  enemy[3])
            print()
            print("JUGADOR:")
            tubar = bars.gen_barras(ingame[2], ingame[3])
            bars.mostrar_barras(tubar)
            print("vida: ", ingame[2], "|energia: ", ingame[3])

            #Cambios en personaje principal
            ingame[2] += (changes[1] - echanges[0])
            ingame[3] = changes[2]
            

            #Cambios en personaje enemigo
            enemy[2] += (echanges[1] - changes[0])
            enemy[3] = echanges[2]


        Battle = False
    print()
    if ingame[2] > 0:
        usuario = funcion_csv.leer_ascii("name.txt")
        name = usuario[0].replace(",", "")
        print(f"Fin del combate, has ganado {name}!")
        ingame[2] += 300
    else:
        tools.clear()
        print("Fin del combate, has perdido.")
        
        



def generarenemigosarcade(n):
    '''Genera una lista de 5 enemigos, el ultimo siempre sera lonsi'''
    list=[]
    for i in range(n):
        x= random.randint(1, 6)
        en = importarenemigo(0, x)
        list.append(en)
        if i == n-1:
            lonsi = importarlonsi(0, 666)
            list.append(lonsi)
    #list.pop()
    return list

def generarenemigosversus(n):
    '''Genera una lista de 5 enemigos, el ultimo siempre sera lonsi'''
    list=[]
    for i in range(n):
        x= random.randint(1, 6)
        en = importarenemigo(0, x)
        if i == n:
            lonsi = importarlonsi(0, 666)
        list.append(en)
    return list

def arcade():
    '''Programa principal, mezcla de todos las funciones anteriores'''
    print("FIGHT!")
    personaje = importarjugador(1, 0)
    lista_Enemigos = generarenemigosarcade(2)
    for i in range(len(lista_Enemigos)):
        batalla(personaje, lista_Enemigos[i])

def versus():
    '''Programa principal, mezcla de todos las funciones anteriores '''
    print("FIGHT!")
    personaje = importarjugador(1, 0)
    lista_Enemigos = generarenemigosversus(2)
    for i in range(len(lista_Enemigos)-1):
        batalla(personaje, lista_Enemigos[i])

# x = generarenemigosarcade(2)
# print(x)

# x = batalla(Arbutus,Lonsi)
# print(x)

