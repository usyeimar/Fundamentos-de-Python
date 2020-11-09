#Herencia Multiple
 class Telefono:
	def __init__(self):
		
		pass
	def llamar(self):
	  print('llamando...')
	def ocupado(self):
	  print('ocupado...')

 class Camara:
 	def __init__(self):
 		pass

 	def fotografia(sel):
 		print('Tomando fotos...')

 class Reproduccion:
 	"""docstring for Reproduccion"""
 	def __init__(self):
 		
 	def reproduccionmusica(self):
 		print('Reproduciendo Musica')
 	def Reproducirvideo(self):
 		print('reproducir un viedo...')



class  smartphone(Telefono,Camara,Reproduccion):
	"""docstring for  smartphone"""
	def __del__(self):
		 print('Telefono apagado')

movil = smartphone()
print(movil.fotografia())









		
 		
 		
