#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Ejercicio: Calculadora de funciones básicas
Para ejecutarlo, desde la shell:
$ python check.py login_github
"""
import sys


def suma(sumando1, sumando2):
    return (sumando1 + sumando2)

    
def resta(minuendo, sustraendo):
    return (minuendo - sustraendo)


def multiplicacion(factor1, factor2):
    return (factor1 * factor2)


def division(dividendo, divisor):
    return (dividendo / divisor)

if len(sys.argv) != 4:
    print "ERROR: Número de argumentos incorrecto"
    sys.exit()

if (sys.argv[1] != "suma" and sys.argv[1] != "resta" and \
sys.argv[1] != "multiplicacion" and sys.argv[1] != "division"):
    print "ERROR: Nombre de operación incorrecto"
    sys.exit()
try:
    factor1 = int(sys.argv[2])
    factor2 = int(sys.argv[3])
except ValueError:
    print "ERROR: los factores deben ser números enteros"

if sys.argv[1] == ("suma"):
    resultado = suma(factor1, factor2)
elif sys.argv[1] == ("resta"):
    resultado = resta(factor1, factor2)
elif sys.argv[1] == ("multiplicacion"):
    resultado = multiplicacion(factor1, factor2)
elif sys.argv[1] == ("division"):
    try:
        resultado = division(factor1, factor2)
    except ZeroDivisionError:
        print "Error: división entre 0"
        sys.exit()

print ("El resultado de la " + sys.argv[1] + " es: " + str(resultado))
