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
    '1': ('Ataque', ataque),
    '2': ('Habilidades', habilidad),
    '3': ('Resguardar', resguardar),
    '4': ('Defensa', defensa),
    '5': ('Salir', salir)
}
    generar_menu(opciones, '5')

def menu_habilidad():
    opciones = {
    '1': ('$hab1', habilidad1),
    '2': ('$hab2', habilidad2),
    '3': ('Salir', salir)
    }
    generar_menu(opciones, '2')
    

    

def ataque():
    print('Elegiste la opción Ataque')

def habilidad():
    print('Elegiste la opción Habilidades')
    menu_habilidad()

def habilidad1():
    print('Utilizaste $hab1')

def habilidad2():
    print('Utilizaste $hab2')

def resguardar():
    print('Elegiste la opción Reguardar')

def defensa():
    print('Elegiste la opción Defender')

def salir():
    print('Saliste al menu')
    print()
    menu_principal()

if __name__ == '__main__':
    menu_principal()