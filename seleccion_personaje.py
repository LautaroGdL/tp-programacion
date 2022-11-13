import funcion_csv
import clear
import draw
from Personajes.Gregg import Gregg
 
def select_character():
    run = True
    menu = True


    print("Seleccione a su personaje: ")
    choice = ""
    choice = input("< > ")

    if choice == "1":
        lista_texto=funcion_csv.traer_csv("Personajes/Gregg/Gregg_ascii.txt")
        for i in range(0, len(lista_texto)):
            print(lista_texto[i].replace("\n", ""))
        print("Hp: ",Gregg.hp ,"||","Energia: ",Gregg.energia,"||","Daño: ",Gregg.dmge)

    if choice == "2":
            lista_texto=funcion_csv.traer_csv("Personajes/Gregg/Gregg_ascii.txt")
            for i in range(0, len(lista_texto)):
                print(lista_texto[i].replace("\n", ""))
                

    if choice == "3":
            lista_texto=funcion_csv.traer_csv("Personajes/Gregg/Gregg_ascii.txt")
            for i in range(0, len(lista_texto)):
                print(lista_texto[i].replace("\n", ""))

    if choice == "4":
            lista_texto=funcion_csv.traer_csv("Personajes/Gregg/Gregg_ascii.txt")
            for i in range(0, len(lista_texto)):
                print(lista_texto[i].replace("\n", ""))

    if choice == "5":
            lista_texto=funcion_csv.traer_csv("Personajes/Gregg/Gregg_ascii.txt")
            for i in range(0, len(lista_texto)):
                print(lista_texto[i].replace("\n", ""))

    if choice == "6":
            lista_texto=funcion_csv.traer_csv("Personajes/Gregg/Gregg_ascii.txt")
            for i in range(0, len(lista_texto)):
                print(lista_texto[i].replace("\n", ""))

select_character()