"""
EJERCICIO 4: Suma de Tesoros - ⭐⭐
📝 Descripción: Tienes una lista de valores de gemas: gems = [10, 50, 100, 25]. 
Crea una variable total_gold = 0. 
Usa un bucle for para recorrer la lista de gemas e ir sumando su valor a total_gold. 
Al final del bucle, imprime el total.
"""

print("*** Suma de Tesoros ***\n")

gems = [10, 50, 100, 25]
total_gold = 0

for gem in gems:
    total_gold = total_gold + gem

print(f"La suma del tesoro es: {total_gold}")