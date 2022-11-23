dmg=3
dmg2=5
hp=23
energia=50
name="Froggy"
des="Su pasión por el origami es tan grande que su cuerpo se volvió uno. Gracias a su poco peso ganó mucha agilidad, pero ahora odia el viento."
desh1="Vuela (evitando el viento) con el fin de envestir al enemigo causando 12 de DMG. Coste 30 de energía"
desh2="Con su pierna filosa, corta al enemigo 2-7 (DMG) y se cura 40 de HP. 20 Coste de energía"
desh3="Arroja un cisne de origami (que a veces usa como sombrero) causando 5-9 de DMG. Coste 20 de energía"

def habilidad1(hp,energia):
    dmg_turno,heal=0,0
    if energia>=30:
        dmg_turno=12
        energia=energia-30
    else:
        dmg_turno,heal,energia=0,0,0
    return(dmg_turno,heal,energia)

def habilidad2(hp,energia):
    dmg_turno,heal=0,0
    import random
    if energia>=20:
        dmg_turno=random.randint(2,7)
        heal=10
        energia=energia-20
    else:
        dmg_turno,heal,energia=0,0,0
    return(dmg_turno,heal,energia)

def habilidad3(hp,energia):
    dmg_turno,heal=0,0
    import random
    if energia>=20:
        dmg_turno=random.randint(5,9)
        energia=energia-20
    else:
        dmg_turno,heal,energia=0,0,0
    return(dmg_turno,heal,energia)

win="Su victoria ante Lonsi no significaba nada para Froggy. Todo este torneo no era mas que un mal necesario para llevar a cabo su verdadero plan. Un plan repleto de odio, uno que viene planificando cada detalle desde pequeño.\n Esto solo lo podría llevar a cabo alguien tan temerario como un sapo origami podría hacer: Declararle la guerra al aire.\n"
lose="Lonsi asestó el ultimo golpe. Y con el Froggy desapareció. Los espectadores creerían que fue obra de Lonsi. Pero no. Fue el viento. El viento se llevó a Froggy.\n"