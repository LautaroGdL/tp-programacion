import funcion_csv
import tools
from Personajes.Gregg import Gregg
from Personajes.Huigh import Huigh
from Personajes.Arbutus import Arbutus
from Personajes.Stewie import Stewie
from Personajes.Willy import Willy
from Personajes.Froggy import Froggy
from Personajes.Lonsi import Lonsi
 
def galeria():
    menu = True
    run = True

    while run:
        while menu:
            # tools.time(1,tools.clear())
            tools.clear()
            tools.draw()
            galeria_p()
            print()
            print("|Gr-egg:  1||Arbutus: 2||Huigh:   3||Stewie:  4||Willy:   5||Froggy:  6|||Lonsi:   7|")
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
            
            elif choice == "7":
                tools.clear() 
                lista_texto=funcion_csv.leer_csv("Personajes/Lonsi/Lonsi_ascii.txt")
                for i in range(0, len(lista_texto)):
                        print(lista_texto[i].replace("\n", ""))
                print("Nombre: ",Lonsi.name,"\n" + Lonsi.des)
            
            elif choice == "0":
                run = False
                menu = False
                break
                

            else:
                continue
        
            print()
            galeria_personaje = input("Aprete cualquier letra para volver... \n> ").lower()

            while galeria_personaje:
                tools.clear()
                if galeria_personaje == "":
                    menu = True
                    galeria_personaje= False
                    # stats_personaje=funcion_csv.escribir_csv()
                else:
                    galeria_personaje = False
                    menu = True
                    
        tools.clear()



lista_galeria=funcion_csv.leer_csv("galeria.txt")
def galeria_p():
    for i in range(0, len(lista_galeria)):
        print(lista_galeria[i].replace("\n", ""))

