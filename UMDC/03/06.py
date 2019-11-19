"""
Ejercicio 06

Utilizando la función randrange del módulo random, escribir un programa que
obtenga un número aleatorio secreto, y luego permita al usuario ingresar
números y le indique sin son menores o mayores que el número a adivinar,
hasta que el usuario ingrese el número correcto.
"""
from random import randrange

n = randrange(10)
while True:
    leyendo = True
    while leyendo:
        try:
            adivina = int(input("Adivina el número: "))
            leyendo = False
        except ValueError:
            print("Introduzca un valor numérico")
    if adivina == n:
        print("¡¡ Ese es !!")
        break
    elif adivina < n:
        print("El número es más alto")
    else:
        print("El número es más bajo")
