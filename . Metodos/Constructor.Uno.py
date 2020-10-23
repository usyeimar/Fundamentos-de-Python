# Metodo Constrcutor
# __init__()
## Eso quiere decir que esta funcion es especial.
## En la programacion orientada a objetos normalmente usamos esto para inicializar todo tipo de variable


class Persona:
    pass # quiere decir que por el momento esta vacio
    def __init__(self,nombre,año):
        ## Los usamoas para crear todos los atributos que van atrabajar con la clase o el metodo
       
        self.nombre = nombre
        self.año = año
    def descripcion(self):
        # ".format dar una respuesta un poco corta y coherente
        return "{} tiene {} años ".format(self.nombre, self.año)
    def comentario(self,frase):
        return "{} dice:".format(self.nombre,frase)

doctor =  Persona('Yeimar',17)
print(doctor.nombre)
print(doctor.descripcion())
print(doctor.comentario("Hola mundo")) 


