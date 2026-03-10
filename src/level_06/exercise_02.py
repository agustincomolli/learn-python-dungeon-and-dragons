"""
EJERCICIO 2: La Resistencia del Enano - ⭐
📝 Descripción: Un personaje sobrevive a un veneno si su 
constitution es mayor a 15 O si tiene una poción_antídoto 
(pídelo como "si/no"). 
Usa or para mostrar si el personaje sobrevive.
"""

print("*** La Resistencia del Enano ***\n")

constitution = int(input("Constitución: "))
antidote_potion = input("¿Tienes el antídoto? [si/no]")

if constitution > 15 or antidote_potion == "si":
    print("Sobrevives al envenenamiento")
else:
    print("El venenoo invade todo tu cuerpo y mueres")