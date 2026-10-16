from facturacion.interfaces import Notificador


class NotificadorWhatsApp(Notificador):
    """WIP: esqueleto. Sustituye a otro Notificador sin cambiar el servicio (LSP)."""

    def enviar(self, destinatario: str, mensaje: str) -> None:
        raise NotImplementedError("Pendiente: integrar API de WhatsApp Business")
