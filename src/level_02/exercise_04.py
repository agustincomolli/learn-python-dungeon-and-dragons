"""
EJERCICIO 4: Daño Crítico - ⭐⭐
📝 Descripción: En D&D, un golpe crítico a veces dobla los dados.
Crea die_roll = 8 y strength_mod = 3.
Calcula el daño normal (die_roll + strength_mod).
Calcula el daño crítico (die_roll * 2 + strength_mod).
Imprime ambos resultados con mensajes claros.
"""

die_roll = 8
strength_mod = 3

normal_hit = die_roll + strength_mod
critical_hit = die_roll * 2 + strength_mod

print(f"El daño normal es: {normal_hit}")
print(f"El daño crítico es: {critical_hit}")
