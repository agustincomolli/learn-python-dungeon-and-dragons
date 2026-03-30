"""
EJERCICIO 3: El Contador de Flechas - ⭐⭐
📝 Descripción: Un arquero tiene 10 flechas. 
Crea un bucle que cuente desde 10 hasta 1 (hacia atrás). 
En cada vuelta imprime: "Disparando flecha... Quedan [X] flechas".
Pista: Investiga range(10, 0, -1).
"""

print("*** El Contador de Flechas ***\n")

for i in range(10, 0, -1):
    print(f"Disparando flecha... Quedan {i - 1} flechas")