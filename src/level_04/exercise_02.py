"""
EJERCICIO 2: La Prueba de Fuerza - ⭐
📝 Descripción: Pide al usuario que introduzca su Fuerza (con int(input())). 
Compara si esa fuerza es mayor o igual a 15 (una DC difícil). 
Imprime: "¿Eres lo suficientemente fuerte? [True/False]".
"""

strength = int(input("Fuerza: "))
DC = 15
is_strong = strength >= DC

print(f"¿Eres lo suficientemente fuerte? {is_strong}")