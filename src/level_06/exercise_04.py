"""
EJERCICIO 4: El Simulador de Ventaja - ⭐⭐
📝 Descripción: Pide al usuario que introduzca dos tiradas de d20 
(porque tiene ventaja). Pide la DC a superar. 
Si la tirada1 es mayor o igual a la DC O la tirada2 es mayor o 
igual a la DC, imprime "¡Éxito con ventaja!". De lo contrario, imprime "Fallo".
"""

print("*** El Simulador de Ventaja ***\n")

print("¡Tienes ventaja, tira dos dados d20")
roll_1 = int(input("Tirada 1: "))
roll_2 = int(input("Tirada 2: "))
dc = int(input("Clase de Dificultad: "))

if roll_1 >= dc or roll_2 >= dc:
    print("¡Éxito con ventaja!")
else:
    print("Fallo")