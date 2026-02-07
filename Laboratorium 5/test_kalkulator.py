# Zadanie 6 – Pierwszy test (assert i konwencje)
from kalkulator import dodaj

def test_dodawania_liczb_dodatnich():
    assert dodaj(2, 3) == 5

def test_dodawania_liczb_ujemnych():
    assert dodaj(-1, -1) == -2



# Zadanie 7 - Testowanie Wyjątków (pytest.raises)
import pytest
from kalkulator import dziel

def test_poprawnego_dzielenia():
    assert dziel(10, 2) == 5

def test_dzielenia_przez_zero_powinno_rzucic_blad():
    with pytest.raises(ValueError):
        dziel(10, 0)
