# def main(n):
#     print(n)
import os

run = True
menu = True
play = False
rules = False

HP = 100
ATK = 150

print("Bienvenido a Animalia")

def clear():
    os.system("cls")

def draw():
    print("xX-----------------------Xx")


def save():
    list = [
        name,
        str(HP),
        str(ATK)
    ]

    f = open("load.csv", "w")

    for item in list:
        f.write(item + "\n")
    f.close()

while run:
    while menu:
        clear()
        draw()
        print("1, NEW GAME")
        print("2, LOAD GAME")
        print("3, RULES")
        print("4, QUIT GAME")

        if rules:
            print("Estas son las reglas del juego: ")
            rules = False
            choice = ""
            input("> ")
        else:
            choice = input("# ")
        
        #Opciones
        if choice == "1":
            clear()
            draw()
            name = input("Escribe tu nombre: ")
            menu = False
            play = True
        elif choice == "2":
            f = open("load.csv", "r")
            load_list = f.readlines()
            name = load_list[0][:-1]
            HP = load_list[1][:-1]
            ATK = load_list[2][:-1]
            clear()
            draw()
            print("Bienvenido" + name + "!")
            print("> ")
            menu = False
            play = True
        elif choice == "3":
            rules = True
        elif choice == "4":
            quit()

    while play:
        save()#autosave

        clear()
        draw()
        print("0 - Guardar y salir")
        draw()

        dest = input("#")

        if dest == "0":
            play = False
            menu = True
            save()