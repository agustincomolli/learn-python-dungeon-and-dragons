"""
EJERCICIO 2: El Juicio del Dado - ⭐
📝 Descripción: Pide al usuario que introduzca el resultado de un d20.
Si es 1, imprime "¡PIFIA! Te tropiezas con tu propia túnica".
Si es 20, imprime "¡CRÍTICO! El enemigo tiembla ante ti".
Si no es ninguno de esos, imprime "Una tirada normal".
"""
print("*** El Juicio del Dado ***\n")

dice_rolled = int(input("Resultado de un d20: "))
if dice_rolled == 1:
    print("¡PIFIA! Te tropiezas con tu propia túnica")
elif dice_rolled == 20:
    print("¡CRÍTICO! El enemigo tiembla ante ti")
else:
    print("Una tirada normal")