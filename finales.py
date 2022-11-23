import importar_personaje
def finales(name, win):
    importar_personaje.importar_pj
    if win == 1:
        character = importar_personaje.importar_pj(name)
        print(character.win)
        input("Continuar: Enter ")
    else:
        character = importar_personaje.importar_pj(name)
        print(character.lose)
        input("Continuar: Enter ")
