#Metodo constructor
# MOdificar un archivo

# Metodo Constrcutor
# __init__()
## Eso quiere decir que esta funcion es especial.
## En la programacion orientada a objetos normalmente usamos esto para inicializar todo tipo de variable


class Email:
    def __init__(self):
        ## Los usamoas para crear todos los atributos que van atrabajar con la clase o el metodo
       self.enviado = False

    def enviar_correo(self):
        self.enviado = True

mi_correo = Email()

#print(mi_correo.enviado) #Ocultamos el valor que se debia imprimir 'False'
mi_correo.enviar_correo()
print(mi_correo.enviado)
