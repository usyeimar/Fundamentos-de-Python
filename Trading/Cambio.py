pesos = input("¿Cuantos pesos colombianos tienes?: ")
pesos = float(pesos)
valor_dolar = 3875
dolares = pesos / valor_dolar
dolares = round(dolares,2) # aqui lo redondeamos a dos decimales
dolares = str(dolares)
print("Tienes $" + dolares + "dólares") 