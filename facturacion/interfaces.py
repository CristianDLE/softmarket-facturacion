from abc import ABC, abstractmethod
from decimal import Decimal

from facturacion.modelos import Factura


class RepositorioFacturas(ABC):
    """Contrato pequeno: solo persistencia (ISP)."""

    @abstractmethod
    def guardar(self, factura: Factura, total: Decimal) -> None: ...


class Notificador(ABC):
    """Contrato pequeno: solo notificar (correo, WhatsApp, SMS...)."""

    @abstractmethod
    def enviar(self, destinatario: str, mensaje: str) -> None: ...
