habilidad=int(input("Ingrese n° de habilidad deseada"))
dmgt=40
dmge=50
hp=450
hpe=500
energia=150
cool1:0
cool2=0
cool3=0
def habilidad_egg(dmgt,dmge,hp,hpe,energia):
    import random
    if habilidad>=1 and habilidad<=3:
        if habilidad==1 and energia>=80:
            #dmgt=daño x turno
            #dmge=daño enemigo
            dmgt=dmgt+20
            reduccion=dmge*(10/100)
            dmge=dmge-reduccion
            hpe=hpe-dmgt
            energia=energia-80
            cool10=3
            print(f"Realizas {dmgt} de daño este turno")
                
        elif habilidad==2 and energia>=60:
            parry=dmge*(50/100)
            dmgt=parry
            energia=energia=60
            cool1=2
            print(f"Realizas {dmgt} de daño este turno")
            print(f"Mitigas {dmge} de daño y devuelves {dmgt} de daño")
            
        elif habilidad==3 and energia>=40:
             dmgt=0
             times=random.randint(1,3)
             for i in range (times):
                 dtimes=random.randint(33,44)
                 dmgt=dmgt+dtimes
             print(f"Realizas {dmgt} de daño este turno")
             energia=energia-40
             cool3=2
             for i in range (times):
                 dtimes=random.randint(33,44)
                 dmgt=dmgt+dtimes
        

            
habilidad_egg(dmgt,dmge,hp,hpe,energia)
        