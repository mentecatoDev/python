"""

a) Escribir una función que reciba una tupla con nombres, y para cada nombre
retorne una lista con un menasaje para cada nombre del tipo:
"Estimado [nombre],vote por mí".

>>> campaign(("José", "Ango", "Juana", "Luis", "Paco"))
['Estimado José, vote por mí',\
 'Estimado Ango, vote por mí',\
 'Estimado Juana, vote por mí',\
 'Estimado Luis, vote por mí',\
 'Estimado Paco, vote por mí']
"""


def campaign(names):
    messages = []
    for name in names:
        messages.append("Estimado %s, vote por mí" % name)
    return messages


if __name__ == "__main__":
    import doctest
    doctest.testmod()
