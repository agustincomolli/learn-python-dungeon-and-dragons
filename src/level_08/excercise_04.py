"""
EJERCICIO 4: El Calculador de Daño - ⭐⭐
📝 Descripción: Crea una función llamada calculate_damage(die_roll, modifier). 
Debe recibir el valor de un dado y un modificador, sumarlos y retornar el total. 
Invoca la función y guarda el resultado en una variable llamada final_damage.
"""

print("*** El Calculador de Daño ***\n")

def calculate_damage(die_roll, modifier):
    return die_roll + modifier


total_damage = calculate_damage(15, 2)