"""
Ejercicio 3
===========
Escribir un programa que lea un archivo e imprima las letras en orden decreciente de
frecuencia de aparición. El programa debería convertir toda la entrada a minúsculas
y solo contar las letras a-z (excluir la "ñ"). No se debeen contar espacios, dígitos,
signos de puntuación o cualquier otro carácter. Buscar textos en diferentes lenguas y
ver cómo la frecuencia de las letras varían entre lenguajes. Comparar los resultados
con las tablas que se puede encontrar en wikipedia.org/wiki/Letter_frequencies.
"""
import string

try:
    fhandle = open(input("Introduzca el nombre del fichero: "))
except IOError:
    print("El fichero no existe")
    exit()

full_string = fhandle.read()
alphabet = dict()
for letter in full_string:
    letter = letter.lower()
    if letter in string.ascii_lowercase:
        alphabet[letter] = alphabet.get(letter, 0) + 1
total = 0
ordered_list = []
for key, value in alphabet.items():  
    total += alphabet[key]
    ordered_list += [(value, key)]
ordered_list.sort(reverse=True)
for tupla in ordered_list:
    print("%s %.2f%%" % (tupla[1], tupla[0]*100/total))
