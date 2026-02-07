# Ćwiczenie 11: Tworzymy własny pakiet
import time

def mierz_czas(funkcja):
    def wrapper(*args, **kwargs):
        start = time.time()
        wynik = funkcja(*args, **kwargs)
        koniec = time.time()
        print("Czas wykonania:", koniec - start, "sek.")
        return wynik
    return wrapper