def get_strength() -> int:
    """
    Solicita al usuario la fuerza del aventurero.

    Returns:
        int: la fuerza del aventurero.
    """
    while True:
        try:
            strength = int(input("Fuerza: "))
            return strength
        except:
            print("\nERROR: debes ingresar un número.\n")


def strength_rank(strength) -> str:
    """
    Clasifica la fuerza del aventurero

    Args:
        strength (int): Valor de fuerza.

    Returns
        str: Rango de fuerza
    """
    if strength < 10:
        return "Tu fuerza es baja, deberías evitar el combate cuerpo a cuerpo"
    elif strength >= 15:
        return "Tu fuerza es impresionante"
    else:
        return "Tienes una fuerza decente"


strength = get_strength()
print(strength_rank(strength))