import funcion_csv
import tools
from Personajes.Gregg import Gregg
from Personajes.Huigh import Huigh
from Personajes.Arbutus import Arbutus
from Personajes.Stewie import Stewie
from Personajes.Willy import Willy
from Personajes.Froggy import Froggy
from Personajes.Lonsi import Lonsi


 
def select_character(jugador, choice):
    menu = True
    choice = str(choice)
    while menu:
        if jugador == 1:
            # tools.time(1,tools.clear())
            tools.clear()
            tools.draw()
            seleccion_p()
            tools.draw()
            print("|Gr-egg:  1||Arbutus: 2||Huigh:   3||Stewie:  4||Willy:   5||Froggy:  6|")
            tools.draw()
            choice = ""
            choice = input("> ")

        if choice == "1":
            # tools.time(5,tools.clear())
            tools.clear()
            lista_texto=funcion_csv.leer_csv("Personajes/Gregg/Gregg_ascii.txt")
            for i in range(0, len(lista_texto)):
                print(lista_texto[i].replace("\n", ""))
            print("Hp: ",Gregg.hp ,"||","Energia: ",Gregg.energia,"||","Daño: ",Gregg.dmg,"Daño 2: ","||",Gregg.dmg2,"\n" + Gregg.des)
            funcion_csv.escribir_csv(Gregg)

        elif choice == "2":
            tools.clear()
            lista_texto=funcion_csv.leer_csv("Personajes/Arbutus/Arbutus_ascii.txt")
            for i in range(0, len(lista_texto)):
                    print(lista_texto[i].replace("\n", ""))
            print("Hp: ",Arbutus.hp ,"||","Energia: ",Arbutus.energia,"||","Daño: ",Arbutus.dmg,"Daño 2: ","||",Arbutus.dmg2,"\n" + Arbutus.des)
            funcion_csv.escribir_csv(Arbutus)

        elif choice == "3":
            tools.clear()
            lista_texto=funcion_csv.leer_csv("Personajes/Huigh/Huigh_ascii.txt")
            for i in range(0, len(lista_texto)):
                    print(lista_texto[i].replace("\n", ""))
            print("Hp: ",Huigh.hp ,"||","Energia: ",Huigh.energia,"||","Daño: ",Huigh.dmg,"Daño 2: ","||",Huigh.dmg2,"\n" + Huigh.des)
            funcion_csv.escribir_csv(Huigh)

        elif choice == "4":
            tools.clear()
            lista_texto=funcion_csv.leer_csv("Personajes/Stewie/Stewie_ascii.txt")
            for i in range(0, len(lista_texto)):
                    print(lista_texto[i].replace("\n", ""))
            print("Hp: ",Stewie.hp ,"||","Energia: ",Stewie.energia,"||","Daño: ",Stewie.dmg,"Daño 2: ","||",Stewie.dmg2,"\n" + Stewie.des)
            funcion_csv.escribir_csv(Stewie)

        elif choice == "5":
            tools.clear()
            lista_texto=funcion_csv.leer_csv("Personajes/Willy/Willy_ascii.txt")
            for i in range(0, len(lista_texto)):
                    print(lista_texto[i].replace("\n", ""))
            print("Hp: ",Willy.hp ,"||","Energia: ",Willy.energia,"||","Daño: ",Willy.dmg,"Daño 2: ","||",Willy.dmg2,"\n" + Willy.des)
            funcion_csv.escribir_csv(Willy)

        elif choice == "6":
            tools.clear() 
            lista_texto=funcion_csv.leer_csv("Personajes/Froggy/Froggy_ascii.txt")
            for i in range(0, len(lista_texto)):
                    print(lista_texto[i].replace("\n", ""))
            print("Hp: ",Froggy.hp ,"||","Energia: ",Froggy.energia,"||","Daño: ",Froggy.dmg,"Daño 2: ","||",Froggy.dmg2,"\n" + Froggy.des)
            funcion_csv.escribir_csv(Froggy)

        elif choice == "lonsi":
            tools.clear() 
            lista_texto=funcion_csv.jefe_csv()
            for i in range(0, len(lista_texto)):
                    print(lista_texto[i].replace("\n", ""))
            print("Hp: ",Lonsi.hp ,"||","Energia: ",Lonsi.energia,"||","Daño: ",Lonsi.dmg,"Daño 2: ","||",Lonsi.dmg2,"\n" + Lonsi.des)
            


        elif choice == "0":
            menu = False
            seleccionar_personaje= False
            # stats_personaje=funcion_csv.escribir_csv()
            break
        


        else:
            continue
        if jugador == 0:
            menu = False
        else:
            print()
            seleccionar_personaje = input("Seleccionar este personaje? \nElija: \n\nAceptar: 1 \nVolver: Otra tecla \n> ").lower()

            while seleccionar_personaje:
                tools.clear()
                if seleccionar_personaje == "Aceptar" or seleccionar_personaje == "1":
                    menu = False
                    seleccionar_personaje= False
                    # stats_personaje=funcion_csv.escribir_csv()
                else:
                    seleccionar_personaje = False
                    menu = True
    tools.clear()

seleccion_texto=funcion_csv.leer_ascii("seleccion_ascii.txt")
def seleccion_p():
    for i in range(0, len(seleccion_texto)):
        print(seleccion_texto[i].replace("\n", ""))

