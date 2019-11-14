#### Ejercicio 01d
# 
# d) Escribir un programa que use un ciclo definido con rango numérico, que averigüe a cuántos amigos quieren saludar, les pregunte los nombres de esos amigos/as, y los salude.

leyendo = True
while leyendo:
    numeroAmigos = input("Introduce cuántos amigos tienes: ")
    try:
        numeroAmigos = int(numeroAmigos)
        leyendo = False
    except:
        print (numeroAmigos, "no es un número, prueba de nuevo")

for n in range(numeroAmigos):
       nombre = input("Introduce tu amigo: ")
       print ("Hola", nombre)
