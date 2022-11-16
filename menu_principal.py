import galeria_personaje
import funcion_csv
import tools
import os


# def save():
#     list = [
#         name,
#         str(HP),
#         str(ATK)
#     ]

#     f = open("load.csv", "w")

#     for item in list:
#         f.write(item + "\n")
#     f.close()

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
            print("1: Arcade")
            print("2: Versus")
            print("3: Galeria")
            print("4: Reglas")
            print("5: Salir del juego")

            if rules:
                print("Estas son las reglas del juego: \n-Elegir a un personaje con el cual jugsras el modo Arcade o Versus.-Modo Arcade: Pelear contra 5 oponentes y un jefe final para completar la historia de tu personaje. \n-Modo Versus: Pelear contra otro jugador o la máquina")
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
                menu = False
                play = True
            elif choice == "2":
                
                tools.clear()
                tools.draw()
                print("Bienvenido" + name + "!")
                print("> ")
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
            #save()#autosave
                
            tools.clear()
            tools.draw()
            print("0 - Guardar y salir")
            tools.draw()

            dest = input("#")

            if dest == "0":
                play = False
                menu = True
                #save()       

lista_texto=funcion_csv.leer_csv("ascii_texto.txt")
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


