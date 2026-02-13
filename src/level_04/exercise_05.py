"""
EJERCICIO 5: El Simulador de Pruebas de Habilidad - ⭐⭐⭐
📝 Descripción: Crea un archivo src/level_04/skill_check.py.
Define una variable door_dc = 15.
Pide al usuario su Nombre.
Pide al usuario que "tire un dado" (que introduzca un número del 1 al 20).
Pide al usuario su Modificador de Inteligencia (ej: 2).
Calcula el total_roll (Tirada + Modificador).
Crea una variable booleana success que compare si total_roll es mayor o igual a door_dc.
Muestra un resumen:
"Héroe: [Nombre]"
"Resultado de la tirada: [total_roll]"
"¿Logró descifrar el enigma? [True/False]"
"""

DOOR_DC = 15
character_name = input("¿Cómo te llamas aventurero? ")
d20 = int(input("Tira un dado D20 e introduce el resultado: "))
int_modifier = int(input("¿Cuál es tu modificador de inteligencia? "))
total_roll = d20 + int_modifier
success = total_roll >= DOOR_DC
print(f"Héroe: {character_name}")
print(f"Resultado de la tirada: {total_roll}")
print(f"¿Logró descifrar el enigma? {success}")