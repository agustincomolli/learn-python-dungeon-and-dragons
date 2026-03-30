"""
EJERCICIO 5: Horda de Trasgos - ⭐⭐⭐
📝 Descripción: Crea un archivo src/level_09/horde_battle.py.
Crea una lista llamada goblins que contenga los nombres de 5 trasgos 
(ej: "Trasgo Gruñón", "Trasgo Narizotas", etc.).

Crea una función llamada attack_monster(monster_name) que imprima: 
"⚔️ Atacas a [monster_name] y lo derrotas".

Usa un bucle for para recorrer tu lista de trasgos.

Dentro del bucle, llama a la función attack_monster pasándole el nombre del trasgo actual.

Al terminar el bucle, imprime un mensaje de victoria final.
"""

print("*** Horda de Trasgos ***\n")

goblins = ["Trasgo Gruñón", "Trasgo Narizotas", "Trasgo Tuerto", "Trasgo Enano", "Trasgo Viejo"]

def attack_monster(monster_name):
    print(f"⚔️  Atacas a {monster_name} y lo derrotas")


for goblin in goblins:
    attack_monster(goblin)

print("\n¡Has derrotado a todos tus enemigos! 💪")