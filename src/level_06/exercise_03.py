"""EJERCICIO 3: El Dilema del Pícaro - ⭐⭐
📝 Descripción: Para abrir un cofre sin que explote, el pícaro debe:
Tener dexterity mayor a 14.
Y NO debe estar is_trapped (pide esto como "si/no" y conviértelo a booleano).
Si ambas condiciones se cumplen, el cofre se abre seguro.
"""

print("*** El Dilema del Pícaro ***\n")

dexterity = int(input("Destreza: "))
is_trapped_str = input("¿Está atrapado? [s/n]: ")
if is_trapped_str == "s" or is_trapped_str == "S":
    is_trapped = True
else:
    is_trapped = False

if dexterity > 14 and not is_trapped:
    print("Abriste el cofre sin problemas 📦")
else:
    print("¡Sonaste el cofre explotó! 🔥")