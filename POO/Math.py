import math
from typing import Deque

class Complejo:
    def __init__(self,real,imaginario) -> None:
       self.real = real
       self.img = imaginario
       
    def abs(self):
        print (math.sqrt((self.real*self.real) + (self.img * self.img)))



def main():
    numero = Complejo(3,4)  # Se crea el objeto y se inicializa haciendo
                            # el llamado al metodo __init__ pasnado los valores
                            # real = 3 y imaginario = 4
    
    numero.abs() # Convocamos abs de la clase complejo

input() # Generamos una pausa en la aplicacion esperando a que se presione una tecla

    
if __name__== '__main__':
    main()

