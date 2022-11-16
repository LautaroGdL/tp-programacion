from Personajes.Gregg import Gregg
from Personajes.Huigh import Huigh
from Personajes.Arbutus import Arbutus
from Personajes.Stewie import Stewie
from Personajes.Willy import Willy
from Personajes.Froggy import Froggy
from Personajes.Lonsi import Lonsi

def leer_ascii(archivo):
    #Lee el archivo de texto y lo guarda como lista
    with open(f'Ascii/{archivo}', 'r') as file:
        variable = file.readlines()
        # for row in hoja_personaje:
        #     print(row)
        return variable

def leer_csv(archivo):
    #Lee el archivo de texto y lo guarda como lista
    with open(f'{archivo}', 'r') as file:
        variable = file.readlines()
        # for row in hoja_personaje:
        #     print(row)
        return variable

def personaje_txt(archivo):
    #Lee el archivo de texto dentro de Dibujos y lo imprime
    with open(f'Dibujos/{archivo}_ascii.txt', 'r') as file:
        variable = file.readlines()
        for i in range(0, len(variable)):
                        print(variable[i].replace("\n", ""))

def escribir_csv(personaje):
    #Escribe un archivo temporal que guarda las variables del personaje deseado para luego ser llamado como una lista
    lista = [str(personaje.dmg),str(personaje.dmg2),str(personaje.hp),str(personaje.energia),str(personaje.name),str(personaje.desh1),str(personaje.desh2),str(personaje.desh3),str(personaje.win),str(personaje.lose)]
    arch = open('Ascii/load.txt', 'wt') 
    for i in lista:
        arch.write(i + ",")
    return list
    arch.close()

def guardar_nombre(name):
    lista = [name]
    arch = open(f'Ascii/name.txt', 'wt') 
    for i in lista:
        arch.write(i + ",")
    return list


def cargar_csv():
    #Lee el archivo, lee el listado y asigna cada columna como una variable(deberia)
    f = open("Ascii/load.txt", "r")
    load_list = f.readlines()
    load_list = [
        # [str(dmg)],
        # [str(dmg2)],
        # [str(hp)],
        # [str(energia)],
        # [str(personaje.name)],
        # [str(personaje.desh1)],
        # [str(personaje.desh2)],
        # [str(personaje.desh3)]
        ]
    return load_list


def jefe_csv():
    #Trae la informacion del Jefe Final
    lista = [str(Lonsi.dmg),str(Lonsi.dmg2),str(Lonsi.hp),str(Lonsi.energia),str(Lonsi.name),str(Lonsi.desh1),str(Lonsi.desh2),str(Lonsi.desh3)]
    arch = open('Ascii/lonsi.txt', 'wt') 
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



