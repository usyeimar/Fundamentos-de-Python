
# Creamos la lista vacia 
lista = []
num  = 0

#Con esta funcion le pedimos numeros al usuario
def pedir():
    i = 0 # el contador inicia en 0
    while i < 5 : #Mientras i sea menor que 5 le va a pedir numeros al usuario
        num = int(input("Ingrese Numeros :"))
        lista.append(num) #Con el metodo append agregamos los numeros ingresados por el usuaario a la lista
        i += 1
        
def numeros():
    lista.sort()#Con el metodo sort ordenamos los datos de la lista
    pares = [] #Creamos dos listas, una en la cual se van a almacenar los numeros impares y otra en la cual se almacenan los pares....
    impares = []
    for i in lista: #con el ciclo for  recorremos todos los elementos de la lista 
        if i % 2 == 0: #con la condicion  if i % 2 == 0: evaluamos los elemtos que su residuo siendo divididos == 0 
            pares.append(i)
        else:
            impares.append(i)
    print("Los impares son :",impares)
    print("Los pares son :",pares)
    
pedir()
numeros()
