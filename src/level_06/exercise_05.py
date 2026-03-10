"""
EJERCICIO 5: La Prueba de los Tres Desafíos - ⭐⭐⭐
📝 Descripción: Crea un archivo src/level_06/saving_throw.py.
Un mago oscuro lanza un hechizo sobre el héroe. 
Para salvarse, el héroe debe cumplir una de estas tres condiciones épicas:
Tener una intelligence de 18 o más.
O Tener un luck_point (puntos de suerte) y que su tirada de d20 sea mayor a 10. 
(Usa and para esta parte).
O Ser de la raza "Elfo" y que el hechizo no sea de tipo "Sueño".
Instrucciones: Pide al usuario todos los datos necesarios y usa una combinación de and, 
or y paréntesis para evaluar la salvación final.
Pista: if condition1 or (condition2 and condition3) or condition4:
"""

print("*** La Prueba de los Tres Desafíos ***\n")

race = input("Raza: ")
intelligence = int(input("Inteligencia: "))
luck = int(input("Suerte: "))
roll_d20 = int(input("Tirada d20: "))
spell = input("Hechizo: ")

if intelligence >= 18 or (luck > 0 and roll_d20 > 10) or (race == "Elfo" and not spell == "Sueño"):
    print("\n¡Te salvaste!")
else:
    print("\nNo has pasado la prueba de salvación")