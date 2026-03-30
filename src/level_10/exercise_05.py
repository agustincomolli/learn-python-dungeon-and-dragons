"""
EJERCICIO 5: El Umbral de la Muerte - ⭐⭐⭐
📝 Descripción: Crea un archivo src/level_10/death_saves.py.
Este es el ejercicio más complejo hasta ahora. 
Vas a simular las Tiradas de Salvación contra Muerte de D&D.
1. Crea dos variables: successes = 0 y failures = 0.
2. Crea un bucle while que se ejecute mientras successes < 3 y failures < 3.
3. Dentro del bucle:
    Pide al usuario el resultado de una tirada de d20.
    Si es 10 o más: suma 1 a successes.
    Si es menor a 10: suma 1 a failures.
    Imprime cuántos éxitos y fallos llevas.
4. Al salir del bucle, usa un if para determinar el destino final:
    Si successes == 3, imprime "❤️ ¡Te has estabilizado!".
    De lo contrario, imprime "💀 El héroe ha caído en la oscuridad...".
"""