def impares(n):
    if (n % 2 == 1):
        return n

lista = [1,2,3,4,5,67,89,34,56,78,223,45,6,7,878,9,9,9767,6,54]

lista_impares = list(filter(impares,lista))
print(lista_impares)

