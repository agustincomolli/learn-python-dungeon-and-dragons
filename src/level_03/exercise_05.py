"""
EJERCICIO 5: Generador de Héroes Interactivo - ⭐⭐⭐
📝 Descripción: Crea un archivo en src/level_03/character_creator.py.
Este será tu primer programa "completo". Debe:
Pedir el Nombre y Clase del héroe.
Pedir las puntuaciones de Inteligencia y Constitución.
Calcular automáticamente el Modificador de Inteligencia y el Spell Save DC (8 + 2 + mod_int).
Calcular los Puntos de Vida (6 + mod_con).
Imprimir una ficha formateada con f-strings que muestre todos los datos calculados.
"""

print("Generador de Héroes Interactivo 💪🏻")

character_name = input("¿Cuál es tu nombre aventurero? ")
character_class = input("¿Cuál es tu profesión? ")
character_int = int(input("Inteligencia: "))
character_con = int(input("Constitución: "))

int_modifier = (character_int - 10) // 2
con_modifier = (character_con - 10) // 2

character_spell_save_dc = 8 + 2 + int_modifier
character_hp = 6 + con_modifier

print(f"🛡️ {character_name} - {character_class} 🛡️")
print(f"\nTirada de salvación de hechizo: {character_spell_save_dc}")
print(f"Total de puntos de vida: {character_hp}")