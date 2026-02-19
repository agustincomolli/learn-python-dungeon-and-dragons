"""
EJERCICIO 5: El Simulador de Encuentros - ⭐⭐⭐
📝 Descripción: Crea un archivo src/level_05/encounter.py.
Define una GOBLIN_DC = 12.
Pide al usuario su Nombre.
Pregúntale qué quiere hacer: "1. Atacar" o "2. Sigilo".
Si elige "1": Pide una tirada de d20. Si es >= GOBLIN_DC, el Trasgo es derrotado. 
Si no, el Trasgo contraataca.
Si elige "2": Pide una tirada de d20. Si es >= 15 (es más difícil esconderse), 
el héroe pasa sin ser visto. Si no, lo descubren.
Si elige cualquier otra cosa: Imprime "Te quedas paralizado por el miedo".
Usa f-strings para que cada mensaje incluya el nombre del héroe.
"""

print("*** El Simulador de Encuentros ***\n")

GOBLIN_DC = 12

name = input("¿Cuál es tu nombre aventurero? ")

print("\n¿Qué prefieres?")
print("1. Atacar")
print("2. Sigilo")
answer = int(input("> "))

if answer == 1:
    rolled_dice = int(input("Resultado de un d20: "))
    if rolled_dice >= GOBLIN_DC:
        print(f"El Trasgo derrotado por {name}")
    else:
        print(f"El Trasgo contraataca a {name}")
elif answer == 2:
    rolled_dice = int(input("Resultado de un d20: "))
    if rolled_dice >= 15:
        print(f"{name} pasa sin ser visto")
    else:
        print(f"{name} es descubierto")
else:
    print(f"{name} se queda paralizado por el miedo")