def importar_pj(name):
    "Devuelve el archivo de un pj basandose en el nombre dado"
    while name not in ("Arbutus", "Froggy", "Gregg", "Huigh", "Lonsi", "Stewie", "Willy"):
        name=input("Nombre no valido, elegir de vuelta, (Arbutus, Froggy, Gregg, Huigh, Lonsi, Stewie, Willy): ")
    
    if name == "Gregg":
        from Personajes.Gregg import Gregg
        return Gregg
    elif name =="Huigh":
        from Personajes.Huigh import Huigh
        return Huigh
    elif name == "Arbutus":
        from Personajes.Arbutus import Arbutus
        return Arbutus
    elif name == "Stewie":
        from Personajes.Stewie import Stewie
        return Stewie
    elif name == "Lonsi":
        from Personajes.Lonsi import Lonsi
        return Lonsi
    elif name == "Willy":
        from Personajes.Willy import Willy
        return Willy
    elif name =="Froggy":
        from Personajes.Froggy import Froggy
        return Froggy
    else:
        print("Error, no existe ese personaje ")
        
        
   
    
    
