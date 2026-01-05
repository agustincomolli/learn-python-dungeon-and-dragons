"""
Aelan intenta abrir la puerta.

Crea una variable clase_dificultad = 15.

Crea una variable tirada_dado = 13.

Calcula el resultado_final (tirada_dado + modificador de destreza de Aelan que calculaste antes, que era 2).

Escribe un bloque if/else:

Si el resultado_final es mayor o igual a la clase_dificultad, imprime: "¡ÉXITO! La puerta se desliza silenciosamente."

De lo contrario, imprime: "¡FALLO! La puerta no se mueve y un eco resuena en el pasillo."
"""
DC = 15  # Difficulty class
DEXTERITY = 14
modifier = (DEXTERITY - 10) // 2
rolled_dice = 13
if rolled_dice + modifier >= DC:
    print("¡ÉXITO! La puerta se desliza silenciosamente.")
else:
    print("¡FALLO! La puerta no se mueve y un eco resuena en el pasillo.")

"""
En D&D los personajes tienen alineamientos (Legal, Neutral, Caótico).

Crea una variable puntos_karma y asígnale un valor (ejemplo: 5).

Usa if/elif/else para clasificar al personaje:

Si puntos_karma es mayor a 10: "Tu alma brilla con Legalidad."

Si puntos_karma está entre 0 y 10: "Eres un ser Neutral."

Si puntos_karma es menor a 0: "El Caos te consume."
"""
karma_points = 5
if karma_points > 10:
    print("Tu alma brilla con Legalidad.")
elif karma_points < 0:
    print("El Caos te consume.")
else:
    print("Eres un ser Neutral.")
