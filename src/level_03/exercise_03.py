"""
EJERCICIO 3: El Calculador de Modificadores en Vivo - ⭐⭐
📝 Descripción: Pide al usuario que introduzca su puntuación de Constitución. 
Convierte la entrada a número. Calcula el modificador (recuerda: (stat - 10) // 2). 
Luego, calcula sus Puntos de Vida (HP) si fuera un Mago (HP = 6 + modificador). 
¡Dile cuánta vida tiene!
"""

constitution = int(input("Constitución: "))
modifier = (constitution - 10) // 2
hp = 6 + modifier
print(f"Tienes {hp} puntos de vida")