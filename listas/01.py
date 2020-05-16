"""
Ejercicio 01

Descargar una copia del archivo "romeo.txt" desde
http://www.pythonlearn.com/code3/romeo.txt. Escribir un programa para abrir el
fichero y leerlo línea a línea. Por cada línea separar las palabras en una
lista de palabras usando la función split. Las palabras no deben estar
repetidas en la lista. Cuando la lista esté completa, visualizar el resultado
en orden alfabético.
"""


try:
    fhandle = open("romeo.txt")
except IOError:
    print("El fichero no existe.")
    exit()

words_list = list()


for line in fhandle:
    for word in line.split():
        if word not in words_list:
            words_list.append(word)
words_list.sort()

for word in words_list:
    print(word, sep=' ', end=' ')

print()
