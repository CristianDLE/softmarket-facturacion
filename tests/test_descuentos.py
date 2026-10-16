from decimal import Decimal

import pytest

from facturacion.descuentos import descuento_para


@pytest.mark.parametrize(
    "tipo, esperado",
    [("VIP", "90"), ("MAYORISTA", "85"), ("NORMAL", "100")],
)
def test_descuento_por_tipo_de_cliente(tipo, esperado):
    resultado = descuento_para(tipo).aplicar(Decimal("100"))
    assert resultado == Decimal(esperado)
