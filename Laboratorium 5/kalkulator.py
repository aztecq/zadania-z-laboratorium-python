# Zadanie 6 – Pierwszy test (assert i konwencje)
def dodaj(a: int, b: int) -> int:
    return a + b



# Zadanie 7 - Testowanie Wyjątków (pytest.raises)
def dziel(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Nie można dzielić przez zero!")
    return a / b
