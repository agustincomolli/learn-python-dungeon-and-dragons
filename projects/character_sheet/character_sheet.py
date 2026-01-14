def ability_modifier(score) -> int:
    """
    Calcula el modificador de un atributo según D&D

    Args:
        score (int): Valor del atributo (3 a 18)

    Returns:
        int: Modificador del atributo
    """
    return (score - 10) // 2


def get_int(prompt) -> int:
    """
    Solicita al usuario un valor de atributo válido para D&D.
    El valor debe ser un número entero entre 3 y 18 inclusive.

    Args:
        prompt (str): Mensaje al usuario

    Returns:
        int: Número entero
    """
    while True:
        try:
            number = int(input(prompt))
            if number < 3:
                print("\nEl número debe ser mayor o igual a 3\n")
            elif number > 18:
                print("\nEl número debe ser menor o igual a 18\n")
            else:
                return number
        except ValueError:
            print("\nERROR: Debes ingresar un número\n")


def create_character() -> dict:
    """
    Crea y devuelve los atributos de un personaje.

    Returns:
        dict: El diccionario con los atributos del personaje.
    """
    character = {}

    character["strength"] = get_int("Fuerza: ")
    character["dexterity"] = get_int("Destreza: ")
    character["constitution"] = get_int("Constitución: ")
    character["intelligence"] = get_int("Inteligencia: ")
    character["wisdom"] = get_int("Sabiduría: ")
    character["charisma"] = get_int("Carisma: ")

    return character


def print_ability(name: str, score: int) -> None:
    """
    Muestra en pantalla una habilidad con los valores y modificadores.

    Args:
        name (str): El nombre de la habilidad.
        score (int): La puntuación de la habilidad.
    """
    modifier = ability_modifier(score)
    sign = "+" if modifier >= 0 else ""
    print(f"{name.capitalize():<15} {score:>2} ({sign}{modifier})")


def print_character(abilities: dict) -> None:
    print("\n📜 HOJA DE PERSONAJE 📜\n")
    for name, score in abilities.items():
        print_ability(name, score)
