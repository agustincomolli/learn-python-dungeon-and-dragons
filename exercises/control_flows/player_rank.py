character_age = int(input("Ingrese su edad: "))

if character_age < 13:
    print("Eres un aprendiz")
elif character_age >= 18:
    print("Eres un aventurero experimentado")
else:
    print("Eres un aventurero joven")