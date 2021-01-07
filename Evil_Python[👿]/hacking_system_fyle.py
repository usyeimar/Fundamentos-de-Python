import os
command = ("systeminfo")
tubo = os.popen(command)
datos = tubo.readlines()
nombre_pc = datos[1].split("")[-1].split("\n")[0]
nombre_fichero = "information-"+nombre_pc+".txt"
fichero = open(nombre_fichero, "w")
fichero.writelines(datos)
fichero.close()
print (nombre_fichero)
