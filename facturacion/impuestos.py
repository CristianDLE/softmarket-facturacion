from abc import ABC, abstractmethod
from decimal import Decimal


class Impuesto(ABC):
    @abstractmethod
    def calcular(self, base: Decimal) -> Decimal: ...


class IVA(Impuesto):
    def __init__(self, tasa: Decimal = Decimal("0.19")) -> None:
        self._tasa = tasa

    def calcular(self, base: Decimal) -> Decimal:
        return base * self._tasa
