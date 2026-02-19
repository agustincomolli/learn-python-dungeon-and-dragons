"""
EJERCICIO 4: Clasificación de Héroes - ⭐⭐
📝 Descripción: Pide al usuario su puntuación de Inteligencia.
Si es 18 o más, imprime "Eres un Archimagomago".
Si está entre 14 y 17, imprime "Eres un erudito".
Si está entre 10 y 13, imprime "Tienes una inteligencia promedio".
Si es menor a 10, imprime "Prefieres usar los músculos".
"""

print("*** Clasificación de Héroes ***\n")

intelligence = int(input("Inteligencia: "))
if intelligence >= 18:
    print("Eres un Archimagomago")
elif intelligence >= 14 and intelligence <= 17:
    print("Eres un erudito")
elif intelligence >= 10 and intelligence <= 13:
    print("Tienes una inteligencia promedio")
else:
    print("Prefieres usar los músculos")