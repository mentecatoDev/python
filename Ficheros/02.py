"""
Ejercicio 02
7.2 Escribe un programa que solicite un nombre de fichero, lo abra, lea y
busque líneas de la forma:

X-DSPAM-Confidence: 0.8475

Contar estas líneas y extraer los valores en punto flotante de cada una de
ellas para finalmente calcular la media de esos valores y generar una salida
como la que se muestra a continuación. Media de correo basura: 0.750718518519
No utilizar la función sum() o una variable que se llame sum en la solución.
Se puede descargar un fichero con los datos de prueba
http://www.pythonlearn.com/code/mbox-short.txt.
"""

leyendo = True
while leyendo:
    try:
        fichero = input("Nombre de fichero: ")
        manejador = open(fichero)
        leyendo = False
    except IOError:
        print("El fichero no existe.")
cont = 0
total = 0
for linea in manejador:
    if linea.startswith("X-DSPAM-Confidence:"):
        numero = float(linea[linea.find(" ") + 1:].strip())
        cont += 1
        total += numero
        print(numero)

print("Media de correo basura: ", total/cont)
