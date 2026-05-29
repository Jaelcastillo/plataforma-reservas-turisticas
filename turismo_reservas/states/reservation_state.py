import reflex as rx
from datetime import datetime
from api.services import crear_reserva


class ReservationState(rx.State):
    nombre: str = ""
    email: str = ""
    telefono: str = ""
    pais_destino: str = ""
    oferta: str = ""
    fecha_viaje: str = ""
    personas: str = "1"
    metodo_pago: str = ""
    comentarios: str = ""
    mensaje: str = ""

    def set_nombre(self, value: str):
        self.nombre = value

    def set_email(self, value: str):
        self.email = value

    def set_telefono(self, value: str):
        self.telefono = value

    def set_pais_destino(self, value: str):
        self.pais_destino = value

    def set_oferta(self, value: str):
        self.oferta = value

    def set_fecha_viaje(self, value: str):
        self.fecha_viaje = value

    def set_personas(self, value: str):
        self.personas = value

    def set_metodo_pago(self, value: str):
        self.metodo_pago = value

    def set_comentarios(self, value: str):
        self.comentarios = value

    def guardar_reserva(self):
        try:
            if not self.nombre or not self.email or not self.pais_destino or not self.oferta or not self.fecha_viaje:
                self.mensaje = "❌ Completa los campos obligatorios."
                return

            crear_reserva(
                nombre=self.nombre,
                email=self.email,
                telefono=self.telefono,
                pais_destino=self.pais_destino,
                oferta=self.oferta,
                fecha_viaje=datetime.strptime(self.fecha_viaje, "%Y-%m-%d").date(),
                personas=int(self.personas),
                metodo_pago=self.metodo_pago,
                comentarios=self.comentarios,
            )

            self.nombre = ""
            self.email = ""
            self.telefono = ""
            self.pais_destino = ""
            self.oferta = ""
            self.fecha_viaje = ""
            self.personas = "1"
            self.metodo_pago = ""
            self.comentarios = ""
            self.mensaje = "✅ Reserva realizada correctamente."

        except Exception as e:
            self.mensaje = f"❌ Error al guardar reserva: {str(e)}"