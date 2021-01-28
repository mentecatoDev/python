"""
c) Modificar las funciones anteriores para que tengan en cuenta el género del
destinatario, para ello, deberán recibir una tupla de tuplas, conteniendo el
nombre y el género.

>>> campaign_3a((("H", "José"), ("H", "Ango"), ("M", "Juana"), ("H", "Luis"),
... ("H", "Paco")))
['Estimado José, vote por mí',\
 'Estimado Ango, vote por mí',\
 'Estimada Juana, vote por mí',\
 'Estimado Luis, vote por mí',\
 'Estimado Paco, vote por mí']

>>> campaign_3b((("H", "José"), ("H", "Ango"), ("M", "Juana"), ("H", "Luis"),
... ("H", "Paco")),1, 2)
['Estimado Ango, vote por mí',\
 'Estimada Juana, vote por mí']
"""


def campaign_3a(names):
    messages = []
    for name in names:
        messages.append("Estimad" + ("o" if name[0] == "H" else "a") +
                        " %s, vote por mí" % name[1])
    return messages


def campaign_3b(names, pos, num):
    messages = []
    for i in range(pos, pos + num):
        messages.append("Estimad" + ("o" if names[i][0] == "H" else "a") +
                        " %s, vote por mí" % names[i][1])
    return messages


if __name__ == "__main__":
    import doctest
    doctest.testmod()
