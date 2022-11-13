import funcion_csv
import clear
import draw
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
            clear.clear()
            draw.draw()
            menu_p()
            print("1: Arcade")
            print("2: Versus")
            print("3: Galeria")
            print("4: Reglas")
            print("5: Salir del juego")

            if rules:
                print("Estas son las reglas del juego: \n-Elegir a un personaje con el cual jugsras el modo Arcade o Versus.-Modo Arcade: Pelear contra 5 oponentes y un jefe final para completar la historia de tu personaje. \n-Modo Versus: Pelear contra otro jugador o la máquina \n-Quedar en el ranking habiendo recibido poco daño durante el Modo historia( si se llega a hacer)")
                rules = False
                choice = ""
                input("> ")
            else:
                choice = input("# ")
                
            #Opciones
            if choice == "1":
                clear.clear()
                draw.draw()
                name = input("Escribe tu nombre: ")
                menu = False
                play = True
            elif choice == "2":
                f = open("load.csv", "r")
                load_list = f.readlines()
                name = load_list[0][:-1]
                # HP = load_list[1][:-1]
                # ATK = load_list[2][:-1]
                clear.clear()
                draw.draw()
                print("Bienvenido" + name + "!")
                print("> ")
                menu = False
                play = True
            elif choice == "3":
                clear.clear()
                draw.draw()
                print(">")
            elif choice == "4":
                clear.clear()
                draw.draw()
                rules = True
            elif choice == "5":
                quit()

        while play:
            #save()#autosave
                
            clear.clear()
            draw.draw()
            print("0 - Guardar y salir")
            draw.draw()

            dest = input("#")

            if dest == "0":
                play = False
                menu = True
                #save()       

lista_texto=funcion_csv.traer_csv("ascii_texto.txt")
# lista_1= lista_texto[0].split(' ')
# print(lista_texto[0].replace("\n", ""))
# print(lista_texto[1].replace("\n", ""))
# print(lista_texto[2].replace("\n", ""))
# print(lista_texto[3].replace("\n", ""))
# print(lista_texto[4].replace("\n", ""))
# print(lista_texto[5].replace("\n", ""))
# print(lista_texto[6].replace("\n", ""))

def menu_p():
    for i in range(0, len(lista_texto)):
        print(lista_texto[i].replace("\n", ""))

