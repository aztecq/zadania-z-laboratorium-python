# Ćwiczenie 9 - Tworzenie modułu "narzedzia"
import time

def mierz_czas(funkcja):
    def wrapper(*args, **kwargs):
        start = time.time()
        wynik = funkcja(*args, **kwargs)
        koniec = time.time()
        print("Czas wykonania:", koniec - start, "sek.")
        return wynik
    return wrapper



# Ćwiczenie 10 - Zastosowanie if __name__ == "__main__"
if __name__ == "__main__":
    @mierz_czas
    def test():
        time.sleep(1)

    test()