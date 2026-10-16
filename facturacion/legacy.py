# facturacion/legacy.py  (estado inicial: "el caos")
import smtplib
import psycopg2


class Factura:
    def __init__(self, cliente, items, tipo_cliente, metodo_pago):
        self.cliente = cliente
        self.items = items              # lista de diccionarios sin validar
        self.tipo_cliente = tipo_cliente
        self.metodo_pago = metodo_pago

    def procesar(self):
        total = 0
        for it in self.items:                       # 1) calcula el subtotal
            total += it["precio"] * it["cantidad"]
        if self.tipo_cliente == "VIP":              # 2) descuentos con if/elif
            total = total * 0.90
        elif self.tipo_cliente == "MAYORISTA":
            total = total * 0.85
        total = total + total * 0.19                # 3) IVA "quemado" en el codigo
        db = psycopg2.connect("host=prod user=admin password=1234")   # 4) BD
        db.cursor().execute("INSERT INTO facturas VALUES (%s, %s)",
                            (self.cliente, total))
        if self.metodo_pago == "TARJETA":           # 5) pagos con if/elif
            pasarela_tarjeta.cobrar(total)
        elif self.metodo_pago == "PSE":
            pasarela_pse.cobrar(total)
        smtplib.SMTP("smtp.gmail.com").sendmail("a@x.co", self.cliente, "Su factura")
        generar_pdf(self)                           # 6) PDF y correo en la misma clase
        return total
