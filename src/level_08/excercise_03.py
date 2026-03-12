"""
EJERCICIO 3: El Alquimista de Modificadores - ⭐⭐
📝 Descripción: Crea una función llamada get_modifier(score). 
Debe recibir una puntuación de estadística (ej: 15), 
calcular el modificador (score - 10) // 2 y retornar (return) el resultado.
Luego, fuera de la función, imprime: "Tu modificador es: [resultado]".
"""

print("*** El Alquimista de Modificadores ***\n")

def get_modifier(score):
    return (score - 10) // 2


modifier = get_modifier(15)

print(f"Tu modificador es: {modifier}")