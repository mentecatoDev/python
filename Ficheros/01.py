"""
Ejercicio 01

Escribe un programa que solicite un nombre de fichero, lo abra, lea y
visualice el contenido en mayúsculas. Usa el fichero words.txt para crear la
salida que se busca.
"""

leyendo = True
while leyendo:
    try:
        fichero = input("Nombre de fichero :")
        manejador = open(fichero)
        leyendo = False
    except IOError:
        print("El fichero no existe")
for linea in manejador:
    print(linea.upper(), end="")
