"""
Crear una lista vacía rolls

Tirar 3 d6

Guardar cada tirada

Mostrar:

    todas las tiradas
    la mayor
    la suma total
"""

import random


def roll_dice(quantity: int, sides: int) -> list:
    """
    Simula una tirada de dados de D&D.

    Args:
        quantity (int): Cantidad de dados a tirar.
        sides (int): cantidad de caras de cada dado.

    Returns:
        list: La lista con los resultados.
    """
    rolls = []
    for _ in range(quantity):
        rolls.append(random.randint(1, sides))

    return rolls


rolls = roll_dice(3, 6)

print(f"Tiradas: {rolls}")
print(f"La mejor: {max(rolls)}")
print(f"La suma de las tiradas es: {sum(rolls)}")
