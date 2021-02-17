def cursos (c):
    return c.upper()

tupla = ('php','java','python','css')
tupla_mayusculas = tuple(map(cursos,tupla))

print(tupla_mayusculas)