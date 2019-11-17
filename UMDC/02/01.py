"""
Ejercicio 01

Escribir dos funciones que permitan calcular:
    La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
    La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
"""


def hms_seg(h, m, s):
    return ((h*60)+m)*60+s


def seg_hms(s):
    horas = s//3600
    s = s % 3600
    minutos = s//60
    segundos = s % 60
    return (horas, minutos, segundos)
