import random


def roll_dice(sides: int) -> int:
    """
    Simula la tirada de 1 dado

    Args:
        sides (int): Cantidad de caras que tiene el dado

    Returns:
        int: Resultado de la tirada
    """
    return random.randint(1, sides)


print(f"🎲 d20: {roll_dice(20)}")
print(f"🎲 d6: {roll_dice(6)}")
