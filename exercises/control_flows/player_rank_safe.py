try:
    age = int(input("Ingrese su edad: "))
    if age <= 0:
        print("Edad inválida")
    if age < 13:
        print("Eres un aprendiz")
    elif age >= 18:
        print("Eres un aventurero experimentado")
    else:
        print("Eres un aventurero joven")
except:
    print("ERROR: Debe ingresar un número")
