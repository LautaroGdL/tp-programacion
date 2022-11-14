def gen_barras(hp,st):
    health = []
    energy = []
    health.append("|"*hp)
    energy.append("|"*st)
    bars = [health, energy]
    health.append("|"*hp)
    energy.append("|"*st)
    
    return bars

def mostrar_barras(estadisticas):
    for i in range(0, len(estadisticas[0])):
        print(estadisticas[0][i].replace(",", ""),end="")
    print()
    for i in range(0, len(estadisticas[1])):
        print(estadisticas[1][i].replace(",", ""),end="")
    print()


x = gen_barras(20,15)
mostrar_barras(x)

