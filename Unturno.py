import random
import funcion_csv
import seleccion_personaje
import importar_personaje
import bars
import tools
import finales

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

def seleccionarhabilidad(name, jugador):
    '''Selecciona la habilidad que se quiere utilizar y devuelve los cambios en hp, st, energy'''
    func=importar_personaje.importar_pj(name[4])
    turno = True
    changes = []
    while turno:
        if jugador != 0:
            
            print("Seleccionar habilidad")
            print("--> 1: Ataque básico: Realizas entre", func.dmg,"y", func.dmg2, " además, regeneras 20 de energía" +"\n")
            print("--> 2: Primera Habilidad")
            print("         ", func.desh1 +"\n")
            print("--> 3: Segunda Habilidad: ")
            print("         ", func.desh2 +"\n")
            print("--> 4: Tercer Habilidad: ")
            print("         ", func.desh3 +"\n")
            habilidad = input(":> ")
            while habilidad not in ("1", "2", "3", "4"):
                print("Movimiento no valido, seleccione otro movimiento:\n")
                print("--> 1: Ataque basico: Realizas entre", func.dmg,"y", func.dmg2, " además, regeneras 20 de energía" +"\n")
                print("--> 2: Primera Habilidad")
                print("         ", func.desh1 +"\n")
                print("--> 3: Segunda Habilidad: ")
                print("         ", func.desh2 +"\n")
                print("--> 4: Tercer Habilidad: ")
                print("         ", func.desh3 +"\n")
                habilidad = input(":> ")
            habilidad = int(habilidad)
        else:
            habilidad = random.randint(1, 4)
        print()
        changes1, changes2, changes1 = 0, 0, 0
        '''Mantiene en bucle hasta que se seleccione una habilidad que puedas tirar '''
        if habilidad == 2:
            changes1, changes2, changes3 = func.habilidad1(name[2], name[3])
            changes.append(changes1)
            changes.append(changes2)
            changes.append(changes3)
            if changes[1] == 0 and changes[0] == 0 and jugador == 1:
                print("No tienes suficiente energía, selecciona otra habilidad. ")
        elif habilidad == 3:
            changes1, changes2, changes3 = func.habilidad2(name[2], name[3])
            changes.append(changes1)
            changes.append(changes2)
            changes.append(changes3)
            if changes[1] == 0 and changes[0] == 0 and jugador == 1:
                print("No tienes suficiente energía, selecciona otra habilidad. ")
        elif habilidad == 4:
            changes1, changes2, changes3 = func.habilidad3(name[2], name[3])
            changes.append(changes1)
            changes.append(changes2)
            changes.append(changes3)
            if changes[1] == 0 and changes[0] == 0 and jugador == 1:
                print("No tienes suficiente energía, selecciona otra habilidad. ")
        elif habilidad == 1:
            x = basico(name[0], name[1])
            name[3] += 20
            if name[3]>=50:
                name[3] = 50
            changes = [x, 0, name[3]]
        if changes[0] != 0 or changes[1] != 0:
            turno = False
    return changes


def batalla(ingame, enemy, primera):
    Battle = True
    '''Batalla épica: Sistema de turnos hasta que la vida de alguno de los dos personajes pierda toda la vida'''
    print("Enemigo: ", enemy[4] )
    ingame[2], ingame[3] = int(ingame[2]), int(ingame[3])
    enemy[2], enemy[3] = int(enemy[2]), int(enemy[3])
    tools.clear()
    print("Comienza un duelo legendario entre dos adversarios por el destino del reinonsi..... (y otros)")
    echanges = [], []
    #Display de vida y st
    funcion_csv.personaje_txt(enemy[4])
    print("ENEMIGO:")
    enebar = bars.gen_barras(enemy[2], enemy[3])
    bars.mostrar_barras(enebar)
    print("Vida:", enemy[2], "| Energía:",  enemy[3])
    print()
    print("JUGADOR:")
    tubar = bars.gen_barras(ingame[2], ingame[3])
    bars.mostrar_barras(tubar)
    print("Vida:", ingame[2], "| Energía:", ingame[3])
    print()

    '''Inicio de la batalla'''    
    while ingame[2] > 0 and enemy[2] > 0:

        #Seleccion de habilidad del Own Character, y la pc
        changes = seleccionarhabilidad(ingame, 1)
        print(echanges)
        echanges = seleccionarhabilidad(enemy, 0)
        
        #Cambios en personaje principal
        ingame[2] += (changes[1] - echanges[0])
        ingame[3] = changes[2]
        

        #Cambios ene enemigo
        enemy[2] += (echanges[1] - changes[0])
        enemy[3] = echanges[2]
        
        tools.clear()
        funcion_csv.personaje_txt(enemy[4])

        tools.clear()
                #Display de vida y st
        funcion_csv.personaje_txt(enemy[4])
        print("ENEMIGO:")
        enebar = bars.gen_barras(enemy[2], enemy[3])
        bars.mostrar_barras(enebar)
        print("Vida:", enemy[2], "| Energía:",  enemy[3])
        print()
        print("JUGADOR:")
        tubar = bars.gen_barras(ingame[2], ingame[3])
        bars.mostrar_barras(tubar)
        print("Vida:", ingame[2], "| Energía:", ingame[3])
        print()
        #Display de daño
        print()
        print("Daño realizado: ", changes[0]) 
        print("Daño recibido: ", echanges[0], "| Curacion realizada: ", changes[1])
        print()

    print()
    if ingame[2] > 0:
        usuario = funcion_csv.leer_ascii("name.txt")
        name = usuario[0].replace(",", "" + "\n")
        x = input(f"Ganaste el duelo {name} Presione cualquier tecla para continuar")
        ingame[2] += 20
        ingame[3] += 20
        tools.clear()
        return 1, primera
    elif primera:
        tools.clear()
        input("Finalizó el combate, has perdido. ")
        primera = False
        return 0, primera

        
        



def generarenemigosarcade(n):
    '''Genera una lista de 3 enemigos, el ultimo siempre sera lonsi'''
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
    '''Genera un enemigo'''
    list=[]
    for i in range(n):
        x= random.randint(1, 6)
        en = importarenemigo(0, x)
        list.append(en)
    return list

def arcade():
    '''Programa principal, mezcla de todos las funciones anteriores'''
    print("FIGHT!")
    personaje = importarjugador(1, 0)
    lista_Enemigos = generarenemigosarcade(2)
    primera = True
    for i in range(len(lista_Enemigos)):
        ganar, primera = batalla(personaje, lista_Enemigos[i], primera)
    tools.clear()
    finales.finales(personaje[4], ganar)

def versus():
    '''Programa principal, mezcla de todos las funciones anteriores '''
    print("FIGHT!")
    personaje = importarjugador(1, 0)
    lista_Enemigos = generarenemigosversus(2)
    for i in range(len(lista_Enemigos)-1):
        batalla(personaje, lista_Enemigos[i])
