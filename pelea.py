import os
import random

clear= lambda : os.system('cls')

"""
def special_egg(pj1,pj2,cooldown):
    if cooldown==0 and pj1['energia']>=80:
        cooldown=3
        pj2['hp']-=pj1['dmg']-20
        pj1['energia']-=80
        return pj1,pj2,cooldown
    else:
        print("Ataque no disponible")
        return False,False,False

def h2_egg(pj1,pj2,cooldown):
    if cooldown==0 and pj1['energia']>=40:
        cooldown=2
        pj2['hp']=pj2['hp']-(random.randint(35,55)*random.randint(1,3))
        pj1['energia']-=40
        return pj1,pj2,cooldown
    else:
        return False,False,False

def h2_arbutus(pj1,pj2,cooldown):
    if cooldown==0 and pj1['energia']>=60:
        cooldown=1
        pj2['hp']-=40
    return pj1,pj2,cooldown
"""



def pelea(pj1,pj2):
    pj1stats=pj1.copy()
    pj2stats=pj2.copy()
    while pj2['hp']>0 and pj1['hp']>0:
        while True:
            print(pj1)
            print(pj2)
            print("1-Ataque simple\n2-Habilidad\n3-Defensa\n4-Resguardo")
            mov=int(input("Introduce el movimiento a realizar:"))
            clear()

            
            if mov==1:
                #Se pierde energia por ataque basico?
                while True:
                        if random.randint(1,100)<pj2['dodge']:
                            print("Ataque fallido")
                        else:
                            pj2['hp']-=random.randint(pj1['dmg'][0],pj1['dmg'][1]) 
                            pj1['energia']+=pj1['re']
                            if pj1stats['energia']<pj1['energia']:
                                pj1['energia']=pj1stats['energia']
                            print("Ataque exitoso")
                            break
                break        

            if mov==2:
                break
            if mov==3:
                break
            if mov==4:
                if pj1stats['energia']>pj1['energia']:
                    pj1['energia']+=100
                    print(f'La energia de {pj1["nombre"]} ha aumentado a {pj1["energia"]}')
                    break
                else:
                    print("Energia completa, realiza otro movimiento")
                #Cuanta energia gana por movimiento de resguardo?

        if  pj2['hp']>0:
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
                if movrandom==2:
                    print("habilidad")
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
                        pass

        else:
            print(f'{pj1["nombre"]} ha ganado')
            break
        if pj1['hp']<=0:
            print(f'{pj2["nombre"]} ha ganado')
            break

        

        
    


def main():
    egg={'hp':450,'energia':150,'dmg':[50,60],'dodge':10,'re':40,'nombre':'egg'}
    arbutus={'hp':600,'energia':200,'dmg':[30,45],'dodge':5,'re':50,'nombre':'arbutus'}    

    pelea(egg,arbutus)

main()
