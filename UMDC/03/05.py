from time import sleep

"""
Ejercicio 05

Manejo de contraseñas
Escribir un programa que contenga una contraseña inventada, que le pregunte
al usuario la contraseña, y no le permita continuar hasta que la haya
ingresado correctamente.
"""


contrasena = "contra"
while True:
    con = input("Contraseña : ")
    if con == contrasena:
        print("Contraseña correcta")
        break
    else:
        print("Contraseña errónea")

"""
Modificar el programa anterior para que solamente permita una cantidad fija de
intentos.
"""


contrasena = "contra"
intentos = 3
while intentos:
    con = input("Contraseña : ")
    if con == contrasena:
        print("Contraseña correcta")
        break
    else:
        print("Contraseña errónea")
        intentos -= 1

"""
Modificar el programa anterior para que después de cada intento agregue una
pausa cada vez mayor, utilizando la función sleep del módulo time.
"""

contrasena = "contra"
maxIntentos = 3
intentos = maxIntentos
while intentos != 0:
    con = input("Contraseña : ")
    if con == contrasena:
        print("Contraseña correcta")
        break
    else:
        print("Contraseña errónea")
        intentos -= 1
        if intentos > 0:
            sleep(10-int(10/maxIntentos*intentos))

"""
Modificar el programa anterior para que sea una función que devuelva si
el usuario ingresó o no la contraseña correctamente, mediante un valor
booleano (True o False).
"""


def passwords():
    from time import sleep
    contrasena = "contra"
    maxIntentos = 5
    intentos = maxIntentos
    while intentos != 0:
        con = input("Contraseña : ")
        if con == contrasena:
            print("Contraseña correcta")
            return True
        else:
            print("Contraseña errónea")
            intentos -= 1
            if intentos > 0:
                sleep(10-int(10/maxIntentos*intentos))
    return False
