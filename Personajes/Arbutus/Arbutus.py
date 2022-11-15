name="Arbutus"
dmg=40
dmg2=45
hp=600
energia=150
des="Sus hojas huyeron del miedo que inspira su apariencia, pero en el interior posee un corazón de roble. \n Adora enseñar botánica pero suele ir por las ramas mientras habla. "
desh1="Emplea sus ramas como latigos, realizando 100 de daño. Coste: 90 energía"
desh2="Se come un Alfajor el cual cura un '30%' de su vida max. Coste:70 energía "
desh3="Golpea al piso entre 3 a 4 veces con sus raices causando 20 a 25 con cada golpe. Coste:50 energía"
def habilidad1 (dmg,dmg2,energia):
    if energia>=90:
        dmg_turno=100
        energia=energia-90
        print(f"Realizas {dmg_turno} de daño este turno")

    else:
        print("No tienes energía suficiente")
        return (dmg_turno, energia)

def habilidad2 (hp,dmg,dmg2,energia):
    if energia>=70:
        heal=heal+(hp*(30/100))
        hp=heal+hp
        energia=energia-90

        print(f"Te curas {heal} de vida")
    else:
        print("No tienes energía suficiente")
        return (heal, energia)

def habilidad3 (energia):
    import random
    if energia>=60:
        times=random.randint(3,4)
        for i in range (times):
            dtimes=random.randint(20,25)
            dmg_turno=dmg_turno+dtimes
        energia=energia-60
        print(f"Realizas {dmg_turno} de daño este turno")
    else:
        print("No tienes energía suficiente")
        return (dmg_turno, energia)