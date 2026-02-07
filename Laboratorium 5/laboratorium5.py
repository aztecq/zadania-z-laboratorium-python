# Zadanie 1: Generatory jako Korutyny (Dwukierunkowa Komunikacja)
from functools import wraps

def korutyna(func):
"""Dekorator, który automatycznie "uruchamia" korutynę."""
@wraps(func)
def primer(*args, **kwargs):
    gen = func(*args, **kwargs)
    next(gen)
    return gen
return primer

@korutyna
def srednia_kroczaca():
"""Korutyna obliczająca średnią kroczącą."""
suma = 0.0
licznik = 0
while True:
    nowa_liczba = yield
    suma += nowa_liczba
    licznik += 1
    print(f"Otrzymano: {nowa_liczba}, nowa średnia: {suma / licznik:.2f}")

kalkulator = srednia_kroczaca() 

kalkulator.send(10)
kalkulator.send(20)
kalkulator.send(5)



# Zadanie 2 - Pełna Kontrola - Obsługa Błędów (.throw())
class ResetKorutyny(Exception):
    pass

from functools import wraps

def korutyna(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer

@korutyna
def srednia_kroczaca_z_resetem():
    suma = 0.0
    licznik = 0
    while True:
        try:
            nowa_liczba = yield
            suma += nowa_liczba
            licznik += 1
            print(f"Otrzymano: {nowa_liczba}, nowa średnia: {suma / licznik:.2f}")
        except ResetKorutyny:
            print("--- RESETOWANIE KORUTYNY ---")
            suma = 0.0
            licznik = 0

k = srednia_kroczaca_z_resetem()
k.send(10)
k.send(20)
k.throw(ResetKorutyny)
k.send(5)



# Zadanie 3 - Procesor Poleceń
from functools import wraps

def korutyna(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer

class ResetProcesora(Exception):
    pass

@korutyna
def procesor_polecen():
    print("--- Procesor poleceń gotowy. ---")
    dane = []
    while True:
        try:
            polecenie = yield

            czesci = polecenie.strip().split(":", 1)
            akcja = czesci[0].upper()
            wartosc = czesci[1] if len(czesci) > 1 else None

            if akcja == "DODAJ":
                dane.append(wartosc)
                print(f"DODANO: '{wartosc}'")
            elif akcja == "USUN":
                if wartosc in dane:
                    dane.remove(wartosc)
                    print(f"USUNIĘTO: '{wartosc}'")
                else:
                    print(f"BŁĄD: Nie można usunąć, brak '{wartosc}'")
            elif akcja == "POKAZ":
                print("AKTUALNE DANE:", dane)
            else:
                print(f"BŁĄD: Nieznana akcja '{akcja}'")

        except ResetProcesora:
            print("--- RESETOWANIE PROCESORA ---")
            dane = []
        except Exception as e:
            print("Wystąpił błąd:", e)

p = procesor_polecen()
p.send("DODAJ:jabłko")
p.send("DODAJ:banan")
p.send("POKAZ")
p.send("USUN:gruszka")
p.send("USUN:jabłko")
p.send("POKAZ")
p.throw(ResetProcesora)
p.send("POKAZ")



# Zadanie 4 - Budowa Własnych Iteratorów (Protokół Iteratora)
class Odliczanie:
    def __init__(self, start: int):
        self.start = start

    def __iter__(self):
        liczba = self.start
        while liczba > 0:
            yield liczba
            liczba -= 1
        yield "START!"

odliczanie_do_startu = Odliczanie(5)
for krok in odliczanie_do_startu:
    print(krok)



# Zadanie 5 - Pułapka Iteratora: Obiekt Jednorazowego Użytku
class LicznikJednorazowy:
    def __init__(self, max_val):
        self.max = max_val
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            wynik = self.n
            self.n += 1
            return wynik
        raise StopIteration

licznik = LicznikJednorazowy(3)

print("Pierwsza próba iteracji:")
for x in licznik:
    print(x)

print("\nDruga próba iteracji (na tym samym obiekcie):")
for x in licznik:
    print(x)