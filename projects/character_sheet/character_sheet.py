def ability_modifier(score) -> int:
    """
    Calcula el modificador de un atributo según D&D

    Args:
        score (int): Valor del atributo (3 a 18)

    Returns:
        int: Modificador del atributo
    """
    return (score - 10) // 2


def print_ability(name: str, score: int) -> None:
    """
    Muestra en pantalla una habilidad con los valores y modificadores.

    Args:
        name (str): El nombre de la habilidad.
        score (int): La puntuación de la habilidad.
    """
    modifier = ability_modifier(score)
    sign = "+" if modifier >= 0 else ""
    print(f"{name}: {score} ({sign}{modifier})")


def print_character(abilities: dict) -> None:
    print("=== CHARACTER SHEET ===")
    for name, score in abilities.items():
        print_ability(name, score)


abilities = {
    "Strength": 14,
    "Dexterity": 12,
    "Constitution": 10,
    "Intelligence": 8,
    "Wisdom": 8,
    "Charisma": 16
}

print_character(abilities)
