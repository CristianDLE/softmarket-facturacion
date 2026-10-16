from dataclasses import dataclass, field
from decimal import Decimal


@dataclass(frozen=True)
class ItemFactura:
    descripcion: str
    precio: Decimal
    cantidad: int

    def __post_init__(self) -> None:
        if self.cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")

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
