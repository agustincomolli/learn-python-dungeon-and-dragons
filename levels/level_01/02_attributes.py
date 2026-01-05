"""
Añade al archivo anterior tres variables numéricas: fuerza, destreza y constitucion. 
Según el SRD 5.1, una puntuación de 10 es la media humana. 
Asigna valores entre 3 y 18. Imprime la suma total de estos tres atributos.
"""

characters_name = "Aelan Valdorien"
characters_race = "Humano"
characters_class = "Mago"

print(f"Mi nombre es {characters_name} y soy un {characters_class} {characters_race}.")

strength = 8
dexterity = 14
constitution = 15

print(f"La suma de los tres valores es {strength + dexterity + constitution}")
