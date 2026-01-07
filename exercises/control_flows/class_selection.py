"""
Escribí un programa simple que haga lo siguiente:

Pida la clase del personaje

Convierta la entrada a minúsculas

Muestre:

“Eres un guerrero fuerte” si es guerrero

“Eres un mago sabio” si es mago

“Eres un pícaro astuto” si es picaro

“Clase desconocida” en otro caso
"""


def get_class_description(character_class) -> str:
    """
    Devuelve una descripción de la clase.

    Args:
        character_class (str): La clase del aventurero.

    Returns:
        str: La descripción de la clase.
    """

    if character_class == "guerrero":
        return "Eres un guerrero fuerte"
    elif character_class == "mago":
        return "Eres un mago sabio"
    elif character_class == "picaro":
        return "Eres un pícaro astuto"
    else:
        return "Clase desconocida"


character_class = input("Ingresa la clase de aventurero que eres: ")
character_class = character_class.lower()
print(get_class_description(character_class))
