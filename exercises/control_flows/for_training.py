"""
Pedir cuántos días entrena el aventurero

Mostrar:

Día 1: entrenamiento completo
Día 2: entrenamiento completo
...
"""


def get_int(prompt: str) -> int:
    """
    Solicita un número entero
    
    Args:
        prompt (str): Mensaje al usuario
    
    Returns:
        int: El número ingresado
    """
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("\nERROR: Debes ingresar un número.\n")


days = get_int("¿Cuántos días entrenará tu aventurero? ")

for i in range(days):
    print(f"Día {i + 1}: entrenamiento completo")