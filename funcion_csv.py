from Personajes.Gregg import Gregg
from Personajes.Huigh import Huigh
from Personajes.Arbutus import Arbutus
from Personajes.Stewie import Stewie
from Personajes.Willy import Willy
from Personajes.Froggy import Froggy
from Personajes.Lonsi import Lonsi

def leer_csv(archivo):
    with open(f'{archivo}', 'r') as file:
        variable = file.readlines()
        # for row in hoja_personaje:
        #     print(row)
        return variable

def escribir_csv(personaje):
    lista = [str(personaje.dmg),str(personaje.dmg2),str(personaje.hp),str(personaje.energia),str(personaje.name),str(personaje.desh1),str(personaje.desh2),str(personaje.desh3)]
    arch = open('load.txt', 'wt') 
    for i in lista:
        arch.write(i + ",")
    return list
    arch.close()

def cargar_csv():
    f = open("load.txt", "r")
    load_list = f.readlines()
    dmg= load_list[0]
    dmg2= load_list[1]
    hp = load_list[2]
    energia = load_list[3]
    name = load_list[4]
    des = load_list[5]
    desh1 = load_list[6]
    desh2 = load_list[7]
    desh3 = load_list[8]

def jefe_csv():
    lista = [str(Lonsi.dmg),str(Lonsi.dmg2),str(Lonsi.hp),str(Lonsi.energia),str(Lonsi.name),str(Lonsi.desh1),str(Lonsi.desh2),str(Lonsi.desh3)]
    arch = open('lonsi.txt', 'wt') 
    for i in lista:
        arch.write(i + ",")
    return list
    arch.close()

# def save():
#     list = [
#         name,
#         str(hp),
#         str(dmg)
#     ]

#     f = open("load.csv", "w")

#     for item in list:
#         f.write(item + "\n")
#     f.close()

#escribir_csv(Lonsi)

