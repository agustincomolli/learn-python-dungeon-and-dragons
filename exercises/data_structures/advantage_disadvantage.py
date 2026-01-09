"""
Tirar 2 d20

Guardarlos en una lista

Mostrar:

las tiradas
ventaja (mayor)
desventaja (menor)
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


rolls = roll_dice(2, 10)
print(f"Tiradas: {rolls}")
print(f"Ventaja: {max(rolls)}")
print(f"Desventaja: {min(rolls)}")