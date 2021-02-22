"""
Ejercicio 01b

b) Escribir un ciclo definido que salude por pantalla a sus cinco mejores
amigos/as.

>>> for amigo in ["Luis", "José Antonio", "Miguel", "Paco", "Jaime"]:
...    print("Hola", amigo)
Hola Luis
Hola José Antonio
Hola Miguel
Hola Paco
Hola Jaime

"""

for amigo in ["Luis", "José Antonio", "Miguel", "Paco", "Jaime"]:
    print("Hola", amigo)

import doctest

doctest.testmod()
