dmg=80
dmg2=100
hp=350
energia=150
des="Su pasión por el origami es tan grande que su cuerpo se volvió uno. \n Gracias a su poco peso ganó mucha agilidad, pero ahora odia el viento"
desh1="Vuela embistiendo al enemigo causando 140 de DMG.Coste 100 de energía"
desh2="Corta al enemigo realizando 40-70 DMG y se cura un '40%' del daño realizado. 50 coste de energía"
desh3="Arroja un cisne de origami causando 90-110 de DMG. Coste 40 de energía"

def habilidad1(energia):
    if energia>=100:
        dmg_turno=120
        energia=energia-100
        print(f"Realizaste {dmg_turno} de daño este turno.")
    else:
        print("No tienes energía")
    return(dmg_turno,energia)

def habilidad2(energia,hp):
    import random
    if energia>=50:
        dmg_turno=random.randint(40,70)
        heal=dmg_turno+(dmg_turno*(40/100))
        hp=hp+heal
        energia=energia-50
        print(f"Realizaste {dmg_turno} de daño y te curas {heal} este turno.")
    else:
        print("No tienes energía")
    return(dmg_turno,energia,hp)

def habilidad3(energia):
    import random
    if energia>=40:
        dmg_turno=random.randint(90,110)
        energia=energia-40
        print(f"Realizaste {dmg_turno} de daño este turno.")
    else:
        print("No tienes energía")
    return(dmg_turno,energia)