dmg=30
dmg2=60
hp=375
energia=150
name="Stewie"
des="Encontró su sombrero de bruja en un tacho de basura. Ahora cree que domina las artes arcanas, pero solo son sus amigos escondidos arrojando basura.\n"
desh1="Bebe un elixir místico rejuvenecedor (una gaseosa que encontró en la basura) curandolo 100 de vida  Coste 100 de energia\n"
desh2="Lanza un ataque psiquico. El enemigo queda impactado de tal suciedad y por ello recibe 90 de daño. turnos Coste: 70 de energía\n"
desh3="Invoca proyectiles extremadamente punzantes causando 60 de daño. Coste: 20 de energía (Realmente son sus amigos arrojando pedazos de vidrio que encontraron en el camino)\n"

def habilidad1(hp,energia):
    dmg_turno,heal=0,0
    if energia>=100:
        heal=100
        energia=energia-100
    else:
        dmg_turno,heal,energia=0,0,0
    return(dmg_turno,heal,energia)

def habilidad2(hp,energia):
    dmg_turno,heal=0,0
    if energia>=70:
        dmg_turno=90
        energia=energia-70
    else:
        dmg_turno,heal,energia=0,0,0
    return(dmg_turno,heal,energia)

def habilidad3(hp,energia):
    dmg_turno,heal=0,0
    if energia>=20:
        dmg_turno=60
        energia=energia-20
    else:
        dmg_turno,heal,energia=0,0,0
    return(dmg_turno,heal,energia)

win="Luego de su epica batalla contra Lonsi a Stewie se le cayó el sombrero. En ese momento fue testigo de la verdad; el sombrero no era mágico.\n Todos sus hechizos e invocaciones eran simplemente una farsa. Todo montado por sus amigos, quienes desde los arbustos, lo apoyaban en cada batalla.\n Su sueño de ser el rey de los magos se desplomó.\n Pero esto no le importó, pues se dió cuenta de algo revelador. No existe mayor magia que la amistad.\n"
lose="Tras su derrota Stewie creyó que no era lo suficientemente fuerte para ganar.\n Por lo que entrenó y entrenó.\n Pero nunca mejoró y un día su magia desapareció.\n"