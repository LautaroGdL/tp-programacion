import os
import random


clear= lambda : os.system('cls')


def pelea(pj1,pj2):
    #dodge extra es de 10% para todas las habilidades que lo tienen
    #reduccion del dano es del 15% para todas las habilidades que lo tienen
    #hab1 de egg tiene 15% de reduccion de da;o por 3 turnos 
    #hab1 froggy reduccion de da;o de enemigos por 2 turnos
    #special froggy dmg=120
    #special willy dmg=110
    #problema con reduccion del ataque del da;o (se cambian las stats permanentes del pj2) (testearlo con hab1 de egg)
    #problema cooldown (funcion para copiar diccionarios)
    stunpj2,stunpj1,stunpj2hab,stunpj1hab,extradodgepj1,extradodgepj2,defensapj1,defensapj2=0,0,0,0,0,0,0,0   

    pj1stats=pj1.copy()
    pj2stats=pj2.copy()

    while pj2['hp']>0 and pj1['hp']>0:
        
        if extradodgepj1>0:
            pj1['dodge']=(pj1stats['dodge']*0.1)+pj1stats['dodge']
            extradodgepj1-=1
        else:
            pj1['dodge']=pj1stats['dodge']
        

        
        if pj1['hab2']['cooldown']>pj1stats['hab2']['cooldown']:
            pj1['hab2']['cooldown']-=1

        if pj1['hab1']['cooldown']>pj1stats['hab1']['cooldown']:
            pj1['hab1']['cooldown']-=1

        if pj1['special']['cooldown']>pj1stats['special']['cooldown']:
            pj1['special']['cooldown']-=1


        while True:

            print(pj1)
            print(pj2)

            if stunpj1>0:
                stunpj1-=1
                continue
            
            while True:

                try:
                    print("1-Ataque simple\n2-Habilidad\n3-Ataque especial\n4-Resguardo")
                    mov=int(input("Introduce el movimiento a realizar:"))
                    if mov<1 or mov>4:
                        raise ValueError
                    break
                except:
                    clear()
                    print('Debe introducir un numero que responda a algun movimiento')
            clear()


            if mov==1:
                        if random.randint(1,100)<=pj2['dodge']:
                            print("Ataque fallido")
                            break
                        else:
                            pj2['hp']-=random.randint(pj1stats['dmg'][0],pj1stats['dmg'][1]) 
                            pj1['energia']+=pj1['re']
                            if pj1stats['energia']<pj1['energia']:
                                pj1['energia']=pj1stats['energia']
                            print("Ataque exitoso")
                            break
                            

            elif mov==2:
                while True:    
                    try:
                        habilidad=int(input('Seleccione la habilidad a realizar:'))
                        if habilidad<1 or habilidad>2:
                            raise ValueError
                        break
                        
                    except:
                        clear()
                        print('Debe introducir un numero que responda a alguna habilidad')
                clear()
                if habilidad==1:
                    if pj1['hab1']['energia']<pj1['energia']  and pj1['hab1']['cooldown']==pj1stats['hab1']['cooldown']: 
                        pj1['energia']-=pj1['hab1']['energia']
                        pj1['hab1']['cooldown']+=pj1stats['hab1']['cooldown']

                        if pj1['hab1']['dmg']!=None:
                            pj2['hp']-=pj1['hab1']['dmg']
                            print('Ataque de habilidad exitoso')
    
                        if pj1['hab1']['dodgehab']!=None:
                            extradodgepj1=pj1['hab1']['dodgehab']     
                            print('El dodge ha aumentado un 10%')

                        if pj1['hab1']['defensa']!=None:
                            defensapj1=pj1['hab1']['defensa']
                            pj2['dmg'][0]-=pj2stats['dmg'][0]*0.15
                            pj2['dmg'][1]-=pj2stats['dmg'][1]*0.15
                            print(f'Se ha reducido el daño de enemigos un 15% por {pj1["hab1"]["defensa"]} turnos')

                        if pj1['hab1']['stun']!=None:
                            stunpj2+=pj1['hab1']['stun']
                            print(f'Se ha stuneado a {pj2["nombre"]}')
                        break
                    
                    else:
                        print('Energia o cooldown insuficiente, o habilidad inhabilitada por el enemigo. Realiza otro movimiento')


                if habilidad==2:


                    if pj1['hab2']['energia']<pj1['energia']  and pj1['hab2']['cooldown']==pj1stats['hab2']['cooldown'] and stunpj1hab==0: 
                        pj1['energia']-=pj1['hab2']['energia']
                        pj1['hab2']['cooldown']+=pj1stats['hab2']['cooldown']

                        if pj1['hab2']['dmg']!=None:
                            pj2['hp']-=pj1['hab2']['dmg']
                            print('Ataque de habilidad exitoso')
    
                        if pj1['hab2']['dodgehab']!=None:
                            extradodgepj1=pj1['hab2']['dodgehab']     
                            print('El dodge ha aumentado un 10%')

                        if pj1['hab2']['defensa']!=None:
                            defensapj1=pj1['hab2']['defensa']
                            print(f'Se ha reducido el daño de enemigos un 15% por {pj1["hab2"]["defensa"]} turnos')

                        if pj1['hab2']['stun']!=None:
                            stunpj2+=1

                        if pj1['hab2']['re']!=None:
                            pj1stats['hp']+=pj1['hab2']['re']
                            pj1['hp']+=pj1['hab2']['re']
                            print(f'La vida maxima ha aumentado a {pj1stats["hp"]}')

                        
                        break
                        
                    else:
                        print('Energia o cooldown insuficiente, o habilidades inhabilitadas por el enemigo, realiza otro movimiento')
            
            
            elif mov==3:
                if pj1['energia']>=pj1['special']['energia'] and pj1['special']['cooldown']==pj1stats['special']['cooldown']:
                    if pj1['special']['dmg']!=None:
                        pj2['hp']-=pj1['special']['dmg']

                    if pj1['special']['stunhab']!=None:
                        stunpj2hab+=pj1['special']['stunhab']

                    pj1['energia']-=pj1['special']['energia']
                    pj1['special']['cooldown']+=pj1stats['special']['cooldown']
                    print('Ataque de habilidad exitoso')
                    break
                else:
                    print('Energia insuficiente o cooldown insuficiente, realiza otro movimiento')
            
            
            elif mov==4:
                if pj1stats['energia']>pj1['energia']:
                    pj1['energia']+=100
                    print(f'La energia de {pj1["nombre"]} ha aumentado a {pj1["energia"]}')
                    break
                else:
                    print("Energia completa, realiza otro movimiento")
    

        
        if  pj2['hp']>0:
            
            if stunpj2>0:
                stunpj2-=1
                print(f'Stun de {pj1["nombre"]}')
                continue

            if defensapj1>0:
                defensapj1-=1
            else:
                pj2['dmg']=pj2stats['dmg']
            
            while True:
                
                movrandom=random.randint(1,4)
                print(movrandom)
                if movrandom==1:
                    if random.randint(1,100)<pj1['dodge']:
                        print (f'Ataque fallido de {pj2["nombre"]}')
                        break
                    
                    else:
                        pj1['hp']-=random.randint(pj2stats['dmg'][0],pj2stats['dmg'][1]) 
                        pj2['energia']+=pj2['re']
                        if pj2stats['energia']<pj2['energia']:
                                pj2['energia']=pj2stats['energia']
                        print(f'Ataque exitoso de {pj2["nombre"]}')
                        break
                        
                if movrandom==2:
                    if stunpj2hab!=0:
                        print('Enemigo inhabilitado del uso de habilidades')
                    else:
                        print('habilidad')
                        break

                if movrandom==3:
                    print("defensa")
                    break

                if movrandom==4:
                    if pj2stats['energia']>pj2['energia']:
                        pj2['energia']+=100
                        if pj2['energia']>pj2stats['energia']:
                            pj2['energia']=pj2stats['energia']
                        print(f'La energia de {pj2["nombre"]} ha aumentado a {pj2["energia"]}')
                        break
                    else:
                        print('asd')

    if pj1['hp']<=0:
        print(f'{pj2["nombre"]} ha ganado')
    else:
        print(f'{pj1["nombre"]} ha ganado')
        

        

        

        
    


def main():
    specialegg={'energia':80,'cooldown':3,'dmg':random.randint(70,80),'defensa':2,'stunhab':None}
    hab1egg={'energia':60,'cooldown':2,'dmg':None,'defensa':3,'stun':None,'dodgehab':None,'re':None}
    hab2egg={'energia':40,'cooldown':2,'dmg':random.randint(35,165),'defensa':None,'stun':None,'dodgehab':None,'re':None}
    specialarbutus={'energia':80,'cooldown':4,'dmg':None,'defensa':None,'stunhab':1}
    hab2arbutus={'energia':60,'cooldown':1,'dmg':40,'defensa':2,'stun':None,'dodgehab':None,'re':None}
    hab1arbutus={'energia':90,'cooldown':3,'dmg':None,'stun':2,'dodgehab':None,'defensa':None,'re':None}
    egg={'hp':450,'energia':150,'dmg':[50,60],'dodge':10,'re':40,'nombre':'egg','hab1':hab1egg,'hab2':hab2egg,'special':specialegg}
    arbutus={'hp':600,'energia':200,'dmg':[30,45],'dodge':5,'re':50,'nombre':'arbutus','hab2':hab2arbutus,'hab1':hab1arbutus,'special':specialarbutus} 
    hab1froggy={'energia':50,'cooldown':3,'dmg':random.randint(40,70),'dodgehab':None,'defensa':2,'stun':None,'re':None}
    hab2froggy={'energia':40,'cooldown':2,'dmg':random.randint(80,85),'dodgehab':2,'defensa':None,'stun':None,'re':None}
    specialfroggy={'energia':100,'cooldown':6,'dmg':120,'defensa':None,'stunhab':None}
    froggy={'hp':350,'energia':150,'dmg':[80,100],'dodge':35,'re':40,'hab1':hab1froggy,'hab2':hab2froggy,'special':specialfroggy}
    hab1willy={'energia':30,'cooldown':2,'dmg':random.randint(45,60),'dodgehab':None,'defensa':None,'stun':None,'re':None}
    hab2willy={'energia':60,'cooldown':4,'dmg':None,'dodgehab':None,'defensa':None,'stun':None,'re':50}
    specialwilly={'energia':60,'cooldown':6,'dmg':110,'defensa':None,'stunhab':None}
    willy={'hp':450,'energia':150,'dmg':[45,70],'dodge':3,'re':40,'nombre':'willy','hab1':hab1willy,'hab2':hab2willy,'special':specialwilly}

    #h1 stewiee

    pelea(willy,egg)


main()

