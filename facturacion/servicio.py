from decimal import Decimal
from typing import Callable

from facturacion.descuentos import EstrategiaDescuento
from facturacion.impuestos import Impuesto
from facturacion.interfaces import Notificador, RepositorioFacturas
from facturacion.modelos import Factura


class ServicioFacturacion:
    """Orquesta la emision de una factura. Depende de abstracciones (DIP)."""

    def __init__(
        self,
        repositorio: RepositorioFacturas,
        notificador: Notificador,
        impuesto: Impuesto,
        selector_descuento: Callable[[str], EstrategiaDescuento],
    ) -> None:
        self._repositorio = repositorio
        self._notificador = notificador
        self._impuesto = impuesto
        self._selector_descuento = selector_descuento

    def emitir(self, factura: Factura) -> Decimal:
        descuento = self._selector_descuento(factura.tipo_cliente)
        base = descuento.aplicar(factura.subtotal())
        total = base + self._impuesto.calcular(base)
        self._repositorio.guardar(factura, total)
        mensaje = f"Factura {factura.numero} por {total}"
        self._notificador.enviar(factura.cliente_id, mensaje)
        return total
