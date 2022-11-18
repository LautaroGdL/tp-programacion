dmg=15
dmg2=35
hp=800
energia=150
name="Lonsi"
des="Lonsi se cansó de que lo llamaran Planteonsi (porque es una planta). Así que se disfrazó de león engañandolos a todos, por eso fue coronado como rey. \n Seducido por el poder armó un torneo con los seres mas poderosos del Reinonsi.\n"
desh1="Se pone lentes de sol y con su facheronsi baja drasticamente tu autoestima. Dañandote en el proceso, causandole 30-70DMG. Coste 40 de energía\n"
desh2="Toma la chocolatada curandose 80HP y te da sed. (como no es una stat en el juego, no ocurre nada). Coste 60 de energía.\n"
desh3="No para de hablar. Hace que que quieras golpearte la cabeza contra el piso, perdiendo en el proceso 50-60 neuronas (DMG). Coste 40\n"

def habilidad1(hp,energia):
    dmg_turno,heal=0,0
    import random
    if energia>=40:
        dmg_turno=random.randint(25,45)
        energia=energia-40
        heal=0
    else:
        dmg_turno,heal,energia=0,0,0
    return (dmg_turno,heal,energia)

def habilidad2(hp,energia):
    dmg_turno,heal=0,0
    import random
    if energia>=60:
        dmg_turno=0
        heal=60
        energia=energia-60
    else:
        dmg_turno,heal,energia=0,0,0
    return(dmg_turno,heal,energia)

def habilidad3(hp,energia):
    dmg_turno,heal=0,0
    import random
    if energia==80:
        heal=0
        dmg_turno=random.randint(30,70)
        energia=energia-40
    else:
        dmg_turno,heal,energia=0,0,0
    return(dmg_turno,heal,energia)
