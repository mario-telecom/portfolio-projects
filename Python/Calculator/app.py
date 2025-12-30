# app.py - Calculadora simple en Python


def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división por cero"


print("Calculadora simple")
print("Suma 2 + 3 =", suma(2, 3))
print("Resta 5 - 2 =", resta(5, 2))
print("Multiplicación 4 * 3 =", multiplicacion(4, 3))
print("División 10 / 2 =", division(10, 2))
