# Calculo de vida para un Mago de nivel 1
hit_die = 6 # El Mago usa un d6
constitution = 13
con_modifier = (constitution - 10) // 2 # Resultado 1

total_hp = hit_die + con_modifier

print(f"Tus puntos de vida (HP) totales son: {total_hp}")