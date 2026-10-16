from abc import ABC, abstractmethod
from decimal import Decimal


class EstrategiaDescuento(ABC):
    """Contrato: recibe un subtotal y devuelve el subtotal con descuento."""

    @abstractmethod
    def aplicar(self, subtotal: Decimal) -> Decimal: ...


class SinDescuento(EstrategiaDescuento):
    def aplicar(self, subtotal: Decimal) -> Decimal:
        return subtotal


class DescuentoVip(EstrategiaDescuento):
    def aplicar(self, subtotal: Decimal) -> Decimal:
        return subtotal * Decimal("0.90")


class DescuentoMayorista(EstrategiaDescuento):
    def aplicar(self, subtotal: Decimal) -> Decimal:
        return subtotal * Decimal("0.85")


_DESCUENTOS = {"VIP": DescuentoVip(), "MAYORISTA": DescuentoMayorista()}


def descuento_para(tipo_cliente: str) -> EstrategiaDescuento:
    """Agregar un nuevo tipo de cliente = agregar una clase (no tocar las demas)."""
    return _DESCUENTOS.get(tipo_cliente, SinDescuento())
