dmg=80
dmg2=100
hp=350
energia=150
name="Froggy"
des="Su pasión por el origami es tan grande que su cuerpo se volvió uno. \n Gracias a su poco peso ganó mucha agilidad, pero ahora odia el viento\n"
desh1="Vuela embistiendo al enemigo causando 140 de DMG.Coste 100 de energía\n"
desh2="Corta al enemigo realizando 40-70 DMG y se cura un '40%' del daño realizado. 50 coste de energía\n"
desh3="Arroja un cisne de origami causando 90-110 de DMG. Coste 40 de energía\n"

def habilidad1(hp,energia):
    if energia>=100:
        dmg_turno=120
        heal=0
        energia=energia-100
        print(f"Realizaste {dmg_turno} de daño este turno.\n")
    else:
        print("No tienes energía suficiente, elegí otra movimiento\n")
        dmg_turno,heal,energia=0,0,0
    return(dmg_turno,heal,energia)

def habilidad2(hp,energia):
    import random
    if energia>=50:
        dmg_turno=random.randint(40,70)
        heal=dmg_turno+(dmg_turno*(40/100))
        energia=energia-50
        print(f"Realizaste {dmg_turno} de daño y te curas {heal} este turno.\n")
    else:
        print("No tienes energía suficiente, elegí otra movimiento\n")
        dmg_turno,heal,energia=0,0,0
    return(dmg_turno,heal,energia)

def habilidad3(hp,energia):
    import random
    if energia>=40:
        dmg_turno=random.randint(90,110)
        energia=energia-40
        heal=0
        print(f"Realizaste {dmg_turno} de daño este turno.\n")
    else:
        print("No tienes energía suficiente, elegí otra movimiento\n")
        dmg_turno,heal,energia=0,0,0
    return(dmg_turno,heal,energia)

win="Su victoria ante Lonsi no significaba nada para Froggy.\n Todo este torneo no era mas que un mal necesario para llevar a cabo su verdadero plan.\n Un plan repleto de odio, uno que viene planificando cada detalle desde pequeño.\n Esto solo lo podría llevar a cabo alguien tan temerario como un sapo origami podría hacer:\n Declararle la guerra al aire.\n"
lose="Lonsi asestó el ultimo golpe. Y con el Froggy desapareció.\n Los espectadores creerían que fue obra de Lonsi. Pero no.\n Fue el viento. El viento se llevó a Froggy.\n"