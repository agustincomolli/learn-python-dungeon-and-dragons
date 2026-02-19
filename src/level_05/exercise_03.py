"""
EJERCICIO 3: El Guardián del Enigma - ⭐⭐
📝 Descripción: Crea una variable enigma_answer = "fuego". 
Pide al usuario que intente adivinar la respuesta. Si acierta, 
imprime "La puerta se abre". 
Si no, imprime "El guardián te lanza un hechizo de sueño".
"""

print("*** El Guardián del Enigma ***\n")
enigma_answer = "fuego"
answer = input("Adivina la respuesta: ")
if answer == enigma_answer:
    print("La puerta se abre")
else:
    print("El guardián te lanza un hechizo de sueño")