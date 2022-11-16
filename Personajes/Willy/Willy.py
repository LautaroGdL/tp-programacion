dmg=45
dmg2=60
hp=450
energia=150
name="Willy"
des="Un famoso socorrista conocido por su gran velocidad en el agua, su frase célebre es 'todo gracias al salvavidas'. \n Si lo ves no toques su salvavidas, pierde sus estribos cuando alguien lo hace."
desh1="Se arroja heroicamente al agua, salvando una persona y dañando permanentemente el autoestima del enemigo. Causandole 120 de daño. Coste=90 energia\n"
desh2="Lanza su salvavidas como un boomerang, dañando 3 veces al enemigo haciendo 15-20 de daño cada golpe. Coste: 30 energia\n"
desh3="Se coloca unos flotadores que tiene guardados, aumentando su propia moral y regenerando 70 de vida. Coste: 60 energia\n"

def habilidad1(hp,energia):
    dmg_turno,heal=0,0
    if energia>=90:
        dmg_turno=120
        energia=energia-90
    else:

        dmg_turno,heal,energia=0,0,0
    return(dmg_turno,heal,energia)

def habilidad2(hp,energia):
    dmg_turno,heal=0,0
    import random
    if energia>=30:
        for i in range (3):
            dtimes=random.randint(15-20)
            dmg_turno=dmg_turno+dtimes
        energia=energia-30
    else:
        dmg_turno,heal,energia=0,0,0
    return(dmg_turno,heal,energia)

def habilidad3(hp,energia):
    dmg_turno,heal=0,0
    if energia>=60:
        heal=70
        dmg_turno=0
    else:
        dmg_turno,heal,energia=0,0,0
    return(dmg_turno,heal,energia)

win="Finalmente derrotó a Lonsi. Ahora se decidió a cumplir su sueño. Parecía imposible, pero finalmente lo va a conseguir.\n Como nuevo rey del Reinonsi establecerá su primer decreto. El cual obligará a todos los habitantes a llevar puesto un salvavidas todo el tiempo.\n De esta forma Willy podrá retirar de su trabajo de socorrista y pasará a la historia como el Mesías del salvavidas.\n Una tortuga tan heroica que salvaría a todos los que se estén por ahogar sin siquiera estar presente. \n (Además de darles un grandioso look)\n"
lose="Su ultima batalla fue decisiva. Willy dió todo lo que tenía... pero falló.\n Durante esta ocurrió algo impensable: su salvavidas se rompió. Al igual que el espíritu de Willy.\n Pues sin el no era nada.\n"