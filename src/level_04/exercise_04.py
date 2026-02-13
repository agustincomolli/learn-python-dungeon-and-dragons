"""
EJERCICIO 4: ¿Eres un Mago, Harry? - ⭐⭐
📝 Descripción: Pide al usuario su clase. 
Crea una comparación que devuelva True si la clase es diferente de "Guerrero". 
Imprime: "¿Eres alguien que usa el cerebro o la magia? [Resultado]".
"""

character_class = input("¿Cuál es tu clase? ")
is_mage = character_class != "Guerrero"

print(f"¿Eres alguien que usa el cerebro o la magia? {is_mage}")