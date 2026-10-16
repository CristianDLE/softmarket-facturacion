from decimal import Decimal

from facturacion.descuentos import descuento_para
from facturacion.impuestos import IVA
from facturacion.interfaces import Notificador, RepositorioFacturas
from facturacion.modelos import Factura, ItemFactura
from facturacion.servicio import ServicioFacturacion


class RepositorioFalso(RepositorioFacturas):
    def __init__(self):
        self.guardadas = []

    def guardar(self, factura, total):
        self.guardadas.append((factura.numero, total))


class NotificadorFalso(Notificador):
    def __init__(self):
        self.enviados = []

    def enviar(self, destinatario, mensaje):
        self.enviados.append((destinatario, mensaje))


def test_emitir_factura_vip_calcula_total_guarda_y_notifica():
    repo, notif = RepositorioFalso(), NotificadorFalso()
    servicio = ServicioFacturacion(repo, notif, IVA(), descuento_para)
    factura = Factura("F-001", "cliente@correo.co", "VIP",
                      [ItemFactura("Licencia", Decimal("100000"), 2)])

    total = servicio.emitir(factura)

    assert total == Decimal("214200")     # 200000 - 10% = 180000; + IVA 19%
    assert repo.guardadas == [("F-001", total)]
    assert len(notif.enviados) == 1
