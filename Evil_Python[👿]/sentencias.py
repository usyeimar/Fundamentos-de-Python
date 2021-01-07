
# Sentencias de control de flujo
#if
#elif
#for
#while
#else

diccionarios_tcp = {"ssh":22,"Telnet":23,"https":80}
for x,y in  diccionarios_tcp.items():
    print("Escaneando el servicio",x)
    print("por el puerto",y)

x = 1
while  x < 10:
    print (x)
    x = x+1


