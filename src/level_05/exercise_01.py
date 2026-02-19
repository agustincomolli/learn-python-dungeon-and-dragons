"""
EJERCICIO 1: El Portero de la Taberna - ⭐
📝 Descripción: Pide al usuario su age. Si es mayor o igual a 18, 
imprime "Puedes pasar a beber hidromiel". De lo contrario (else), 
imprime "Solo servimos leche de cabra para los menores".
"""

print("*** El Portero de la Taberna ***\n")

age = int(input("¿Qué edad tienes aventurero? "))
if age >= 18:
    print("Puedes pasar a beber hidromiel")
else:
    print("Solo servimos leche de cabra para los menores")