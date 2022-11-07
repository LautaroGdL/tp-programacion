import csv 
import re
def traer_csv():
    with open('personajes.csv', 'r') as file:
        hoja_personaje = file.readlines()
        # for row in hoja_personaje:
            #print(','.join([0]))
        return hoja_personaje

lista_estadisticas=traer_csv()
def dic_prueba(lista:list)->dict:
    lista_dic = lista.copy()
    dic_1 = {}
    for valor in lista_dic:
        lista_2= valor.split(',')
        dic_1['Nombre']=(lista_2[0])
        dic_1['HP']=(lista_2[1])
        dic_1['Energia']=(lista_2[2])
        dic_1['Ataque min']=(lista_2[3])
        dic_1['Ataque max']=(lista_2[4])
    return dic_1

diccionario_final = dic_prueba(lista_estadisticas)    
lista_2= lista_estadisticas[0].split(',')
print(lista_2)