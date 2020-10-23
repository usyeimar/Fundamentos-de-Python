#Funciones para atributos

# Creo la clase persona
class Persona:
    edad = 27
    nombre = 'Yeimar'
    pais = " Colombia"
    



# Le asigno a la variable doctor el atributo de la clase
doctor = Persona()

#esta linea del codigo nos imprime el valor agregado en el atributo edad.
print("La edad es :",doctor.edad)
print('la edad es:', getattr(doctor, 'edad'))

#aqui se muestra una comprobacion de que si  un atributo de la clase existe nos arroja un true, si no  un false. 
print('El doctor tiene una edad?',hasattr(doctor,'Apellido'))

print("Antes era :",doctor.nombre)

#
setattr(doctor,"nombre"," Victor")
print("Ahora se llamma :",doctor.nombre)


delattr(Persona,"pais") # aqui elimino el atributo  pais y luego lo imprimio
# print(doctor, "pais")
setattr(Persona,"pais","paises")
print(doctor.nombre)
print(doctor.edad)
print(doctor.pais, "se actualizo correcatmente  ")
print(doctor.pais)






