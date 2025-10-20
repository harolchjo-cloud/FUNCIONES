# Ejercicio 80: contar vocales
def HaroldOlivera(texto):
    return sum(1 for c in texto.lower() if c in 'aeiou')
print(HaroldOlivera('Python'))
