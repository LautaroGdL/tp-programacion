dmg=2
dmg2=5
hp=26
energia=50
name="Willy"
des="Un famoso socorrista conocido por su gran velocidad en el agua, su frase célebre es 'todo gracias al salvavidas'. Si lo ves no toques su salvavidas, pierde sus estribos cuando alguien lo hace."
desh1="Se arroja heroicamente al agua, salvando una persona y dañando permanentemente el autoestima del enemigo. Causandole 12 de daño. Coste=30 energia"
desh2="Lanza su salvavidas como un boomerang, dañando 3 veces al enemigo haciendo 1-3 de daño cada golpe. Coste: 30 energia"
desh3="Se coloca unos flotadores que tiene guardados, aumentando su propia moral y regenerando 15 de vida. Coste: 30 energia"

def habilidad1(hp,energia):
    dmg_turno,heal=0,0
    if energia>=30:
        dmg_turno=13
        energia=energia-30
    else:
        dmg_turno,heal,energia=0,0,0
    return(dmg_turno,heal,energia)

def habilidad2(hp,energia):
    dmg_turno,heal=0,0
    import random
    if energia>=20:
        for i in range (3):
            dtimes=random.randint(1, 3)
            dmg_turno=dmg_turno+dtimes
        energia=energia-20
    else:
        dmg_turno,heal,energia=0,0,0
    return(dmg_turno,heal,energia)

def habilidad3(hp,energia):
    dmg_turno,heal=0,0
    if energia>=30:
        heal=15
        dmg_turno=0
        energia=energia-30
    else:
        dmg_turno,heal,energia=0,0,0
    return(dmg_turno,heal,energia)

win="Finalmente derrotó a Lonsi. Ahora se decidió a cumplir su sueño. Parecía imposible, pero finalmente lo va a conseguir.\nComo nuevo rey del Reinonsi establecerá su primer decreto. El cual obligará a todos los habitantes a llevar puesto un salvavidas todo el tiempo.\nDe esta forma Willy podrá retirar de su trabajo de socorrista y pasará a la historia como el Mesías del salvavidas.\nUna tortuga tan heroica que salvaría a todos los que se estén por ahogar sin siquiera estar presente.\n(Además de darles un grandioso look)\n"
lose="Su ultima batalla fue decisiva. Willy dió todo lo que tenía... pero falló.\nDurante esta ocurrió algo impensable: su salvavidas se rompió. Al igual que el espíritu de Willy.\nPues sin el no era nada.\n"
