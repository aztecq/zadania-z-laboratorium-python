# Zadanie 8 - Izolowanie testów: Wprowadzenie do Mockowania
from kursy_walut import pobierz_cene_euro

def test_pobierania_ceny_euro_w_izolacji(mocker):
    fake_json = {"rates": [{"mid": 4.321}]}

    mocker.patch(
        "requests.get",
        return_value=mocker.Mock(json=lambda: fake_json)
    )

    cena = pobierz_cene_euro()
    assert cena == 4.321
