# Herencia
class Pokemon: # padre
    pass
    def __init__(self,nombre,tipo):
            self.nombre = nombre
            self.tipo = tipo
    def description (self):
        return "{} es un pokemon de tipo {}".format(self.nombre,self.tipo)


class pikachu(Pokemon): #hijo
    def ataque(self,tipoataque):
        return "{} tipo de ataque {} ".format(self.nombre,tipoataque)

class charmander(Pokemon):#hijo
    def ataque(self, tipoataque):
        return "{} tipo de ataque : {} ".format(self.nombre, tipoataque)


nuevo_pokemon = pikachu("electronys","electrico") 
print(nuevo_pokemon.description())

print(nuevo_pokemon.ataque(":""electrobalt"))