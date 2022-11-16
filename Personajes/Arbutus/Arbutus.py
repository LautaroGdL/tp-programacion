dmg=40
dmg2=45
hp=600
energia=150
name="Arbutus"
des="Sus hojas huyeron del miedo que inspira su apariencia, pero en el interior posee un corazón de roble. \n Adora enseñar botánica pero suele ir por las ramas mientras habla.\n"
desh1="Accidentalmente se tropieza aplastando al enemigo realizando al enemigo 100 de daño. (Se disculpa y levanta nuevamente) Coste: 90 energía\n"
desh2="Se come un Alfajor el cual cura un '30%' de su vida max. Coste:70 energía\n"
desh3="Se distrae e inconscientemente golpea al enemigo 3 a 4 veces con sus raíces causando 20 a 25 con cada golpe. Coste:50 energía\n"
def habilidad1 (hp,energia):
    dmg_turno,heal=0,0
    if energia>=90:
        dmg_turno=100
        energia=energia-90
    else:
        dmg_turno,heal,energia=0,0,0
    return (dmg_turno,heal,energia)

def habilidad2 (hp,energia):
    dmg_turno,heal=0,0
    if energia>=70:
        heal=heal+(hp*(30/100))
        energia=energia-90
        dmg_turno=0
    else:
        dmg_turno,heal,energia=0,0,0
    return (dmg_turno,heal,energia)

def habilidad3 (hp,energia):
    dmg_turno,heal=0,0
    import random
    if energia>=60:
        times=random.randint(3,4)
        for i in range (times):
            dtimes=random.randint(20,25)
            dmg_turno=dmg_turno+dtimes
        energia=energia-60
    else:
        dmg_turno,heal,energia=0,0,0
    return (dmg_turno,heal,energia)
win="Arbutus lo supo desde el principio. Lonsi no era un león. Era una flor. Lo dedujo gracias a sus bastos conocimientos en botánica (y a que se le cayó el disfraz luego de ser derrotado).\n Pero el vió algo en Lonsi que nadie hizo, a un alma gentil pero asustada, alguien con defectos pero con buenas intenciones. El vio a un gran amigo.\n Comenzaron a hablar y su conexión fue natural, sintieron que tenían las mismas raíces (no porque ambos fuesen plantas).\n El tiempo pasó.... Hoy en día son un dúo muy famoso que da conferencias sobre el medio ambiente. Sus charlas son profundas y demuestran mucho experiencia sobre el campo, el problema es que hablan tanto que nunca terminan.\n"
lose="No fue capaz de desenmascarar la farsa de Lonsi. El estaba seguro de que era una flor, pero nadie le creía.\n Ello se volvió la única cosa de la que hablaba. No podía parar. No hasta que la gente lo supiera. Habló y habló, pero nadie le creyó.\n Con el tiempo fue tachado de paranoico, un loco más. Perdió tanto su trabajo como su cordura en el camino. \n Se lo puede ver por los prados repitiendo lo mismo una y otra vez: '¡Lonsi es una flor ¿No lo ven? No le crean al gobierno!\n'"