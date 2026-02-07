# Ćwiczenie 1: Pierwszy dialog
imie = input("Podaj swoje imię: ")
print(f"Witaj, {imie}!")

kolor = input("Jaki jest Twój ulubiony kolor? ")
print(f"{kolor} to fajny kolor")



# Ćwiczenie 2: Implementacja instrukcji if
wiek = int(input("Podaj swój wiek: "))

if wiek >= 18:
    print("Jesteś pełnoletni/a – możesz korzystać ze specjalnej oferty!")

print("Dziękuję za skorzystanie z usługi.")



# Ćwiczenie 3: Implementacja wielu ścieżek (if-elif-else)
wiek = int(input("Podaj swój wiek: "))

if wiek < 13:
    print("Kategoria: dziecko")
elif wiek <= 17:
    print("Kategoria: nastolatek")
elif wiek <= 64:
    print("Kategoria: dorosły")
else:
    print("Kategoria: senior")



# Zadanie 1: Wystawianie Oceny
punkty = int(input("Podaj liczbę punktów (0-100): "))

if 0 <= punkty <= 50:
    print("Ocena: 2.0")
elif 51 <= punkty <= 60:
    print("Ocena: 3.0")
elif 61 <= punkty <= 70:
    print("Ocena: 3.5")
elif 71 <= punkty <= 80:
    print("Ocena: 4.0")
elif 81 <= punkty <= 90:
    print("Ocena: 4.5")
elif 91 <= punkty <= 100:
    print("Ocena: 5.0")



# and, or, not
is_admin = False
is_group_member = True
is_locked = True
if (is_admin or is_group_member) and is_locked:
    print("Dostęp przyznany.")
else:
    print("Brak dostępu do zasobu")



# Ćwiczenie 4: Implementacja pętli "while"
kwota_poczatkowa = 1000
cel = 2000
roczne_oprocentowanie = 0.05

kwota = kwota_poczatkowa
lata = 0

while kwota < cel:
    kwota = kwota + kwota * roczne_oprocentowanie
    lata = lata + 1

print("Liczba lat:", lata)
print("Końcowa kwota:", kwota)



# Ćwiczenie 5: Interaktywna pętla
while True:
    tekst = input("Napisz coś: ")
    if tekst == "koniec":
        break
    print(tekst)



# Ćwiczenie 6: Pierwsza pętla "for"
slowo = input("Podaj słowo: ").lower()
licznik_samoglosek = 0

for litera in slowo:
    if litera in "aeiouy":
        licznik_samoglosek = licznik_samoglosek + 1

print("Liczba samogłosek:", licznik_samoglosek)



# Ćwiczenie 7: Proste powtórzenia
for i in range(1, 6):
    print("To jest powtórzenie numer:", i)



# Zadanie 2: FizzBuzz
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)



# Ćwiczenie 8 – Implementacja listy zakupów
lista = []

while True:
    produkt = input("Podaj produkt (lub 'koniec'): ")
    if produkt == "koniec":
        break
    lista.append(produkt)

print("Twoja lista zakupów:", lista)



# Zadanie 3 – Analizator tagów
wejscie = input("Podaj tagi oddzielone przecinkami: ")

tagi = wejscie.split(",")
czyste_tagi = []

for t in tagi:
    czyste_tagi.append(t.strip())

unikalne = set(czyste_tagi)

print("Liczba wszystkich podanych tagów:", len(czyste_tagi))
print("Liczba unikalnych tagów:", len(unikalne))

print("Unikalne tagi (alfabetycznie):")
for t in sorted(unikalne):
    print("-", t)



# Zadanie 4: Dynamiczna książka kontaktowa
kontakty = {}

while True:
    print("\n")
    print("1. Dodaj kontakt")
    print("2. Wyświetl kontakt")
    print("3. Usuń kontakt")
    print("4. Wyświetl wszystko")
    print("5. Zakończ")

    wybor = input("Wybierz opcję: ")

    if wybor == "1":
        nazwa = input("Podaj nazwę: ")
        numer = input("Podaj numer: ")
        kontakty[nazwa] = numer

    elif wybor == "2":
        nazwa = input("Podaj nazwę: ")
        if nazwa in kontakty:
            print("Numer:", kontakty[nazwa])
        else:
            print("Brak takiego kontaktu.")

    elif wybor == "3":
        nazwa = input("Podaj nazwę: ")
        if nazwa in kontakty:
            del kontakty[nazwa]
            print("Usunięto.")
        else:
            print("Brak takiego kontaktu.")

    elif wybor == "4":
        print(kontakty)

    elif wybor == "5":
        break



# Zadanie 5: Baza Danych Pracowników
baza_danych = [
    {"imie": "Anna", "stanowisko": "Specjalista", "pensja": 4500},
    {"imie": "Piotr", "stanowisko": "Manager", "pensja": 8000},
    {"imie": "Zofia", "stanowisko": "Specjalista", "pensja": 5200},
    {"imie": "Krzysztof", "stanowisko": "Stażysta", "pensja": 2500}
]

suma = 0
for p in baza_danych:
    suma = suma + p["pensja"]
srednia = suma / len(baza_danych)
print("Średnia pensja:", srednia)

max_pracownik = baza_danych[0]
for p in baza_danych:
    if p["pensja"] > max_pracownik["pensja"]:
        max_pracownik = p
print("Najwięcej zarabia:", max_pracownik)

print('Specjaliści:')
for p in baza_danych:
    if p["stanowisko"] == "Specjalista":
        print("-", p["imie"])
