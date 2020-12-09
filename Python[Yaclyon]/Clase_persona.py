class Persona:
    edad = 27
    nombre = 'Victor'
    pais = 'Colombia'

    
doctor = Persona()
print('La edad es :' ,doctor.edad)
print('La edad es :' , getattr (doctor,'edad'))
print('El doctor tiene una edad? :', hasattr(doctor,'apellido'))
print('antes era :',doctor.nombre)
# Con esta linea hacemos un cambio de valor en el nombre
setattr(doctor, 'nombre','Yeimar')
print('ahora se llama :' ,doctor.nombre )
delattr(Persona,'pais')
print(doctor.nombre)
print(Persona.edad)