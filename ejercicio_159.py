# Ejercicio 159: multiplicar elementos de una lista
def HaroldOlivera(lista):
    resultado = 1
    for n in lista:
        resultado *= n
    return resultado
print(HaroldOlivera([1, 2, 3, 4]))
