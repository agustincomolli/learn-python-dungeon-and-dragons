"""
EJERCICIO 5: El Oráculo de la Vida y la Mente - ⭐⭐⭐
📝 Descripción: Crea un archivo src/level_02/calculator.py.
Define constitution = 13 e intelligence = 15.
Calcula los modificadores de ambos usando la fórmula sagrada.
Calcula tu HP Máximo (Para un Mago es: 6 + modificador_de_constitucion).
Calcula tu "Dificultad de Salvación de Conjuros" (Spell Save DC). La fórmula es: 8 + 2 
(bono de competencia) + modificador_de_inteligencia.
Imprime una ficha que diga:
"MODIFICADOR DE CONSTITUCIÓN: [valor]"
"PUNTOS DE VIDA: [valor]"
"DC DE CONJUROS: [valor]"
"""

constitution = 13
intelligence = 15
HIT_DIE = 6

con_modifier = (constitution - 10) // 2
int_modifier = (intelligence - 10) // 2

total_hp = HIT_DIE + con_modifier
spell_save_dc = 8 + 2 + int_modifier

print(f"MODIFICADOR DE CONSTITUCIÓN: {con_modifier}")
print(f"PUNTOS DE VIDA: {total_hp}")
print(f"DC DE CONJUROS: {spell_save_dc}")