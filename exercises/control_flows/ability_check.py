import random


def ability_modifier(score: int) -> int:
    """
    Devuelve el modificador según la habilidad

    Args:
        score (int): Puntuación de habilidad.

    Return:
        int: El valor del modificador.
    """
    return (score - 10) // 2


character = {
    "strength": 14,
    "dexterity": 12,
    "constitution": 15,
    "intelligence": 10,
    "wisdom": 8,
    "charisma": 13
}

ability = "wisdom"
score = character[ability]

roll = random.randint(1, 20)
modifier = ability_modifier(score)
total = roll + modifier

print(f"Habilidad: {ability}")
print(f"Tirada: {roll}")
print(f"Modificador: {modifier}")
print(f"Total: {total}")

if total >= 10:
    print("Resultado: ÉXITO")
else:
    print("Resultado: FALLO")
