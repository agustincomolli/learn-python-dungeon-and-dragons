"""
EJERCICIO 1: El Puente de Khazad-dûm - ⭐
📝 Descripción: Para cruzar el puente necesitas ser "Mago" Y tener un nivel mayor a 5. 
Pide estos dos datos al usuario y usa and para decidir si puede pasar o si "No pasará".
"""

print("*** El Puente de Khazad-dûm ***\n")

character_class = input("¿Qué clase de aventurero eres? ")
character_lvl = int(input("¿Cuál es tu nivel? "))

if character_class == "Mago" and character_lvl > 5:
    print("Puedes pasar")
else:
    print("¡You can not pass!")