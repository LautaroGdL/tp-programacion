dmg=2
dmg2=5
hp=26
energia=50
name="Gregg"
des="Ganó su apodo por su extravagante forma de hablar.\nSu arma de elección es cuchara, su mejor amigo pez espada.\nForman un equipo muy balanceado y nutritivo (?)\n"
desh1=" Gr-egg pega un cabezaso el cual infringe su daño base + 10%. Coste=20 energia"
desh2=" Cuchara con una mirada intensa le roba 15 de vida al enemigo y cura a Gr-egg. Coste=20 energía\n"
desh3=" El pez espada se mueve sin control dañando al enemigo Golpeando 1-3 veces, infligiendo de 1-5 de daño x cada golpe. Coste=30 energía\n"

def habilidad1 (hp,energia):
    dmg_turno,heal=0,0
    import random
    if energia>=20:
        dmg_turno=random.randint(3, 6)
        energia=energia-20
    else:
        dmg_turno,heal,energia=0,0,0
    return (dmg_turno,heal,energia)

def habilidad2 (hp,energia):
    dmg_turno,heal=0,0
    if energia>=30:
        heal=15
        energia=energia-20
        dmg_turno=heal
    else:
        dmg_turno,heal,energia=0,0,0
    return (dmg_turno,heal,energia)

def habilidad3 (hp,energia):
    dmg_turno,heal=0,0
    import random
    if energia>=30:
        times=random.randint(1,3)
        for i in range (times):
            dtimes=random.randint(1,4)
            dmg_turno=dmg_turno+dtimes
        energia=energia-30
        heal=0
    else:
        dmg_turno,heal,energia=0,0,0
    return (dmg_turno,heal,energia)

win="Durante el torneo Gr-egg tuvo muchas revelaciones.\n Respondió muchas dudas. Se aclaró(como la clara del huevo) las cosas consigo mismo.\n Tras su victoria quedó atónito. Encontró la respuesta.\n Supo quien vino primero, si el huevo o la gallina.\n Con un tono un tanto elegante pero extraño dijo:\n 'Cuchara. Luego de tantos años encontré la respuesta. Quien vino primero. Fue...'\n"
lose="El ultimo ataque de Lonsi fue devastador para Gr-egg. Le agrietó la cáscara.\n Estas cicatrices harían creer al huevo que ya era su momento.\n Tenía miedo. Había oído historias de lo que les pasaba a los huevos que agrietaban.\n Se convertían en algo espantoso. Un polluelo.\n Pero no. Solo se agritó por el golpe. Esto Gr-egg nunca lo supo, por lo que vivió el resto de sus días con miedo\n"