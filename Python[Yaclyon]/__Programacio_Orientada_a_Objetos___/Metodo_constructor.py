# Metodo Constructor

class Persona :
    pass
    def __init__(self, nombre, año) -> None:
        self.nombre = nombre
        self.año = año
   
    def descripcion(self):
        return '{} tiene {} '.format(self.nombre, self.año)

    def comentario(self,frase):
        return '{} dice {}' .format(self.nombre,frase)


doctor = Persona('Yeimar',20)
print(doctor.descripcion())
print(doctor.comentario('Hola, ¿Como estan todos?'))
