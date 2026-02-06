"""
EJERCICIO 2: El Cambio de Moneda - ⭐
📝 Descripción: Un mercader te ofrece 10 piezas de plata por cada pieza de oro. 
Pide al usuario que introduzca cuántas monedas de oro tiene. 
Convierte la entrada a número y calcula cuántas piezas de plata recibiría.
"""

print("*** El Cambio de Moneda 🪙 ***")
gold_coins = int(input("¿Cuántas monedas de oro tienes? "))
silver_coins = gold_coins * 10
print(f"Te daré {silver_coins} monedas de plata por todo ese oro.")