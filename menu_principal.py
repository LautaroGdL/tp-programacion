import galeria_personaje
import funcion_csv
import Unturno
import tools
import os

def iniciar_juego():
    run = True
    menu = True
    play = False
    rules = False

    while run:
        while menu:
            tools.clear()
            tools.draw()
            menu_p()
            print()
            tools.draw()
            print("1: Arcade")
            print("2: Galeria")
            print("3: Reglas")
            print("4: Salir del juego")
            print()
            tools.draw()
            if rules:
                tools.clear()
                print("Reglas del juego: \n-Elegir a un personaje con el cual jugaras el modo Arcade\n-Modo Arcade: Pelear contra 5 oponentes y un jefe final para completar la historia de tu personaje.\n\nDiviertete y gana!!!")
                rules = False
                choice = ""
                input("> ")
            else:
                choice = input("> ")
                
            #Opciones
            if choice == "1":
                tools.clear()
                tools.draw()
                name = input("Escribe tu nombre: ")
                # Unturno.pelea()
                menu = False
                play = True
            elif choice == "2":
                tools.clear()
                tools.draw()
                galeria_personaje.galeria()
                print(">")
            elif choice == "3":
                tools.clear()
                tools.draw()
                rules = True
            elif choice == "4":
                quit()
                
        print("Juego terminado")
        
        while play:
                
            tools.clear()
            Unturno.pelea()
            desicion = input("Desea volver a jugar? (y/n): ")
            if desicion == "n":
                play = False
                menu = True
            elif desicion == "y":
                play = True
                       

lista_texto=funcion_csv.leer_csv("Ascii/ascii_texto.txt")
def menu_p():
    for i in range(0, len(lista_texto)):
        print(lista_texto[i].replace("\n", ""))

# lista_1= lista_texto[0].split(' ')
# print(lista_texto[0].replace("\n", ""))
# print(lista_texto[1].replace("\n", ""))
# print(lista_texto[2].replace("\n", ""))
# print(lista_texto[3].replace("\n", ""))
# print(lista_texto[4].replace("\n", ""))
# print(lista_texto[5].replace("\n", ""))
# print(lista_texto[6].replace("\n", ""))


