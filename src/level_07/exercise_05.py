"""
EJERCICIO 5: El Gestor de Inventario de Aelan - ⭐⭐⭐
📝 Descripción: Crea un archivo src/level_07/inventory_manager.py.
Crea una lista inventory con el equipo inicial de un mago: 
"Vara de cristal", "Grimorio", "Raciones".
Muestra al usuario su inventario actual y cuántos objetos tiene.
Pregúntale: "¿Qué objeto acabas de encontrar?".
Añade ese objeto a la lista.
Pregúntale: "¿Qué objeto quieres usar/tirar?".
Quita ese objeto de la lista.
Muestra el inventario final y destaca cuál es el primer objeto de la lista 
(tu objeto principal) usando f-strings.
"""

print("*** El Gestor de Inventario de Aelan ***\n")

inventory = ["Vara de cristal", "Grimorio", "Raciones"]

print(f"Inventario: {inventory} - {len(inventory)} objetos.\n")
inventory.append(input("¿Qué objeto acabas de encontrar? "))
inventory.remove(input("¿Qué objeto quieres usar/tirar? "))
print(f"\nInventario final: {inventory}. Primer item: {inventory[0]}")