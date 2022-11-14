from Personajes.Gregg import Gregg
from Personajes.Huigh import Huigh
from Personajes.Arbutus import Arbutus
from Personajes.Stewie import Stewie
from Personajes.Willy import Willy
from Personajes.Froggy import Froggy

def leer_csv(archivo):
    with open(f'{archivo}', 'r') as file:
        variable = file.readlines()
        # for row in hoja_personaje:
        #     print(row)
        return variable

def escribir_csv(personaje):
    lista = [personaje.name,personaje.hp,personaje.dmg]
    with open(f'./Personajes/{personaje}/{personaje}.txt', 'w') as file:
        for item in lista:
            file.write(item + ",")
        file.close()

def cargar_csv():
    f = open("load.csv", "r")
    load_list = f.readlines()
    name = load_list[0][:-1]
    # HP = load_list[1][:-1]
    # ATK = load_list[2][:-1]


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

# escribir_csv(Arbutus)

lista = [Arbutus.name,Arbutus.hp,Arbutus.dmg]
with open(f'./Personajes/Arbutus/Arbutus.txt', 'wt') as file:
    for item in lista:
        file.write(item + "\n")
    file.close()

print()