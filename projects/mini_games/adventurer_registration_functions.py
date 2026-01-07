def get_valid_age():
    """
    Solicita al usuario una edad válida.

    Returns:
        int: La edad del aventurero.
    """
    while True:
        try:
            age = int(input("Ingresa tu edad: "))

            if age <= 0:
                print("\nEdad inválida, tiene que ser mayor a 0.\n")
            else:
                return age
        except:
            print("\nERROR: Debes ingresar un número.\n")


def get_rank(age):
    """
    Clasifica al aventurero según su edad.

    Args:
        age (int): edad del aventurero.

    Returns:
        str: Rango del aventurero.
    """
    if age < 13:
        return "aventurero aprendiz"
    elif age >= 18:
        return "aventurero experimentado"
    else:
        return "aventurero joven"


def show_result(name, rank):
    """
    Muesta el resultado final al usuario

    Args:
        name (str): Nombre del aventurero
        rank (str): Rango del aventurero
    """
    print(name, "es un", rank)


character_name = input("Ingresa tu nombre aventurero: ")
character_age = get_valid_age()
character_rank = get_rank(character_age)
show_result(character_name, character_rank)
