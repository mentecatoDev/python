"""
Ejercicio 01d

d) Escribir un programa que use un ciclo definido con rango numérico, que
averigüe a cuántos amigos quieren saludar, les pregunte los nombres de esos
amigos/as, y los salude.
"""

leyendo = True
while leyendo:
    numero_amigos = input("Introduce cuántos amigos tienes: ")
    try:
        numero_amigos = int(numero_amigos)
        leyendo = False
    except ValueError:
        print(numero_amigos, "no es un número, prueba de nuevo")

for n in range(numero_amigos):
    nombre = input("Introduce tu amigo: ")
    print("Hola", nombre)
