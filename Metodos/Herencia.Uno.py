# Herencia
class Pokemon: # padre
    pass
    def __init__(self,nombre,tipo,clase):
            self.nombre = nombre
            self.tipo = tipo
            self.clase  = clase
    def description (self):
        return "{} es un pokemon de tipo {} y pertenece a la clase {}".format(self.nombre,self.tipo,self.clase)


class pikachu(Pokemon): #hijo
    def ataque(self,tipoataque):
        return "{} tipo de ataque {} ".format(self.nombre,tipoataque)

class charmander(Pokemon):#hijo
    def ataque(self, tipoataque):
        return "{} tipo de ataque : {} ".format(self.nombre, tipoataque)

class serpent(Pokemon): # Hijo
    def ataque(self,tipoataque):
        return "{} tipo de ataque : {} ".format(self.nombre,tipoataque)
       



nuevo_pokemon = pikachu("electronys","electrico","Caos") 
print(nuevo_pokemon.description())
print(nuevo_pokemon.ataque(":""electrobalt"))

nuevo_pokemon2 = serpent("lady","agua","Natura")
print(nuevo_pokemon2.description())
print(nuevo_pokemon2.ataque(":"'Terremoto'))


