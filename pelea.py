import os
import random

clear= lambda : os.system('cls')


def pelea(pj1,pj2):
    #dodge extra es de 10% para todas las habilidades que lo tienen
    #reduccion del dano es del 15% para todas las habilidades que lo tienen
    stunpj2=0
    stunpj1=0
    extradodgepj1=0
    extradodgepj2=0
    defensapj1=0
    defensapj2=0
    
    pj1stats=pj1.copy()
    pj2stats=pj2.copy()

    while pj2['hp']>0 and pj1['hp']>0:
        
        if extradodgepj1>0:
            pj1['dodge']=(pj1stats['dodge']*0.1)+pj1stats['dodge']
        else:
            pj1['dodge']=pj1stats['dodge']
        
        if stunpj1>0:
                stunpj1-=1
                continue

        while True:

            print(pj1)
            print(pj2)
            
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
                            pj2['hp']-=random.randint(pj1['dmg'][0],pj1['dmg'][1]) 
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
                    pass
                if habilidad==2:
   
                    if pj1['hab2']['energia']<pj1stats['energia']:
                        pj1['energia']-=pj1['hab2']['energia']
                        
                        if pj1['hab2']['dmg']!=None:
                            pj2['hp']-=pj1['hab2']['dmg']
                            print('Ataque de habilidad exitoso')
    

                        if pj1['hab2']['dodgehab']!=None:
                            extradodgepj1=pj1['hab2']['dodgehab']
                            print('El dodge ha aumentado un 10%')

                        if pj1['hab2']['stun']!=None:
                            stunpj2+=pj1['hab2']['stun']

                        if pj1['hab2']['defensa']!=None:
                            pass
                        
                        break
                        
                    else:
                        print('Energia insuficiente, realiza otro movimiento')
            
            
            elif mov==3:
                if pj1stats['energia']<pj1['special']['energia']:
                    if pj1['special']['dmg']!=None:
                        pj1['energia']-=pj1['special']['energia']
                    pj2['hp']-=pj1['special']['dmg']
                    break
                else:
                    print('Energia insuficiente, realiza otro movimientoo')
            
            
            elif mov==4:
                if pj1stats['energia']>pj1['energia']:
                    pj1['energia']+=100
                    print(f'La energia de {pj1["nombre"]} ha aumentado a {pj1["energia"]}')
                    break
                else:
                    print("Energia completa, realiza otro movimiento")
                #Cuanta energia gana por movimiento de resguardo?

        
        if  pj2['hp']>0:
            
            if stunpj2>0:
                stunpj2-=1
                continue

            if defensapj1>0:
                pj2['dmg']=pj1stats['dmg']-(pj2stats['dmg']*0.15)
                defensapj1-=1
                
            movrandom=random.randint(1,4)
            if movrandom==1:
                if random.randint(1,100)<pj1['dodge']:
                    print (f'Ataque fallido de {pj2["nombre"]}')
                
                else:
                    pj1['hp']-=random.randint(pj2['dmg'][0],pj2['dmg'][1]) 
                    pj2['energia']+=pj2['re']
                    if pj2stats['energia']<pj2['energia']:
                            pj2['energia']=pj2stats['energia']
                    print(f'Ataque exitoso de {pj2["nombre"]}')
                    
            if movrandom==2:
                print("habilidad")
                

            if movrandom==3:
                print("defensa")
                

            if movrandom==4:
                if pj2stats['energia']>pj2['energia']:
                    pj2['energia']+=100
                    if pj2['energia']>pj2stats['energia']:
                        pj2['energia']=pj2stats['energia']
                    print(f'La energia de {pj2["nombre"]} ha aumentado a {pj2["energia"]}')
                else:
                    pass

    if pj1['hp']<=0:
        print(f'{pj2["nombre"]} ha ganado')
    else:
        print(f'{pj1["nombre"]} ha ganado')
        

        

        

        
    


def main():
    specialegg={'energia':80,'cooldown':3,'dmg':random.randint(70,80),'defensa':10}
    hab2egg={'energia':40,'cooldown':2,'dmg':random.randint(35,165),'defensa':None,'stun':None,'dodgehab':None}
    hab2arbutus={'energia':60,'cooldown':1,'dmg':40,'defensa':10,'stun':None,'dodgehab':None}
    hab1arbutus={'energia':90,'cooldown':3,'dmg':None,'stun':2,'dodgehab':None}
    egg={'hp':450,'energia':150,'dmg':[50,60],'dodge':10,'re':40,'nombre':'egg','hab2':hab2egg,'special':specialegg}
    arbutus={'hp':600,'energia':200,'dmg':[30,45],'dodge':5,'re':50,'nombre':'arbutus','hab2':hab2arbutus} 
    hab2froggy={'energia':40,'cooldown':2,'dmg':random.randint(80,85),'dodgehab':1}
    #h1 arbutus 
    #h1 egg
    #special froggy
    #special willy
    #h1 stewiee

    pelea(egg,arbutus)


main()

