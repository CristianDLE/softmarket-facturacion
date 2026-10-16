from dataclasses import dataclass, field
from decimal import Decimal


@dataclass(frozen=True)
class ItemFactura:
    descripcion: str
    precio: Decimal
    cantidad: int

    def subtotal(self) -> Decimal:
        return self.precio * self.cantidad


@dataclass
class Factura:
    numero: str
    cliente_id: str
    tipo_cliente: str
    items: list = field(default_factory=list)

    def subtotal(self) -> Decimal:
        return sum((i.subtotal() for i in self.items), Decimal("0"))
