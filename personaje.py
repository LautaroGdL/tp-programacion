import csv 
import re

def traer_csv():
    with open('personajes.csv', 'r') as file:
        hoja_personaje = file.readlines()
        # for row in hoja_personaje:
        #     print(row)
        return hoja_personaje

lista_estadisticas=traer_csv()

def dic_prueba(lista_1:list)->dict:
    dic_1: dict = dict()
    dic_1['Id']=(lista_1[0])
    dic_1['Nombre']=(lista_1[1])
    dic_1['HP']=(lista_1[2])
    dic_1['Energia']=(lista_1[3])
    dic_1['Ataque min']=(lista_1[4])
    dic_1['Ataque max']=(lista_1[5])
    return dic_1

def dic_datos(lista_per):
    lista_dic = lista_per
    lista_personajes = []
   
    for valor in lista_dic:
        datos = valor.split(',')
        newDic = dic_prueba(datos)
        lista_personajes.append(newDic)
    return lista_personajes
    

diccionario_final = dic_datos(lista_estadisticas)    
lista_1= lista_estadisticas[0].split(',')

print(diccionario_final)

