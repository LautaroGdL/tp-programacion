dmg=20
dmg2=50
hp=1200
energia=150
name="Lonsi"
des="Lonsi se cansó de que lo llamaran Planteonsi (porque es una planta). Así que se disfrazó de león engañandolos a todos, por eso fue coronado como rey. \n Seducido por el poder armó un torneo con los seres mas poderosos del Reinonsi."
desh1="Se pone lentes de sol y con su facheronsi baja drasticamente el autoestima del enemigo. Dañandolo en el proceso, causandole 30-70DMG. Coste 40 de energía"
desh2="Toma la chocolatada curandose 80HP y le da sed al enemigo. (como no es una stat en el juego, no ocurre nada). Coste 60 de energía."
desh3="No para de hablar. El enemigo se empieza a golpear la cabeza contra el piso, perdiendo en el proceso 50-60 neuronas (DMG). Coste 40"

def habilidad1(energia):
    import random
    if energia>=40:
        dmg_turno=random.randint(30,70)
        energia=energia-40
        heal=0
        print(f"Realizas {dmg_turno} de daño este turno")
    else:
        print("No tienes energía suficiente, elegí otra movimiento")
        dmg_turno,heal,energia=0,0,0
    return (dmg_turno,heal,energia)

def habilidad2(energia):
    import random
    if energia>=60:
        dmg_turno=0
        heal=80
        energia=energia-60
        print(f"Te curas {heal} de vida este turno")
    else:
        print("No tienes energía suficiente, elegí otra movimiento")
        dmg_turno,heal,energia=0,0,0
    return(dmg_turno,heal,energia)

def habilidad3(energia):
    import random
    if energia==40:
        heal=0
        dmg_turno=random.randint(50,60)
        print(f"Te curas {heal}")
    else:
        print("No tienes energía suficiente, elegí otra movimiento")
        dmg_turno,heal,energia=0,0,0
    return(dmg_turno,heal,energia)