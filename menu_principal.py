def mostrar_menu(opciones):
    print('Seleccione una opcion: ')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

def leer_opcion(opciones):
    while(a := input('Opción: ')) not in opciones:
        print('Opcion incorrecta, vuelva a intertarlo.')
    return a

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()

def menu_principal():
    opciones = {
    '1': ('Arcade', arcade),
    '2': ('Versus', versus),
    '3': ('Galeria', galeria),
    '4': ('Salir', salir)
}
    generar_menu(opciones, '4')

    
def menu_versus():
    opciones = {
    '1': ('PvP', pvp),
    '2': ('PvE', pve),
    '3': ('Salir', salir)
    }
    generar_menu(opciones, '3')

    

def arcade():

    print('Elegiste la opción Ataque')

def versus():
    menu_versus()
    print('Elegiste la opción Habilidades')


def galeria():
    print('Utilizaste $hab1')

def menu_versus():
    print("Elegi el mode de pelea")

def pvp():
    print()
    salir()

def pve():
    print()
    salir()

def salir():
    print('Saliste al menu')
    print()
    menu_principal()

if __name__ == '__main__':
    menu_principal()