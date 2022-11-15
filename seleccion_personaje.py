import funcion_csv
import tools
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
        while menu:
            # tools.time(1,tools.clear())
            tools.clear()
            tools.draw()
            print("Seleccione a su personaje: ")
            print("|Gr-egg:  1| \n|Arbutus: 2| \n|Huigh:   3| \n|Stewie:  4| \n|Willy:   5| \n|Froggy:  6|")
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
            
            else:
                continue
        
            print()
            seleccionar_personaje = input("Seleccionar este personaje? \nElija: \n\nAceptar: 1 \nVolver: Otra tecla \n> ").lower()

            while seleccionar_personaje:
                tools.clear()
                if seleccionar_personaje == "Aceptar":
                    menu = False
                    # stats_personaje=funcion_csv.escribir_csv()
                else:
                    seleccionar_personaje = False
                    menu = True

select_character()
