"""
EJERCICIO 5: El Libro de Conjuros de Aelan - ⭐⭐⭐
📝 Descripción: Crea un archivo src/level_08/spellbook.py.
Vas a programar tres funciones esenciales para tu aventura:
show_stats(name, hp): Imprime una mini-ficha con el nombre y la vida.
calculate_spell_dc(intelligence): Recibe la inteligencia, calcula el modificador y 
retorna el Spell Save DC (8 + 2 + mod).
take_damage(current_hp, damage): Recibe la vida actual y el daño recibido, 
resta el daño y retorna la nueva vida.

En el programa principal:
Pide al usuario su nombre y su inteligencia.
Usa la función para calcular su DC y muéstralo.
Define que tiene 15 de vida inicial.
Simula un ataque: resta 5 de vida usando la función take_damage.
Muestra el estado final con show_stats.
"""

print("*** El Libro de Conjuros de Aelan ***\n")

def fill_blanks(total_lenght, initial_space, title, value):
    """Devuelve una cantidad de espacios en blanco para encolumnar un valor"""
    total_blank = total_lenght - (initial_space + len(title + str(value)))
    return " " * total_blank


def show_stats(name, hp):
    """Imprime una mini-ficha con el nombre y la vida"""
    name_blank = 46 - len(f"    Nombre: {name}")
    hp_blank = 46 - len(f"    Vida  : {hp}")
    print("+----------------------------------------------+")
    print("+              FICHA DEL PERSONAJE             +")
    print("+                                              +")
    print(f"+    Nombre: {name}" + fill_blanks(46,4, "Nombre: ", name) + "+")
    print(f"+    Vida  : {hp}"   + fill_blanks(46,4, "Vida  : ", hp) + "+")
    print("+                                              +")
    print("+----------------------------------------------+")


def calculate_spell_dc(intelligence):
    """Recibe la inteligencia, calcula el modificador y retorna el Spell Save DC"""
    modifier = (intelligence - 10) // 2
    return 8 + 2 + modifier


def take_damage(current_hp, damage):
    """Recibe la vida actual y el daño recibido, resta el daño y retorna la nueva vida"""
    return current_hp - damage


name = input("Nombre: ")
intelligence = int(input("Inteligencia: "))
hp = 15
print(f"Clase de Dificultad de Hechizo: {calculate_spell_dc(intelligence)}")
hp = take_damage(hp, 5)
show_stats(name, hp)