#Modificar un atributo
class Email:
    def __init__(self) -> None:
        self.enviado = False
    def enviar_correo(self) -> None:
        self.enviado = True

mi_correo = Email()
mi_correo.enviar_correo()
print(mi_correo.enviado) 

