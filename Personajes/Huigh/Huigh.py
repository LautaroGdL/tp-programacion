dmg=2
dmg2=4
hp=26
energia=50
name="Huigh"
des="No se sabe mucho de Huigh, pero según testimonios '...de repente se acercó tremendo mono muchacho, encima agarra y me dice 'tenes una banana?'. Más firme que si, la banana no se le niega a nadie. Todo bien con el mono, tranquilo, manso. Es contundente la cosa, imaginate que hasta se volvió pirata porque le robaron una sola banana, no se come ni una el monki."
desh1="Llama a su barco, este dispara 3 bolas de cañón cada una infringe 3 de daño con un '50%' de golpear al objetivo. Coste 30 de energía"
desh2="Embiste y apuñala al objetivo causando entre 4-7 DMG, curandose un '50%' del daño realizado. Coste 20 de energía"
desh3="Se come una banana regenerando 15HP, esta crazy el monki. Coste 20 de energía"

def habilidad1(hp,energia):
    dmg_turno,heal=0,0
    import random
    if energia>=30:
        for i in range (3):
            prob=random.randint(1,4)
            if prob==1:
                dmg_turno=dmg_turno+3
            elif prob==2:
                dmg_turno=dmg_turno
        energia=energia-20
        heal=0
    else:
        dmg_turno,heal,energia=0,0,0
    return (dmg_turno,heal,energia)

def habilidad2(hp,energia):
    dmg_turno,heal=0,0
    import random
    if energia>=20:
        dmg_turno=random.randint(4, 7)
        heal=heal+(dmg_turno/2)
        energia=energia-20
    else:
        dmg_turno,heal,energia=0,0,0
    return(dmg_turno,heal,energia)

def habilidad3(hp,energia):
    dmg_turno,heal=0,0
    if energia>=30:
        heal=15
        dmg_turno=0
        energia=energia-20
    else:
        dmg_turno,heal,energia=0,0,0
    return(dmg_turno,heal,energia)

win="Después de vencer a Lonsi. El autoproclamado rey pirata se apropió del castillonsi. Recorriendo su nuevo hogar recordó un leyenda; 'dentro de la habitación del rey se encontraba el mayor de los tesoros, quien lo obtuviese se volverá el rey de todo'.\n El mono, impulsado por fuerzas mas allá del entendimiento, se adentró en la oscuridades del castillonsi.\nLuego de una extensa y tediosa búsqueda finalmente se dio con la mítica habitación.\n Un lugar rebosante de tesoros, pero Huigh se quedó atónito tras observar un colosal cofre con una banana gravada.\n Lo abrió entre nervios. De repente se quedó perplejo, no podía creer tal contenido. El colosal cofre estaba repleto de bananas doradas.\nUno pensaría que eran especiales. Pero solo eran bananas con colorante dorado y sabían mas rico.\nA pesar de eso Huigh se apego con gran cariño a susodicho cofre.\n"
lose="Huigh fue derrotado por lonsi, pero el rey era tan banidoso pero unica condicion el mono podria comer ni una sola banana por el resto de su vida.\nDescendió lentamente a la locura, tanto retorica como literalmente.\nSu historia concluyó en una ciudad carcomida y llena de pestilencia.\nEn la que solo terminó comiendo solo cascaras de banana.\n"