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
            print("1: Modo Arcade")
            print("2: Modo Versus")
            print("3: Galeria")
            print("4: Reglas")
            print("5: Salir del juego")
            print()
            tools.draw()
            if rules:
                tools.clear()
                reglas_p()
                print()
                print("-Elegir a un personaje con el cual jugaras el modo Arcade y Modo Versus\n-Modo Arcade: Pelear contra 5 oponentes y un jefe final para completar la historia de tu personaje.\n-Modo Versus: Elige a un personaje y lucha contra la maquina.\n\nDiviertete y gana!!!")
                rules = False
                choice = ""
                input("> ")
            else:
                choice = input("> ")
                
            #Opciones
            if choice == "1":
                '''Inicia el Modo Arcade '''
                tools.clear()
                tools.draw()
                user = input("Escribe tu nombre: ")
                funcion_csv.guardar_nombre(user)
                menu = False
                play = True
            elif choice == "2":
                '''Inicia el Modo Versus'''
                tools.clear()
                tools.draw()
                user = input("Escribe tu nombre: ")
                funcion_csv.guardar_nombre(user)
                menu = False
                play = True
            elif choice == "3":
                tools.clear()
                tools.draw()
                galeria_personaje.galeria()
                print(">")
            elif choice == "4":
                tools.clear()
                tools.draw()
                rules = True
            elif choice == "5":
                quit()
                  
    
        while play:
            if choice == "1":
                tools.clear()
                Unturno.arcade()
                play = False
                menu = True
            elif choice == "2":
                tools.clear()
                Unturno.versus()
                play = False
                menu = True

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

reglas_texto=funcion_csv.leer_csv("Ascii/reglas_ascii.txt")
def reglas_p():
    for i in range(0, len(reglas_texto)):
        print(reglas_texto[i].replace("\n", ""))

# lista_1= lista_texto[0].split(' ')
# print(lista_texto[0].replace("\n", ""))
# print(lista_texto[1].replace("\n", ""))
# print(lista_texto[2].replace("\n", ""))
# print(lista_texto[3].replace("\n", ""))
# print(lista_texto[4].replace("\n", ""))
# print(lista_texto[5].replace("\n", ""))
# print(lista_texto[6].replace("\n", ""))


