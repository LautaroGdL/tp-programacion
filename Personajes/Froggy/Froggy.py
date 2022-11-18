dmg=50
dmg2=65
hp=375
energia=150
name="Froggy"
des="Su pasión por el origami es tan grande que su cuerpo se volvió uno. \n Gracias a su poco peso ganó mucha agilidad, pero ahora odia el viento.\n"
desh1="Vuela (evitando el viento) con el fin de envestir al enemigo causando 100 de DMG. Coste 100 de energía\n"
desh2="Con su pierna filosa, corta al enemigo 40-70 (DMG) y se cura 40 de HP. 60 Coste de energía\n"
desh3="Arroja un cisne de origami (que a veces usa como sombrero) causando 75-85 de DMG. Coste 50 de energía\n"

def habilidad1(hp,energia):
    dmg_turno,heal=0,0
    if energia>=100:
        dmg_turno=100
        energia=energia-100
    else:
        dmg_turno,heal,energia=0,0,0
    return(dmg_turno,heal,energia)

def habilidad2(hp,energia):
    dmg_turno,heal=0,0
    import random
    if energia>=60:
        dmg_turno=random.randint(45,70)
        heal=40
        energia=energia-60
    else:
        dmg_turno,heal,energia=0,0,0
    return(dmg_turno,heal,energia)

def habilidad3(hp,energia):
    dmg_turno,heal=0,0
    import random
    if energia>=50:
        dmg_turno=random.randint(70,85)
        energia=energia-50
    else:
        dmg_turno,heal,energia=0,0,0
    return(dmg_turno,heal,energia)

win="Su victoria ante Lonsi no significaba nada para Froggy.\n Todo este torneo no era mas que un mal necesario para llevar a cabo su verdadero plan.\n Un plan repleto de odio, uno que viene planificando cada detalle desde pequeño.\n Esto solo lo podría llevar a cabo alguien tan temerario como un sapo origami podría hacer:\n Declararle la guerra al aire.\n"
lose="Lonsi asestó el ultimo golpe. Y con el Froggy desapareció.\n Los espectadores creerían que fue obra de Lonsi. Pero no.\n Fue el viento. El viento se llevó a Froggy.\n"