character_name = input("Ingresa tu nombre aventurero: ")

try:
    character_age = int(input("Ingresa tu edad: "))
    
    if character_age <= 0:
        print("Edad inválida, tiene que ser mayor a 0.")
    elif character_age < 13:
        print(character_name, "eres un aprendiz de aventurero.")
    elif character_age >= 18:
        print(character_name, "eres un aventurero experimentado.")
    else:
        print(character_name, "eres un joven aventurero.")
except:
    print("ERROR: Debes ingresar un número.")