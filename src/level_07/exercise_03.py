"""
EJERCICIO 3: Botín de Guerra - ⭐⭐
📝 Descripción: Tienes una lista loot = ["Monedas de oro", "Gema roja"].
Pide al usuario que introduzca un nuevo objeto encontrado.
Añádelo a la lista usando .append().
Imprime la lista actualizada y el número total de objetos.
"""

print("*** Botín de Guerra ***\n")

loot = ["Monedas de oro", "Gema roja"]
loot.append(input("Nuevo objeto: "))

print(f"Botín: {loot}. Hay {len(loot)} objetos")