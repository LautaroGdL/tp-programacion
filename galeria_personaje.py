import funcion_csv
import tools
from Personajes.Gregg import Gregg
from Personajes.Huigh import Huigh
from Personajes.Arbutus import Arbutus
from Personajes.Stewie import Stewie
from Personajes.Willy import Willy
from Personajes.Froggy import Froggy
 
def galeria():
    menu = True
    
    while menu:
        # tools.time(1,tools.clear())
        tools.clear()
        tools.draw()
        galeria_p()
        print()
        print("|Gr-egg:  1||Arbutus: 2||Huigh:   3||Stewie:  4||Willy:   5||Froggy:  6|")
        tools.draw()
        choice = input("> ")
        

        if choice == "1":
            # tools.time(5,tools.clear())
            tools.clear()
            lista_texto=funcion_csv.leer_csv("Personajes/Gregg/Gregg_ascii.txt")
            for i in range(0, len(lista_texto)):
                print(lista_texto[i].replace("\n", ""))
            print("Nombre: ",Gregg.name,"\n" + Gregg.des)
            
        elif choice == "2":
            tools.clear()
            lista_texto=funcion_csv.leer_csv("Personajes/Arbutus/Arbutus_ascii.txt")
            for i in range(0, len(lista_texto)):
                    print(lista_texto[i].replace("\n", ""))
            print("Nombre: ",Arbutus.name,"\n" + Arbutus.des)

        elif choice == "3":
            tools.clear()
            lista_texto=funcion_csv.leer_csv("Personajes/Huigh/Huigh_ascii.txt")
            for i in range(0, len(lista_texto)):
                    print(lista_texto[i].replace("\n", ""))
            print("Nombre: ",Huigh.name,"\n" + Huigh.des)

        elif choice == "4":
            tools.clear()
            lista_texto=funcion_csv.leer_csv("Personajes/Stewie/Stewie_ascii.txt")
            for i in range(0, len(lista_texto)):
                    print(lista_texto[i].replace("\n", ""))
            print("Nombre: ",Stewie.name,"\n" + Stewie.des)
        elif choice == "5":
            tools.clear()
            lista_texto=funcion_csv.leer_csv("Personajes/Willy/Willy_ascii.txt")
            for i in range(0, len(lista_texto)):
                    print(lista_texto[i].replace("\n", ""))
            print("Nombre: ",Willy.name,"\n" + Willy.des)

        elif choice == "6":
            tools.clear() 
            lista_texto=funcion_csv.leer_csv("Personajes/Froggy/Froggy_ascii.txt")
            for i in range(0, len(lista_texto)):
                    print(lista_texto[i].replace("\n", ""))
            print("Nombre: ",Froggy.name,"\n" + Froggy.des)
        

        else:
            continue
    
        print()
        seleccionar_personaje = input("Aprete cualquier letra para volver... \n> ").lower()

        while seleccionar_personaje:
            tools.clear()
            if seleccionar_personaje == "":
                menu = False
                seleccionar_personaje= False
                # stats_personaje=funcion_csv.escribir_csv()
            else:
                seleccionar_personaje = False
                menu = True
    tools.clear()



lista_galeria=funcion_csv.leer_csv("galeria.txt")
def galeria_p():
    for i in range(0, len(lista_galeria)):
        print(lista_galeria[i].replace("\n", ""))

