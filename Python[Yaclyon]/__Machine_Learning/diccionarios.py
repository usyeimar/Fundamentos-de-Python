dict = { 'jose': 22 ,'juan': 23 ,'maria': 18 ,'juanita': 17 }

varones = {'jose':22,'juan':23}
mujeres = {'maria':18,'juanita':17}

estudiantes = list(dict.keys()) 
estudiantes.sort()

for e in estudiantes:
    print(" : ".join((e,str(dict[e]))))



