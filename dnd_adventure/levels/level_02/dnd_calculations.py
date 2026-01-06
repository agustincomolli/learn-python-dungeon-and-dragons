"""
Usa la variable dexterity = 14 de Aelan. 
Calcula su modificador usando la fórmula simplificada: (dexterity - 10) // 2.

Usa el operador // para que el resultado sea un número entero.

Imprime: "El modificador de Destreza de Aelan es: X".
"""
dexterity =  14
print(f"El modificador de Destreza de Aelan es: {(dexterity - 10) // 2}")

"""
Has encontrado un cofre con 157 monedas de oro. Tienes 3 compañeros de aventura (son 4 personas en total).

Calcula cuántas monedas le tocan a cada uno de forma exacta (usa //).

Calcula cuántas monedas sobran y se quedan en el fondo del cofre (usa el operador módulo %, que devuelve el resto de una división).

Pista: sobrante = 157 % 4
"""
TREASURE = 157
PLAYERS = 4

coins_per_player = TREASURE // PLAYERS
coins_remainder = TREASURE % PLAYERS

print(f"Cada jugador recibe {coins_per_player} monedas de oro y quedan en el fondo del cofre {coins_remainder} moneda/s.")