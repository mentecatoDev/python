"""
Ejercicio 01

Escribir un programa que lea las palabras de un fichero words.txt
(http://www.pythonlearn.com/code3/words.txt) y las almacene como claves en un
diccionario. No importan los valores.
Posteriormente leer palabras desde teclado y utilizar el operador in como una
forma rápida de comprobar si las palabras están dentro del diccionario o no.
"""

try:
    fhandle = open("words.txt")
except IOError:
    print("El fichero no existe")
    exit()

text = fhandle.read()
word_list = text.split()
dictionary = dict()
for word in word_list:
    dictionary[word] = dictionary.get(word, 0) + 1

while True:
    word = input("Introduzca una palabra (* para fin): ")
    if word == "*":
        fhandle.close()
        break
    if word in dictionary:
        print("La palabra %s SÍ está en el texto" % word)
    else:
        print("La palabra %s NO está en el texto" % word)
