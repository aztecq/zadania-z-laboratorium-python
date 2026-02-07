# Ćwiczenie 1: "Elastyczny Asystent"
def przedstaw_sie(nazwa_uzytkownika):
    print(f"Cześć, jestem {nazwa_uzytkownika}. Miło mi Cię poznać.")

imie = input("Podaj swoje imię: ")
przedstaw_sie(imie)



# Ćwiczenie 2: Zwracanie Wielu Wartości
def rozdziel_imie_nazwisko(imie_i_nazwisko):
    czesci = imie_i_nazwisko.split()
    imie = czesci[0]
    nazwisko = czesci[1]
    return imie, nazwisko

tekst = input("Podaj imię i nazwisko: ")
imie, nazwisko = rozdziel_imie_nazwisko(tekst)

print("Imię:", imie)
print("Nazwisko:", nazwisko)



# Ćwiczenie 3: Argumenty Pozycyjne Dowolnej Długości (*args)
def zsumuj_wszystko(*liczby):
    return sum(liczby)

print(zsumuj_wszystko(1, 2, 3))
print(zsumuj_wszystko(5, 10, 15, 25, 50))



# Ćwiczenie 4: Argumenty Nazwane Dowolnej Długości (**kwargs)
def generuj_raport(**szczegoly):
    for klucz, wartosc in szczegoly.items():
        print(f"- {klucz}: {wartosc}")

generuj_raport(status="Aktywny", punkty=150)
generuj_raport(imie="Anna", kraj="Polska", wiek=30)



# Ćwiczenie 5: Rozpakowywanie Kolekcji przy Wywołaniu
def generuj_raport(imie, stanowisko, miasto):
    print("Imię:", imie)
    print("Stanowisko:", stanowisko)
    print("Miasto:", miasto)

dane_pracownika = {"imie": "Jan", "miasto": "Poznań", "stanowisko": "Inżynier"}
generuj_raport(**dane_pracownika)



# Ćwiczenie 6 - "Uniwersalny Dekorator Mierzący Czas"
import time

def mierz_czas(funkcja):
    def wrapper(*args, **kwargs):
        start = time.time()
        wynik = funkcja(*args, **kwargs)
        koniec = time.time()
        print("Czas wykonania:", koniec - start, "sek.")
        return wynik
    return wrapper

@mierz_czas
def dodaj(a, b):
    return a + b

@mierz_czas
def policz_do(n):
    s = 0
    for i in range(n):
        s += i
    return s

print("Wynik dodawania:", dodaj(10, 5))
print("Suma:", policz_do(1000000))



# Ćwiczenie 7 - Generatory i yield: Leniwe Przetwarzanie Danych
def licz_do_trzech():
    yield 1
    yield 2
    yield 3

gen = licz_do_trzech()

for x in gen:
    print(x)



# Ćwiczenie 8: Generator Liczb Fibonacciego
def fibonacci(limit):
    a = 0
    b = 1
    for _ in range(limit):
        yield a
        a, b = b, a + b

for x in fibonacci(10):
    print(x)



# Ćwiczenie 9 - Tworzenie modułu "narzedzia"
import time
import narzedzia

@narzedzia.mierz_czas
def wolna_funkcja():
    time.sleep(2)

wolna_funkcja()



# Ćwiczenie 11: Tworzymy własny pakiet
import time
from narzedzia_firmowe.pomiar import mierz_czas
from narzedzia_firmowe.formatowanie import na_wielkie

@mierz_czas
def wolna_funkcja():
    time.sleep(2)

print(na_wielkie("kotek"))
wolna_funkcja()

