dmg=30
dmg2=60
hp=375
energia=150
name="Stewie"
des="Encontró su sombrero en un tacho de basura. Ahora cree que domina las artes arcanas, pero solo son sus amigos escondidos arrojando basura."
desh1="Bebe un elixir místico rejuvenecedor (una gaseosa que encontró en la basura) curandolo 100 de vida  Coste 100 de energia"
desh2="Lanza un ataque psiquico. El enemigo queda impactado de tal suciedad y por ello recibe 90 de daño. turnos Coste: 70 de energía"
desh3="Invoca proyectiles extremadamente punzantes causando 60 de daño. Coste: 20 de energía (Realmente son sus amigos arrojando pedazos de vidrio que encontraron en el camino)"

def habilidad1(energia,hp):
    if energia>=100:
        heal=100
        hp=hp+heal
        energia=energia-100
        print(f"Te curas {heal} de vida este turno")
    else:
        print("No tienes energía suficiente")
    return(hp,energia)

def habilidad2(energia):
    if energia>=70:
        dmg_turno=90
        energia=energia-70
        print(f"Realizas {dmg_turno} de daño este turno")
    else:
        print("No tienes energía suficiente")
    return(energia,dmg_turno)

def habilidad3(energia):
    if energia>=20:
        dmg_turno=60
        energia=energia-20
        print(f"Realizas {dmg_turno} de daño este turno")
    else:
        print("No tienes energía suficiente")
    return(dmg_turno, energia)



