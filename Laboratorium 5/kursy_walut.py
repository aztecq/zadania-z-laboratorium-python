# Zadanie 8 - Izolowanie testów: Wprowadzenie do Mockowania
import requests

def pobierz_cene_euro() -> float:
    response = requests.get("http://api.nbp.pl/api/exchangerates/rates/a/eur/")
    dane = response.json()
    return dane["rates"][0]["mid"]
