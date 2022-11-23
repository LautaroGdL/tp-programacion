dmg=1
dmg2=3
hp=35
energia=50
name="Arbutus"
des="Sus hojas huyeron del miedo que inspira su apariencia, pero en el interior posee un corazón de roble. Adora enseñar botánica pero suele ir por las ramas mientras habla."
desh1="Accidentalmente se tropieza aplastando al enemigo realizando al enemigo 4 de DMG. (Se disculpa y levanta nuevamente) Coste: 20 energía"
desh2="Se come un Alfajor el cual cura un 10 de vida. Coste:30 energía"
desh3="Se distrae e inconscientemente golpea al enemigo 2 a 3 veces con sus raíces causando 1 a 3 con cada golpe. Coste:30 energía"
def habilidad1 (hp,energia):
    dmg_turno,heal=0,0
    if energia>=20:
        dmg_turno=4
        energia=energia-20
    else:
        dmg_turno,heal,energia=0,0,0
    return (dmg_turno,heal,energia)

def habilidad2 (hp,energia):
    dmg_turno,heal=0,0
    if energia>=30:
        heal=15
        energia=energia-30
    else:
        dmg_turno,heal,energia=0,0,0
    return (dmg_turno,heal,energia)

def habilidad3 (hp,energia):
    dmg_turno,heal=0,0
    import random
    if energia>=30:
        times=random.randint(2,3)
        for i in range (times):
            dtimes=random.randint(1,3)
            dmg_turno=dmg_turno+dtimes
        energia=energia-30
    else:
        dmg_turno,heal,energia=0,0,0
    return (dmg_turno,heal,energia)
win="Arbutus lo supo desde el principio. Lonsi no era un león. Era una flor. Lo dedujo gracias a sus bastos conocimientos en botánica (y a que se le cayó el disfraz luego de ser derrotado).\nPero el vió algo en Lonsi que nadie hizo, a un alma gentil pero asustada, alguien con defectos pero con buenas intenciones. El vio a un gran amigo.\nComenzaron a hablar y su conexión fue natural, sintieron que tenían las mismas raíces (no porque ambos fuesen plantas).\nEl tiempo pasó.... Hoy en día son un dúo muy famoso que da conferencias sobre el medio ambiente. Sus charlas son profundas y demuestran mucho experiencia sobre el campo.\nEl problema es que hablan tanto que nunca terminan.\n"
lose="No fue capaz de desenmascarar la farsa de Lonsi. El estaba seguro de que era una flor, pero nadie le creía.\nEllo se volvió la única cosa de la que hablaba. No podía parar. No hasta que la gente lo supiera. Habló y habló, pero nadie le creyó.\nCon el tiempo fue tachado de paranoico, un loco más. Perdió su trabajo y cordura en el camino.\nHoy en día se lo puede ver por los prados repitiendo lo mismo una y otra vez: '¡Lonsi es una flor ¿No lo ven? No le crean al gobierno!'\n"