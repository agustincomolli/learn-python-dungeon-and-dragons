from character_sheet import create_character, print_character, ability_modifier
from dice import roll_check

character = create_character()
print_character(character)

print("\n🎲 Prueba de Sabiduría\n")

wisdom_mod = ability_modifier(character["wisdom"])
result = roll_check(modifier=wisdom_mod, is_advantage=True)

print(f"Resultado final: {result}")