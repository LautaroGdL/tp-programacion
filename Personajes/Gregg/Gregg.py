dmg=50
dmg2=60
hp=450
energia=150
name="Gr-egg"
des="Ganó su apodo por su extravagante forma de hablar. \n Su arma de elección es cuchara, su mejor amigo pez espada. \n Forman un equipo muy balanceado y nutritivo (?)"
desh1="Gr-egg pega un cabezaso el cual infringe su daño base + 20. Coste=80 energia"
desh2="Cuchara le roba vida al enemigo y cura a Gr-egg.  Coste=60 energía"
desh3="El pez espada se mueve sin control Golpeando 1-3 veces, infligiendo de 35-55 de daño x cada golpe. Coste=40 energía"

def habilidad1 (dmg,dmg2,energia):
    import random
    if energia>=80:
        dmg1=random.randint(dmg, dmg2)
        dmg_turno=dmg1
        energia=energia-80
        heal=0
        print(f"Realizas {dmg_turno} de daño este turno")
    else:
        print("No tienes energía suficiente, elegí otra movimiento")
        dmg_turno,heal,energia=0,0,0
    return (dmg_turno,heal,energia)

def habilidad2 (hp,energia):
    if energia>=60:
        heal=45
        hp=hp+heal
        energia=energia-60
        dmg_turno=heal
        print(f"Te curas {heal} de daño y realizas {dmg_turno} de daño")
    else:
        print("No tienes energía suficiente, elegí otra movimiento")
        dmg_turno,heal,energia=0,0,0
    return (dmg_turno,heal,energia)

def habilidad3 (energia):
    import random
    if energia>=40:
        times=random.randint(1,3)
        for i in range (times):
            dtimes=random.randint(33,44)
            dmg_turno=dmg_turno+dtimes
        energia=energia-40
        heal=0
        print(f"Realizas {dmg_turno} de daño este turno")
    else:
        print("No tienes energía suficiente, elegí otra movimiento")
        dmg_turno,heal,energia=0,0,0
    return (dmg_turno,heal,energia)
        