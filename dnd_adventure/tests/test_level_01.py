# tests/test_nivel_1.py
def test_identidad():
    nombre = "Bárbaro"
    fuerza = 18
    assert type(nombre) == str, "El nombre debe ser un texto (String)"
    assert type(fuerza) == int, "La fuerza debe ser un número entero (Integer)"
    print("✅ ¡Los dioses confirman tu identidad!")

if __name__ == "__main__":
    test_identidad()