dmg=50
dmg2=60
hp=450
energia=150
<<<<<<< HEAD
name="Gr-egg"
des="Ganó su apodo por su extravagante forma de hablar. \n Su arma de elección es cuchara, su mejor amigo pez espada. \n Forman un equipo muy balanceado y nutritivo (?)\n"
desh1="Gr-egg pega un cabezaso el cual infringe su daño base + 20. Coste=80 energia\n"
desh2="Cuchara le roba vida al enemigo y cura a Gr-egg. 50 DMG Coste=60 energía\n"
desh3="El pez espada se mueve sin control Golpeando 1-3 veces, infligiendo de 35-55 de daño x cada golpe. Coste=40 energía\n"
=======
name="Gregg"
des="Ganó su apodo por su extravagante forma de hablar. \n Su arma de elección es cuchara, su mejor amigo pez espada. \n Forman un equipo muy balanceado y nutritivo (?)"
desh1="Gr-egg pega un cabezaso el cual infringe su daño base + 20. Coste=80 energia"
desh2="Cuchara le roba vida al enemigo y cura a Gr-egg.  Coste=60 energía"
desh3="El pez espada se mueve sin control Golpeando 1-3 veces, infligiendo de 35-55 de daño x cada golpe. Coste=40 energía"
>>>>>>> 44f61d7b8a88fb67ee981f588822be07c5d83776

def habilidad1 (hp,energia):
    import random
    if energia>=80:
        dmg1=random.randint(50, 60)
        dmg_turno=dmg1
        energia=energia-80
        heal=0
        print(f"Realizas {dmg_turno} de daño este turno\n")
    else:
        print("No tienes energía suficiente, elegí otra movimiento\n")
        dmg_turno,heal,energia=0,0,0
    return (dmg_turno,heal,energia)

def habilidad2 (hp,energia):
    if energia>=60:
        heal=50
        energia=energia-60
        dmg_turno=heal
        print(f"Te curas {heal} de daño y realizas {dmg_turno} de daño\n")
    else:
        print("No tienes energía suficiente, elegí otra movimiento\n")
        dmg_turno,heal,energia=0,0,0
    return (dmg_turno,heal,energia)

def habilidad3 (hp,energia):
    import random
    if energia>=40:
        times=random.randint(1,3)
        for i in range (times):
            dtimes=random.randint(33,44)
            dmg_turno=dmg_turno+dtimes
        energia=energia-40
        heal=0
        print(f"Realizas {dmg_turno} de daño este turno\n")
    else:
        print("No tienes energía suficiente, elegí otra movimiento\n")
        dmg_turno,heal,energia=0,0,0
    return (dmg_turno,heal,energia)

win="Durante el torneo Gr-egg tuvo muchas revelaciones.\n Respondió muchas dudas. Se aclaró(como la clara del huevo) las cosas consigo mismo.\n Tras su victoria quedó atónito. Encontró la respuesta.\n Supo quien vino primero, si el huevo o la gallina.\n Con un tono un tanto elegante pero extraño dijo:\n 'Cuchara. Luego de tantos años encontré la respuesta. Quien vino primero. Fue...'\n"
lose="El ultimo ataque de Lonsi fue devastador para Gr-egg. Le agrietó la cáscara.\n Estas cicatrices harían creer al huevo que ya era su momento.\n Tenía miedo. Había oído historias de lo que les pasaba a los huevos que agrietaban.\n Se convertían en algo espantoso. Un polluelo.\n Pero no. Solo se agritó por el golpe. Esto Gr-egg nunca lo supo, por lo que vivió el resto de sus días con miedo\n"