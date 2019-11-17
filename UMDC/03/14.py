"""
Ejercicio 14

Escribir una función que dada la cantidad de ejercicios de un examen, y el
porcentaje necesario de ejercicios bien resueltos necesario para aprobar
dicho examen, revise un grupo de examenes. Para ello, en cada paso debe
preguntar la cantidad de ejercicios resueltos por el alumno, indicando con un
valor centinela que no hay más examenes a revisar. Debe mostrar por pantalla
el porcentaje correspondiente a la cantidad de ejercicios resueltos respecto
a la cantidad de ejercicios del examen y una leyenda que indique si aprobó o
no.
"""


def examen(numEje, porcentaje):
    while True:
        leyendo = True
        while leyendo:
            try:
                resueltos = float(input("Número de ejercicios resueltos",
                                        "(-1 para terminar): "))
                leyendo = False
            except ValueError:
                print("Introduzca una cantidad numérica")
        if resueltos == -1:
            return
        else:
            nota = 100/numEje * resueltos
            print("El % de ejercicios resueltos es", 100/numEje * resueltos)
            if nota < porcentaje:
                print("Suspendido")
            else:
                print("Aprobado")


examen(50, 25)
