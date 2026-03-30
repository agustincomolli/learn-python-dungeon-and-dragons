"""
EJERCICIO 1: La Llama de la Vela - ⭐
📝 Descripción: Una vela mágica dura 5 turnos. 
Crea un bucle while que imprima "La vela brilla..." y 
reduzca su duración hasta que se apague (llegue a 0).
"""

print("*** La Llama de la Vela ***\n")

turns_left = 5

while turns_left > 0:
    print("La vela brilla... 🕯️")
    turns_left = turns_left - 1

print("\nLa vela se apagó")