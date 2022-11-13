import funcion_csv
import clear
import draw
from Personajes.Gregg import Gregg
from Personajes.Huigh import Huigh
from Personajes.Arbutus import Arbutus
from Personajes.Stewie import Stewie
from Personajes.Willy import Willy
from Personajes.Froggy import Froggy
 
def select_character():
    run = True
    menu = True

    while run:
        clear.clear()
        draw.draw()
        print("Seleccione a su personaje: ")
        print("|Gr-egg: 1° \n|Arbutus: 2° \n|Huigh: 3° \n|Stewie: 4° \n|Willy: 5° \n|Froggy: 6°")
        choice = ""
        choice = input("> ")

        if choice == "1":
            lista_texto=funcion_csv.traer_csv("Personajes/Gregg/Gregg_ascii.txt")
            for i in range(0, len(lista_texto)):
                print(lista_texto[i].replace("\n", ""))
            print("Hp: ",Gregg.hp ,"||","Energia: ",Gregg.energia,"||","Daño: ",Gregg.dmge)

        if choice == "2":
                lista_texto=funcion_csv.traer_csv("Personajes/Arbutus/Arbutus_ascii.txt")
                for i in range(0, len(lista_texto)):
                    print(lista_texto[i].replace("\n", ""))
                print("Hp: ",Arbutus.hp ,"||","Energia: ",Arbutus.energia,"||","Daño: ",Arbutus.dmge)

        if choice == "3":
                lista_texto=funcion_csv.traer_csv("Personajes/Huigh/Huigh_ascii.txt")
                for i in range(0, len(lista_texto)):
                    print(lista_texto[i].replace("\n", ""))
                print("Hp: ",Huigh.hp ,"||","Energia: ",Huigh.energia,"||","Daño: ",Huigh.dmge)

        if choice == "4":
                lista_texto=funcion_csv.traer_csv("Personajes/Stewie/Stewie_ascii.txt")
                for i in range(0, len(lista_texto)):
                    print(lista_texto[i].replace("\n", ""))
                print("Hp: ",Stewie.hp ,"||","Energia: ",Stewie.energia,"||","Daño: ",Stewie.dmge)

        if choice == "5":
                lista_texto=funcion_csv.traer_csv("Personajes/Willy/Willy_ascii.txt")
                for i in range(0, len(lista_texto)):
                    print(lista_texto[i].replace("\n", ""))
                print("Hp: ",Willy.hp ,"||","Energia: ",Willy.energia,"||","Daño: ",Willy.dmge)

        if choice == "6":
                lista_texto=funcion_csv.traer_csv("Personajes/Froggy/Froggy_ascii.txt")
                for i in range(0, len(lista_texto)):
                    print(lista_texto[i].replace("\n", ""))
                print("Hp: ",Froggy.hp ,"||","Energia: ",Froggy.energia,"||","Daño: ",Froggy.dmge)

select_character()