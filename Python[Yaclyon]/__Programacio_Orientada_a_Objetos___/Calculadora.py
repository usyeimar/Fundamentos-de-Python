# Metodos

class Calculadora:
    def __init__(self,n1,n2): # -> Declaramos el metodo y las variables que se van a utilizar
        self.suma = n1 + n2   # Asignamos el argoritmo que se va a operar con cada llamado
        self.resta = n1 - n2
        self.multiplicacion = n1 * n2
        self.division = n1 / n2

operacion = Calculadora(2,3) #("Asignamos los parametros con los cuales va a funcionar la calculadora") -> Los parametros no pueden estar vacios.
print(operacion.suma)
