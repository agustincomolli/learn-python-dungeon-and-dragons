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


def roll_check(modifier: int = 0, is_advantage: bool = False, is_disadvantage: bool = False) -> int:
    """
    Devuelve una tirada de comprobación.

    Args:
        modifier (int): Modificador de habilidad del personaje.
        is_advantage (bool): Indica si la tirada tiene ventaja.
        is_disadvantage (bool): Indica si la tirada tiene desventaja.

    Returns:
        int: Devuelve el valor de la tirada con la suma de su modificador.
    """
    rolls = roll_dice(2 if is_advantage or is_disadvantage else 1, 20)

    print(f"Tiradas: {rolls}")

    if is_advantage:
        result = max(rolls)
    elif is_disadvantage:
        result = min(rolls)
    else:
        result = rolls[0]

    return result + modifier
