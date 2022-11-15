dmg=45
dmg2=75
hp=400
energia=150
name="Huigh"
des="No se sabe mucho de Huigh, pero según testimonios '...de repente se acercó tremendo mono muchacho, encima agarra y me dice 'tenes una banana?'. Más firme si, la banana no se le niega a nadie. Todo bien con el mono, tranquilo, manso. Es contundente la cosa, imaginate que hasta se volvió pirata porque le robaron una sola banana, no se come ni una el monki."
desh1="Llama a su barco, este dispara 3 bolas de cañón cada una infringe 60 de daño con un '50%' de golpear al objetivo. Coste 100 de energía"
desh2="Embiste y apuñala al objetivo causando DMG 'base-10%', pero se cura un '50%' del daño realizado. Coste 60 de energía"
desh3="Se come una banana regenerando 80HP, esta crazy el monki. Coste 80 de energía"

def habilidad1(energia):
    import random
    if energia>=100:
        for i in range (3):
            prob=random.randint(1,2)
            if prob==1:
                dmg_turno=dmg_turno+60
            elif prob==2:
                dmg_turno=dmg_turno
        energia=energia-80
        heal=0
        print(f"Realizas {dmg_turno} de daño este turno")
    else:
        print("No tienes energía suficiente, elegí otra movimiento")
        dmg_turno,heal,energia=0,0,0
    return (dmg_turno,heal,energia)

def habilidad2(energia,dmg,dmg2):
    import random
    if energia>=60:
        prob=random.randint(dmg, dmg2)
        dmg_turno=dmg_turno-(prob*(10/100))
        heal=heal+(dmg_turno/2)
        print(f"Realizas {dmg_turno} de daño este turno y robas {heal} de vida este turno")
    else:
        print("No tienes energía suficiente, elegí otra movimiento")
        dmg_turno,heal,energia=0,0,0
    return(dmg_turno,heal,energia)

def habilidad3(energia):
    if energia==80:
        heal=80
        dmg_turno=0
        print(f"Te curas {heal}")
    else:
        print("No tienes energía suficiente, elegí otra movimiento")
        dmg_turno,heal,energia=0,0,0
    return(dmg_turno,heal,energia)
