"""
EJERCICIO 3: El Guardián del Tesoro - ⭐⭐
📝 Descripción: Un cofre requiere exactamente 3 llaves para abrirse. 
Pide al usuario que diga cuántas llaves tiene. 
Crea una variable booleana can_open que sea verdadera solo si el número de 
llaves es exactamente igual a 3.
"""

keys = int(input("¿Cuántas llaves tienes para abrir el cofre? "))
KEYS_TO_OPEN = 3
can_open = keys == KEYS_TO_OPEN

print(f"¿Puedes abrir el cofre? {can_open}")