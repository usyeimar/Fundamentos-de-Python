
    #Función para mostrar el menú
def muestra_menu():
    print('')
    print('')
    print('-------- Kwranking --------')
    print('')
    print('[1] – Importar palabras clave')
    print('[2] – Mostrar palabras clave')
    print('[0] – Salir')

    #Función carga_keywords()
def carga_keywords():
    keywords = []
    try:
        with open('keywords.txt') as fichero:
            for kw in fichero:
                kw = kw.replace('\n', '')
                keywords.append(kw)
    except FileNotFoundError:
        print('No se encuentra el fichero keywords.txt')
    return keywords

#Función para mostrar las palabras clave
def muestra_keywords(keywords):
    contador = 0
    for kw in keywords:
        print(kw)
        contador += 1
        if contador == 20:
            contador = 0
            input('Mostrar más...')


#El programa principal
def run():
    keywords = []
    while True:
        muestra_menu()
        opcion = input('Selecciona una opción > ')
        opcion = int(opcion)
        if opcion == 0:
            break
        elif opcion == 1:
            keywords = carga_keywords()
        elif opcion == 2:
            muestra_keywords(keywords)
        else:
            print('Opción no válida')
if __name__ == '__main__':
    run()