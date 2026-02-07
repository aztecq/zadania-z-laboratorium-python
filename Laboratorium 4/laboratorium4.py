# Zadanie 1 - Podstawy Operacji na Plikach
plik = open("dziennik.txt", "w", encoding="utf-8")
plik.write("Pierwszy wpis.\n")
plik.write("Wszystko działa.\n")
plik.close()

plik = open("dziennik.txt", "r", encoding="utf-8")
zawartosc = plik.read()
print(zawartosc)
plik.close()

plik = open("dziennik.txt", "a", encoding="utf-8")
plik.write("Dodaję kolejną linię.\n")
plik.close()

plik = open("dziennik.txt", "r", encoding="utf-8")
print(plik.read())
plik.close()



# Zadanie 2 - Obsługa Wyjątków (try...except)
def oblicz_rok_urodzenia(sciezka_pliku):
    try:
        plik = open(sciezka_pliku, "r", encoding="utf-8")
        tekst = plik.read()
        plik.close()

        wiek = int(tekst)
        aktualny_rok = 2026
        rok = aktualny_rok - wiek
        print("Przybliżony rok urodzenia:", rok)

    except FileNotFoundError:
        print("BŁĄD: Nie znaleziono pliku!")
    except ValueError:
        print("BŁĄD: Zawartość pliku nie jest poprawną liczbą!")

oblicz_rok_urodzenia("wiek.txt")
oblicz_rok_urodzenia("nie_ma_takiego_pliku.txt")



# Zadanie 3 - Menedżery Kontekstu (with)
with open("dziennik_with.txt", "w", encoding="utf-8") as plik:
    plik.write("Pierwszy wpis.\n")
    plik.write("Wszystko działa.\n")

with open("dziennik_with.txt", "a", encoding="utf-8") as plik:
    plik.write("Dodaję kolejną linię.\n")

with open("dziennik_with.txt", "r", encoding="utf-8") as plik:
    print(plik.read())



# Zadanie 4 - Rzucanie Własnych Wyjątków (raise)
class NiepoprawnaIloscProduktuError(ValueError):
    pass

def dodaj_do_koszyka(produkt, ilosc):
    if ilosc <= 0:
        raise NiepoprawnaIloscProduktuError("Ilość produktów musi być dodatnia!")
    print("Dodano do koszyka:", produkt, "x", ilosc)

dodaj_do_koszyka("Chleb", 2)

try:
    dodaj_do_koszyka("Mleko", -3)
except NiepoprawnaIloscProduktuError as e:
    print("Błąd:", e)



# Zadanie 5 - Praktyczny Parser Logów
def zlicz_bledy(sciezka_pliku):
    try:
        ile = 0
        with open(sciezka_pliku, "r", encoding="utf-8") as plik:
            for linia in plik:
                linia = linia.strip()
                try:
                    poziom, wiadomosc = linia.split(":", 1)
                    if poziom == "ERROR":
                        ile += 1
                except ValueError:
                    pass
        return ile
    except FileNotFoundError:
        return 0

print("Liczba błędów:", zlicz_bledy("log.txt"))



# Zadanie 6 - Serializacja Obiektów (pickle)
import pickle

class StanGry:
    def __init__(self, nazwa_gracza, punkty, ekwipunek):
        self.nazwa_gracza = nazwa_gracza
        self.punkty = punkty
        self.ekwipunek = ekwipunek

    def __repr__(self):
        return f"StanGry(nazwa_gracza='{self.nazwa_gracza}', punkty={self.punkty}, ekwipunek={self.ekwipunek})"

stan = StanGry("Aragorn", 120, ["Miecz", "Tarcza"])

with open("stan_gry.pkl", "wb") as f:
    pickle.dump(stan, f)

with open("stan_gry.pkl", "rb") as f:
    wczytany_stan = pickle.load(f)

print(wczytany_stan)
print(type(wczytany_stan))



# Zadanie 7: Czytanie Plików CSV (csv.DictReader)
import csv

def wczytaj_pracownikow(sciezka_pliku):
    wyniki = []
    try:
        with open(sciezka_pliku, "r", newline="", encoding="utf-8") as f:
            czytnik = csv.DictReader(f)
            for wiersz in czytnik:
                try:
                    wiersz["pensja"] = int(wiersz["pensja"])
                    wyniki.append(wiersz)
                except ValueError:
                    pass
        return wyniki
    except FileNotFoundError:
        return []

print(wczytaj_pracownikow("pracownicy.csv"))



# Zadanie 8 - Zapisywanie Plików CSV (csv.DictWriter)
import csv

def zapisz_raport_sprzedazy(sciezka_pliku, dane):
    if not dane:
        print("Brak danych do zapisu.")
        return

    pola = list(dane[0].keys())

    with open(sciezka_pliku, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=pola)
        writer.writeheader()
        writer.writerows(dane)

sprzedaz = [
    {"produkt": "Chleb", "sprzedana_ilosc": 10, "przychody": 45.0},
    {"produkt": "Mleko", "sprzedana_ilosc": 7, "przychody": 28.0},
]
zapisz_raport_sprzedazy("raport.csv", sprzedaz)



# Zadanie 9 - Czytanie i Parsowanie JSON (json.load)
import json

def wczytaj_konfiguracje(sciezka_pliku):
    try:
        with open(sciezka_pliku, "r", encoding="utf-8") as f:
            dane = json.load(f)
        return dane
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

konf = wczytaj_konfiguracje("konfiguracja.json")
if konf:
    print(konf["baza_danych"]["uzytkownik"])



# Zadanie 10 - Zapisywanie do JSON (json.dump)
import json

def zapisz_jako_json(dane, sciezka_pliku):
    try:
        with open(sciezka_pliku, "w", encoding="utf-8") as f:
            json.dump(dane, f, indent=4, ensure_ascii=False)
        print("Zapisano poprawnie.")
    except IOError:
        print("Błąd zapisu do pliku.")

moje_dane = {
    "id": 100,
    "uzytkownik": "żołądź",
    "ulubiony_kolor": "żółty",
}
zapisz_jako_json(moje_dane, "dane.json")



# Zadanie 11 - Walidacja Danych z Pydantic
import json
from pydantic import BaseModel, ValidationError

class SpecyfikacjaModel(BaseModel):
    procesor: str
    ram_gb: int

class ProduktModel(BaseModel):
    nazwa_produktu: str
    id_produktu: str
    cena: float
    dostepny: bool
    tagi: list[str]
    specyfikacja: SpecyfikacjaModel

def wczytaj_i_waliduj_produkt(sciezka_pliku):
    try:
        with open(sciezka_pliku, "r", encoding="utf-8") as f:
            dane = json.load(f)

        produkt = ProduktModel.parse_obj(dane)
        return produkt

    except FileNotFoundError:
        print("Błąd: nie znaleziono pliku.")
        return None
    except json.JSONDecodeError:
        print("Błąd: niepoprawny JSON.")
        return None
    except ValidationError as e:
        print("Błąd walidacji:", e)
        return None

produkt = wczytaj_i_waliduj_produkt("produkt.json")
if produkt:
    print(produkt.nazwa_produktu)
    print(produkt.specyfikacja.procesor)