"""
b) Escribir una función que reciba una tupla con nombres, una posición
de origen p y una cantidad n, e imprima el mensaje anterior para los n
nombres que se encuentran a partir de la posición p.

>>> campaign(("José", "Ango", "Juana", "Luis", "Paco"), 2, 3)
['Estimado Juana, vote por mí',\
 'Estimado Luis, vote por mí',\
 'Estimado Paco, vote por mí']

"""


def campaign(names, pos, num):
    messages = []
    for i in range(pos, pos + num):
        messages.append("Estimado %s, vote por mí" % names[i])
    return messages


if __name__ == "__main__":
    import doctest
    doctest.testmod()





