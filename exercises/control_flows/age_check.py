character_name = input("Ingrese su nombre: ")
character_age = int(input("Ingrese su edad: "))

if character_age >= 18:
    print("Bienvenido", character_name)
    print("¡Estas listo para la aventura!")
else:
    print("Todavía no tenés la edad suficiente")