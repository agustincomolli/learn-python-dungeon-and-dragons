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


def ability_modifier(score) -> int:
    """
    Calcula el modificador de un atributo según D&D

    Args:
        score (int): Valor del atributo (3 a 18)

    Returns:
        int: Modificador del atributo
    """
    return (score - 10) // 2


def print_character_sheet(character:dict):
    """
    Muestra la hoja del personaje D&D

    Args:
        character (dict): Diccionario con los datos del personaje.
    """
    print("\n📜 HOJA DE PERSONAJE 📜\n")
    for ability, score in character.items():
        mod = ability_modifier(score)
        if mod >= 0:
            mod_text = f"+{mod}"
        else:
            mod_text = str(mod)
        print(f"{ability.capitalize():<15} {score:>2} ({mod_text})")


character = {}

character["strength"] = get_int("Fuerza: ")
character["dexterity"] = get_int("Destreza: ")
character["constitution"] = get_int("Constitución: ")
character["intelligence"] = get_int("Inteligencia: ")
character["wisdom"] = get_int("Sabiduría: ")
character["charisma"] = get_int("Carisma: ")

print_character_sheet()