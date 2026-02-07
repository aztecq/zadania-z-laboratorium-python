# Ćwiczenie 1 - Listy Składane (List Comprehensions)
pracownicy = [
    {"imie": "Anna", "stanowisko": "Specjalista", "pensja": 4500},
    {"imie": "Piotr", "stanowisko": "Manager", "pensja": 8000},
    {"imie": "Zofia", "stanowisko": "Specjalista", "pensja": 5200},
]

lista_plac = [p["pensja"] for p in pracownicy if p["stanowisko"] == "Specjalista"]

print(f"Lista płac dla specjalistów: {lista_plac}")



# Ćwiczenie 2 - Rekurencja w Słownikach: "Głębokie Wyszukiwanie"
def znajdz_wartosc(dane, szukany_klucz):
    for klucz, wartosc in dane.items():
        if klucz == szukany_klucz:
            return wartosc
        if isinstance(wartosc, dict):
            wynik = znajdz_wartosc(wartosc, szukany_klucz)
            if wynik is not None:
                return wynik
    return None

konfiguracja = {
    "uzytkownik": "admin",
    "baza_danych": {
        "host": "localhost",
        "port": 5432,
        "credentials": {
            "user": "db_user",
            "password": "secret_password"
        }
    }
}

haslo = znajdz_wartosc(konfiguracja, "password")
print(f"Znalezione hasło: {haslo}")



# Zadanie 1: Od słownika do obiektu
class Gracz:
    def __init__(self, imie, hp):
        self.imie = imie
        self.hp = hp

gracz_obj = Gracz("Aragorn", 100)
print(gracz_obj.imie)
print(gracz_obj.hp)



# Zadanie 2 - Obiekty, które "mówią" i "działają"
class Gracz:
    def __init__(self, imie, hp):
        self.imie = imie
        self.hp = hp

    def pokaz_status(self):
        print(f"Gracz: {self.imie}, HP: {self.hp}")

    def otrzymaj_obrazenia(self, ilosc):
        self.hp = self.hp - ilosc
        print(f"{self.imie} otrzymał obrażenia: {ilosc}")

    def __str__(self):
        return f"Gracz {self.imie} (HP: {self.hp})"

    def __repr__(self):
        return f"Gracz(imie='{self.imie}', hp={self.hp})"

g = Gracz("Aragorn", 100)
print(g)
g.pokaz_status()
g.otrzymaj_obrazenia(15)
print(g)



# Zadanie 3 - Właściwości wspólne i indywidualne (atrybuty klasy)
class Gracz:
    liczba_graczy = 0

    def __init__(self, imie, hp):
        self.imie = imie
        self.hp = hp
        Gracz.liczba_graczy += 1

print(Gracz.liczba_graczy)
g1 = Gracz("Pierwszy", 100)
g2 = Gracz("Drugi", 90)
g3 = Gracz("Trzeci", 80)
print(Gracz.liczba_graczy)



# Zadanie 4: Hierarchia i specjalizacja (Dziedziczenie)
class Gracz:
    def __init__(self, imie, hp):
        self.imie = imie
        self.hp = hp

    def __str__(self):
        return f"Gracz {self.imie} (HP: {self.hp})"

    def przedstaw_sie(self):
        print(str(self))

class Wojownik(Gracz):
    def __init__(self, imie, hp, sila):
        super().__init__(imie, hp)
        self.sila = sila

    def __str__(self):
        return super().__str__() + f", Siła: {self.sila}"

    def atak(self):
        print(f"{self.imie} atakuje z siłą {self.sila}!")

w = Wojownik("Boromir", 120, 30)
w.przedstaw_sie()
w.atak()



# Zadanie 5 - Polimorfizm w akcji
class Gracz:
    def __init__(self, imie, hp):
        self.imie = imie
        self.hp = hp

    def przedstaw_sie(self):
        print(f"Jestem {self.imie}, mam HP: {self.hp}")

class Wojownik(Gracz):
    def __init__(self, imie, hp, sila):
        super().__init__(imie, hp)
        self.sila = sila

    def przedstaw_sie(self):
        print(f"Jestem wojownik {self.imie}, HP: {self.hp}, Siła: {self.sila}")

class Mag(Gracz):
    def __init__(self, imie, hp, mana):
        super().__init__(imie, hp)
        self.mana = mana

    def przedstaw_sie(self):
        print(f"Jestem mag {self.imie}, HP: {self.hp}, Mana: {self.mana}")

druzyna = [
    Gracz("Aragorn", 100),
    Wojownik("Boromir", 120, 30),
    Mag("Gandalf", 80, 200),
]

for postac in druzyna:
    postac.przedstaw_sie()



# Zadanie 6 - Enkapsulacja w praktyce (@property)
class Gracz:
    def __init__(self, imie, hp):
        self.imie = imie
        self._hp = hp

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, nowa_wartosc):
        if nowa_wartosc < 0:
            self._hp = 0
        else:
            self._hp = nowa_wartosc

g = Gracz("Aragorn", 100)
g.hp = -50
print(g.hp)



# Zadanie 7 - Kompozycja (Relacja "ma")
class Ekwipunek:
    def __init__(self):
        self.przedmioty = []

    def dodaj_przedmiot(self, przedmiot):
        self.przedmioty.append(przedmiot)

    def pokaz_przedmioty(self):
        print("Ekwipunek:", self.przedmioty)

class Gracz:
    def __init__(self, imie, hp):
        self.imie = imie
        self.hp = hp
        self.ekwipunek = Ekwipunek()

g = Gracz("Aragorn", 100)
g.ekwipunek.dodaj_przedmiot("Miecz")
g.ekwipunek.dodaj_przedmiot("Tarcza")
g.ekwipunek.pokaz_przedmioty()



# Zadanie 8: Metody Klasy i Statyczne
class Gracz:
    def __init__(self, imie, hp):
        self.imie = imie
        self.hp = hp

    @staticmethod
    def sprawdz_poprawnosc_imienia(imie):
        return (imie != "") and (imie[0].isupper())

    def przedstaw_sie(self):
        print(f"{self.imie} (HP: {self.hp})")

class Wojownik(Gracz):
    def __init__(self, imie, hp, sila):
        super().__init__(imie, hp)
        self.sila = sila

    @classmethod
    def stworz_berserkera(cls, imie):
        return cls(imie, 80, 40)

    def przedstaw_sie(self):
        print(f"{self.imie} (HP: {self.hp}, Siła: {self.sila})")

berserker = Wojownik.stworz_berserkera("Olaf")
berserker.przedstaw_sie()

print(Gracz.sprawdz_poprawnosc_imienia("Aragorn"))
print(Gracz.sprawdz_poprawnosc_imienia("aragorn"))



# Zadanie 9: Porównywanie i Dodawanie Obiektów
class Gracz:
    def __init__(self, imie, hp):
        self.imie = imie
        self.hp = hp

    def __eq__(self, other):
        if isinstance(other, Gracz):
            return self.imie == other.imie
        return False

class Wojownik(Gracz):
    def __init__(self, imie, hp, sila):
        super().__init__(imie, hp)
        self.sila = sila

    def __add__(self, other):
        if isinstance(other, Wojownik):
            nowe_imie = self.imie + " i " + other.imie
            nowe_hp = self.hp + other.hp
            nowa_sila = self.sila + other.sila
            return Wojownik(nowe_imie, nowe_hp, nowa_sila)
        return NotImplemented

    def przedstaw_sie(self):
        print(f"{self.imie} (HP: {self.hp}, Siła: {self.sila})")

g1 = Gracz("Aragorn", 100)
g2 = Gracz("Aragorn", 50)
print(g1 == g2)

w1 = Wojownik("Aragorn", 100, 30)
w2 = Wojownik("Boromir", 120, 25)
fuzja = w1 + w2
fuzja.przedstaw_sie()



# Zadanie 10: dataclasses – Mniej kodu, więcej danych
from dataclasses import dataclass

@dataclass
class PunktData:
    x: int
    y: int

p1 = PunktData(10, 20)
print(p1)

p2 = PunktData(10, 20)
print(p1 == p2)



# Zadanie 11: Własne Iteratory
class IteratorEkwipunku:
    def __init__(self, przedmioty):
        self.przedmioty = przedmioty
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= len(self.przedmioty):
            raise StopIteration
        element = self.przedmioty[self.i]
        self.i += 1
        return element

class Ekwipunek:
    def __init__(self):
        self.przedmioty = []

    def dodaj_przedmiot(self, przedmiot):
        self.przedmioty.append(przedmiot)

    def __iter__(self):
        return IteratorEkwipunku(self.przedmioty)

plecak = Ekwipunek()
plecak.dodaj_przedmiot("Miecz")
plecak.dodaj_przedmiot("Tarcza")
plecak.dodaj_przedmiot("Mikstura")

for p in plecak:
    print(p)

it = iter(plecak)
print(next(it))
print(next(it))
