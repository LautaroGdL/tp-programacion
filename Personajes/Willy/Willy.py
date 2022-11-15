dmg=45
dmg2=60
hp=450
energia=150
name="Willy"
des="Un famoso socorrista conocido por su gran velocidad en el agua, su frase célebre es 'todo gracias al salvavidas'. \n Si lo ves no toques su salvavidas, pierde sus estribos cuando alguien lo hace."
desh1="Se arroja heroicamente al agua, salvando una persona y dañando permanentemente el autoestima del enemigo. Causandole 120 de daño. Coste=90 energia"
desh2="Lanza su salvavidas como un boomerang, dañando 3 veces al enemigo haciendo 15-20 de daño cada golpe. Coste: 30 energia"
desh3="Se coloca unos flotadores que tiene guardados, aumentando su moral y regenerando 70 de vida. Coste: 60 energia"

def habilidad1(energia):
    if energia>=90:
        dmg_turno=120
        heal=0
        energia=energia-90
        print(f"Realizaste {dmg_turno} de daño este turno.")
    else:
        print("No tienes energía suficiente, elegí otra movimiento")
        dmg_turno,heal,energia=0,0,0
    return(dmg_turno,heal,energia)

def habilidad2(energia):
    import random
    if energia>=30:
        for i in range (3):
            dtimes=random.randint(15-20)
            dmg_turno=dmg_turno+dtimes
        energia=energia-30
        heal=0
        print(f"Realizaste {dmg_turno} de daño este turno.")
    else:
        print("No tienes energía suficiente, elegí otra movimiento")
        dmg_turno,heal,energia=0,0,0
    return(dmg_turno,heal,energia)

def habilidad3(energia):
    if energia>=60:
        heal=70
        dmg_turno=0
        print(f"Te curaste {heal} de vida este turno.")
    else:
        print("No tienes energía suficiente, elegí otra movimiento")
        dmg_turno,heal,energia=0,0,0
    return(dmg_turno,heal,energia)