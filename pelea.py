import os
import random


clear= lambda : os.system('cls')


def pelea(pj1,pj2):
    #agregar funcion del dibujo del pj a su diccionario
    #dodge extra es de 10% para todas las habilidades que lo tienen
    #reduccion del dano es del 10% para todas las habilidades que lo tienen
    #hab1 de egg tiene 10% de reduccion de da;o 
    #hab1 froggy 10 % reduccion de da;o de enemigos 
    #special froggy dmg=120
    #special willy dmg=110
 
    stunpj2,stunpj1,stunpj2hab,stunpj1hab,extradodgepj1,extradodgepj2,pj1h1cooldown,pj1h2cooldown,pj1specialcooldown=0,0,0,0,0,0,0,0,0  
    pj2h1cooldown,pj2h2cooldown,pj2specialcooldown=0,0,0
    pj1stats=pj1.copy()
    pj2stats=pj2.copy()

    while pj2['hp']>0 and pj1['hp']>0:
 
        if extradodgepj1>0:
            pj1['dodge']=(pj1stats['dodge']*0.1)+pj1stats['dodge']
            extradodgepj1-=1
        else:
            pj1['dodge']=pj1stats['dodge']
        

        if pj1h1cooldown!=0:
            pj1h1cooldown-=1

        if pj1h2cooldown!=0:
            pj1h2cooldown-=1

        if pj1specialcooldown!=0:
            pj1specialcooldown-=1


        while True:


            if stunpj1>0:
                stunpj1-=1
                print('stun de {pj2["nombre"]}')
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
                    if pj1['hab1']['energia']<pj1['energia']  and pj1h1cooldown==0 and stunpj1hab==0: 
                        pj1['energia']-=pj1['hab1']['energia']
                        pj1h1cooldown=pj1['hab1']['cooldown']

                        if pj1['hab1']['dmg']!=None:
                            pj2['hp']-=pj1['hab1']['dmg']
                            print('Ataque de habilidad exitoso')
    
                        if pj1['hab1']['dodgehab']!=None:
                            extradodgepj1=pj1['hab1']['dodgehab']     
                            print('El dodge ha aumentado un 10%')

                        if pj1['hab1']['defensa']!=None:
                            pj2['dmg'][0]-=pj2['dmg'][0]*0.10
                            pj2['dmg'][1]-=pj2['dmg'][1]*0.10
                            print(f'Se ha reducido el daño de enemigos un 10%')

                        if pj1['hab1']['stun']!=None:
                            stunpj2+=pj1['hab1']['stun']
                            print(f'Se ha stuneado a {pj2["nombre"]}')
                        
                        if pj1['hab1']['re']!=None:
                            pj1stats['hp']+=pj1['hab1']['re']
                            pj1['hp']+=pj1['hab1']['re']
                            print(f'La vida maxima ha aumentado a {pj1stats["hp"]}')

                        break
                    
                    else:
                        print('Energia o cooldown insuficiente, o habilidad inhabilitada por el enemigo. Realiza otro movimiento')


                if habilidad==2:


                    if pj1['hab2']['energia']<pj1['energia']  and pj1h2cooldown==0 and stunpj1hab==0: 
                        pj1['energia']-=pj1['hab2']['energia']
                        pj1h2cooldown=pj1['hab2']['cooldown']

                        if pj1['hab2']['dmg']!=None:
                            pj2['hp']-=pj1['hab2']['dmg']
                            print('Ataque de habilidad exitoso')
    
                        if pj1['hab2']['dodgehab']!=None:
                            extradodgepj1=pj1['hab2']['dodgehab']     
                            print('El dodge ha aumentado un 10%')

                        if pj1['hab2']['defensa']!=None:
                            pj2['dmg'][0]-=pj2['dmg'][0]*0.10
                            pj2['dmg'][1]-=pj2['dmg'][1]*0.10
                            pj2['dmg'][0]=round(pj2['dmg'][0])
                            pj2['dmg'][1]=round(pj2['dmg'][1])
                            print(f'Se ha reducido el daño de enemigos un 10%')

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
                if pj1['energia']>=pj1['special']['energia'] and pj1specialcooldown==0:
                    if pj1['special']['dmg']!=None:
                        pj2['hp']-=pj1['special']['dmg']
                        print('Ataque especial exitoso')

                    if pj1['special']['stunhab']!=None:
                        stunpj2hab+=pj1['special']['stunhab']
                        print('Stun de ataque especial exitoso')

                    pj1['energia']-=pj1['special']['energia']
                    pj1specialcooldown=pj1['special']['cooldown']
  
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

            
            if extradodgepj2>0:
                pj2['dodge']=(pj2stats['dodge']*0.1)+pj2stats['dodge']
                extradodgepj2-=1
            else:
                pj2['dodge']=pj2stats['dodge']
            

            if pj2h1cooldown!=0:
                pj2h1cooldown-=1

            if pj2h2cooldown!=0:
                pj2h2cooldown-=1

            if pj2specialcooldown!=0:
                pj2specialcooldown-=1

            
            while True:
                
                movrandom=random.randint(1,4)
                if movrandom==1:
                    if random.randint(1,100)<pj1['dodge']:
                        print (f'Ataque fallido de {pj2["nombre"]}')
                        break
                    
                    else:
                        pj1['hp']-=random.randint(pj2['dmg'][0],pj2['dmg'][1]) 
                        pj2['energia']+=pj2['re']
                        if pj2stats['energia']<pj2['energia']:
                                pj2['energia']=pj2stats['energia']
                        print(f'Ataque exitoso de {pj2["nombre"]}')
                        break
                        
                elif movrandom==2:
            
                    habilidadrandom=random.randint(1,2)
                    
                    if habilidadrandom==1:
                        if pj2['hab1']['energia']<pj2['energia'] and pj2h1cooldown==0 and stunpj2hab==0:
                            
                            pj2['energia']-=pj2['hab1']['energia']
                            pj2h1cooldown=pj2['hab1']['cooldown']

                            if pj2['hab1']['dmg']!=None:
                                pj1['hp']-=pj2['hab1']['dmg']
                                print(f'Ataque de habilidad de {pj2["nombre"]} exitoso')

                            if pj2['hab1']['dodgehab']!=None:
                                extradodgepj2=pj2['hab1']['dodgehab']
                                print(f'El dodge de {pj2["nombre"]} ha aumentado un 10%')

                            if pj2['hab1']['defensa']!=None:
                                pj1['dmg'][0]-=pj1['dmg'][0]*0.10
                                pj1['dmg'][1]-=pj1['dmg'][1]*0.10
                                pj1['dmg'][0]=round(pj1['dmg'][0])
                                pj1['dmg'][1]=round(pj1['dmg'][1])
                                print(f'{pj2["nombre"]} te ha reducido el daño de ataque un 10%')

                            if pj2['hab1']['stun']!=None:
                                stunpj1+=pj2['hab1']['stun']
                                print(f'{pj2["nombre"]} te ha stuneado')
                            
                            if pj2['hab1']['re']!=None:
                                pj2stats['hp']+=pj2['hab1']['re']
                                pj2['hp']+=pj2['hab1']['re']
                                print(f'La vida maxima de {pj2["nombre"]} ha aumentado a {pj2stats["hp"]}')

                            break

                        else:
                            pass
                   
                    elif habilidadrandom==2:
                        if pj2['hab2']['energia']<pj2['energia'] and pj2h2cooldown==0 and stunpj2hab==0:
                            
                            pj2['energia']-=pj2['hab2']['energia']
                            pj2h2cooldown=pj2['hab2']['cooldown']

                            if pj2['hab2']['dmg']!=None:
                                pj1['hp']-=pj2['hab2']['dmg']
                                print(f'Ataque de habilidad de {pj2["nombre"]} exitoso')

                            if pj2['hab2']['dodgehab']!=None:
                                extradodgepj2=pj2['hab2']['dodgehab']
                                print(f'El dodge de {pj2["nombre"]} ha aumentado un 10%')

                            if pj2['hab2']['defensa']!=None:
                                pj1['dmg'][0]-=pj1['dmg'][0]*0.10
                                pj1['dmg'][1]-=pj1['dmg'][1]*0.10
                                pj1['dmg'][0]=round(pj1['dmg'][0])
                                pj1['dmg'][1]=round(pj1['dmg'][1])
                                print(f'{pj2["nombre"]} te ha reducido el daño de ataque un 10%')

                            if pj2['hab2']['stun']!=None:
                                stunpj1+=pj2['hab2']['stun']
                                print(f'{pj2["nombre"]} te ha stuneado')

                            if pj2['hab2']['re']!=None:
                                pj2stats['hp']+=pj2['hab2']['re']
                                pj2['hp']+=pj2['hab2']['re']
                                print(f'La vida maxima de {pj2["nombre"]} ha aumentado a {pj2stats["hp"]}')

                                break                        
                            
                        else:
                            pass

                
                elif movrandom==3:
               
                    if pj2['energia']>=pj2['special']['energia'] and pj2specialcooldown==0:
                        if pj2['special']['dmg']!=None:
                            pj1['hp']-=pj2['special']['dmg']
                            print(f'Ataque de {pj2["nombre"]} especial exitoso')

                        if pj2['special']['stunhab']!=None:
                            stunpj1hab+=pj2['special']['stunhab']
                            print(f'Stun de habilidad de {pj2["nombre"]} especial exitoso')

                        pj2['energia']-=pj2['special']['energia']
                        pj2specialcooldown=pj2['special']['cooldown']
                        break
                    
                    else:
                        pass

                
                elif movrandom==4:
                    if pj2stats['energia']>pj2['energia']:
                        pj2['energia']+=100
                        if pj2['energia']>pj2stats['energia']:
                            pj2['energia']=pj2stats['energia']
                        print(f'La energia de {pj2["nombre"]} ha aumentado a {pj2["energia"]}')
                        break
                    else:
                        pass

    if pj1['hp']<=0:
        print(f'{pj2["nombre"]} ha ganado')
    else:
        print(f'{pj1["nombre"]} ha ganado')
        



def main():
    specialegg={'energia':80,'cooldown':4,'dmg':random.randint(70,80),'defensa':2,'stunhab':None}
    hab1egg={'energia':60,'cooldown':5,'dmg':None,'defensa':1,'stun':None,'dodgehab':None,'re':None}
    hab2egg={'energia':40,'cooldown':3,'dmg':random.randint(35,165),'defensa':None,'stun':None,'dodgehab':None,'re':None}
    specialarbutus={'energia':80,'cooldown':4,'dmg':None,'defensa':None,'stunhab':1}
    hab2arbutus={'energia':60,'cooldown':6,'dmg':40,'defensa':1,'stun':None,'dodgehab':None,'re':None}
    hab1arbutus={'energia':90,'cooldown':4,'dmg':None,'stun':2,'dodgehab':None,'defensa':None,'re':None}
    egg={'hp':450,'energia':150,'dmg':[50,60],'dodge':10,'re':40,'nombre':'egg','hab1':hab1egg,'hab2':hab2egg,'special':specialegg}
    arbutus={'hp':600,'energia':200,'dmg':[30,45],'dodge':5,'re':50,'nombre':'arbutus','hab2':hab2arbutus,'hab1':hab1arbutus,'special':specialarbutus} 
    hab1froggy={'energia':50,'cooldown':4,'dmg':random.randint(40,70),'dodgehab':None,'defensa':1,'stun':None,'re':None}
    hab2froggy={'energia':40,'cooldown':3,'dmg':random.randint(80,85),'dodgehab':2,'defensa':None,'stun':None,'re':None}
    specialfroggy={'energia':100,'cooldown':6,'dmg':120,'defensa':None,'stunhab':None}
    froggy={'hp':350,'energia':150,'dmg':[80,100],'dodge':35,'re':40,'hab1':hab1froggy,'hab2':hab2froggy,'special':specialfroggy}
    
    
    
    
    
    hab1willy={'energia':30,'cooldown':3,'dmg':random.randint(45,60),'dodgehab':None,'defensa':None,'stun':None,'re':None}
    hab2willy={'energia':60,'cooldown':5,'dmg':None,'dodgehab':None,'defensa':None,'stun':None,'re':50}
    specialwilly={'energia':60,'cooldown':6,'dmg':110,'defensa':None,'stunhab':None}
    willy={'hp':450,'energia':150,'dmg':[45,70],'dodge':3,'re':40,'nombre':'willy','hab1':hab1willy,'hab2':hab2willy,'special':specialwilly}
    pelea(arbutus,egg)


main()

