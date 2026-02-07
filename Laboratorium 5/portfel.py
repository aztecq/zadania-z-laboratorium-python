# Zadanie 9 - Dodawanie adnotacji typów (type hints)
class Portfel:
    def __init__(self, saldo: int = 0) -> None:
        self._saldo: int = saldo

    @property
    def saldo(self) -> int:
        return self._saldo
        
    def wplac(self, kwota: int) -> None:
        self._saldo += kwota