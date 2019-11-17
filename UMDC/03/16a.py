"""
Ejercicio 16a

Escribir funciones que permitan encontrar:

a) El máximo o mínimo de un polinomio de segundo grado (dados los
coeficientes a, b y c), indicando si es un máximo o un mínimo.
http://es.wikihow.com/encontrar-f%C3%A1cilmente-el-valor-m%C3%A1ximo-o-m%C3%ADnimo-de-una-funci%C3%B3n-cuadr%C3%A1tica
"""


def maxmin(a, b, c):
    if a > 0:
        return (-(b**2)/(4*a) + c, "máximo")
    else:
        return (-(b**2)/(4*a) + c, "mínimo")


(valor, Mm) = maxmin(-1, 1, 1)
print("Es un", Mm, "y su valor es", valor)
