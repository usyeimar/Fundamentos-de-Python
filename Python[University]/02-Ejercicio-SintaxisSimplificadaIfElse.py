condicion = False 

print("Condicion verdadera") if condicion else print("Condicion falsa") 

if condicion :
    print("La condición es verdadera")
else:
    print("La condición es falsa")    
    
numero = int(input("Proporciona un número entre 1 y 3:"))
if numero == 1:
    numeroTexto = "número uno"
elif numero == 2:
    numeroTexto = "número dos"    
elif numero == 3:
    numeroTexto = "número tres"  
else:
    numeroTexto = "Valor fuera de rango"
    
print("número proporcionado:", numeroTexto)        
    