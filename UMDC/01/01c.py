#### Ejercicio 01c
#
# c) Escribir un programa que use un ciclo definido con rango numérico, que pregunte los nombres de sus cinco mejores amigos/as, y los salude.

for n in range(5):
    nombre = input("Introduce tu amigo: ")
    print ("Hola", nombre)