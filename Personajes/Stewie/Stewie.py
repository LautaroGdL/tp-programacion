dmg=2
dmg2=4
hp=25
energia=50
name="Stewie"
des="Encontró su sombrero de bruja en un tacho de basura. Ahora cree que domina las artes arcanas, pero solo son sus amigos escondidos arrojando basura."
desh1="Bebe un elixir místico rejuvenecedor (una gaseosa que encontró en la basura) curandolo 15 de vida  Coste 30 de energia"
desh2="Lanza un ataque psiquico. El enemigo queda impactado de tal suciedad y por ello recibe 9 de daño. turnos Coste: 15 de energía"
desh3="Invoca proyectiles extremadamente punzantes causando 7 de daño. Coste: 10 de energía (Realmente son sus amigos arrojando pedazos de vidrio que encontraron en el camino)"

def habilidad1(hp,energia):
    dmg_turno,heal=0,0
    if energia>=30:
        heal=15
        energia=energia-30
    else:
        dmg_turno,heal,energia=0,0,0
    return(dmg_turno,heal,energia)

def habilidad2(hp,energia):
    dmg_turno,heal=0,0
    if energia>=15:
        dmg_turno=8
        energia=energia-15
    else:
        dmg_turno,heal,energia=0,0,0
    return(dmg_turno,heal,energia)

def habilidad3(hp,energia):
    dmg_turno,heal=0,0
    if energia>=10:
        dmg_turno=6
        energia=energia-10
    else:
        dmg_turno,heal,energia=0,0,0
    return(dmg_turno,heal,energia)

win="Luego de su epica batalla contra Lonsi a Stewie se le cayó el sombrero. En ese momento fue testigo de la verdad; el sombrero no era mágico.\nTodos sus grandes hechizos e invocaciones eran simplemente una farsa. Todo montado por sus amigos, quienes desde los arbustos, lo apoyaban en cada batalla.\nSu sueño de ser el rey de los magos se desplomó. Pero esto no le importó, pues se le reveló la verdad.\nNo existe mayor magia que la amistad."
lose="Tras su derrota Stewie creyó que no era lo suficientemente fuerte para ganar. Por lo que entrenó y entrenó.\nPero nunca mejoró y un día su magia desapareció."