dmg=1
dmg2=3
hp=60
energia=50
name="Lonsi"
des="Lonsi se cansó de que lo llamaran Planteonsi (porque es una planta). Así que se disfrazó de león engañandolos a todos, por eso fue coronado como rey. Seducido por el poder armó un torneo con los seres mas poderosos del Reinonsi."
desh1="Se pone lentes de sol y con su facheronsi baja drasticamente tu autoestima. Dañandote en el proceso, causandole 1-4DMG. Coste 20 de energía"
desh2="Toma la chocolatada curandose 9HP y te da sed. (como no es una stat en el juego, no ocurre nada). Coste 30 de energía."
desh3="No para de hablar. Hace que que quieras golpearte la cabeza contra el piso, perdiendo en el proceso 1-4 neuronas (DMG). Coste 20 de energía"

def habilidad1(hp,energia):
    dmg_turno,heal=0,0
    import random
    if energia>=20:
        dmg_turno=random.randint(1,4)
        energia=energia-20
        heal=0
    else:
        dmg_turno,heal,energia=0,0,0
    return (dmg_turno,heal,energia)

def habilidad2(hp,energia):
    dmg_turno,heal=0,0
    if energia>=30:
        heal=9
        energia=energia-30
    else:
        dmg_turno,heal,energia=0,0,0
    return(dmg_turno,heal,energia)

def habilidad3(hp,energia):
    dmg_turno,heal=0,0
    import random
    if energia>=20:
        dmg_turno=random.randint(1,4)
        energia=energia-20
    else:
        dmg_turno,heal,energia=0,0,0
    return(dmg_turno,heal,energia)

win=""
lose=""