name = input("Nombre del héroe: ")
health = int(input("Puntos de vida: "))

while health > 0:
    print(name, "pelea")
    health = health - 1

print("Fin del combate")