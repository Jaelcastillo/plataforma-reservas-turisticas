import reflex as rx
from turismo_reservas.states.reservation_state import ReservationState


def reservas():
    return rx.box(
        rx.center(
            rx.vstack(
                rx.heading("Reserva tu Próxima Aventura", size="8"),
                rx.text("Completa el formulario para reservar tu viaje.", color="gray"),

                rx.input(
                    placeholder="Nombre completo",
                    value=ReservationState.nombre,
                    on_change=ReservationState.set_nombre,
                    width="100%",
                ),
                rx.input(
                    placeholder="Correo electrónico",
                    value=ReservationState.email,
                    on_change=ReservationState.set_email,
                    width="100%",
                ),
                rx.input(
                    placeholder="Teléfono",
                    value=ReservationState.telefono,
                    on_change=ReservationState.set_telefono,
                    width="100%",
                ),
                rx.input(
                    placeholder="Destino",
                    value=ReservationState.pais_destino,
                    on_change=ReservationState.set_pais_destino,
                    width="100%",
                ),
                rx.input(
                    placeholder="Oferta seleccionada",
                    value=ReservationState.oferta,
                    on_change=ReservationState.set_oferta,
                    width="100%",
                ),
                rx.input(
                    type="date",
                    value=ReservationState.fecha_viaje,
                    on_change=ReservationState.set_fecha_viaje,
                    width="100%",
                ),
                rx.input(
                    placeholder="Cantidad de personas",
                    value=ReservationState.personas,
                    on_change=ReservationState.set_personas,
                    width="100%",
                ),
                rx.select(
                    ["Tarjeta", "PayPal", "Transferencia"],
                    placeholder="Método de pago",
                    value=ReservationState.metodo_pago,
                    on_change=ReservationState.set_metodo_pago,
                    width="100%",
                ),
                rx.text_area(
                    placeholder="Comentarios adicionales",
                    value=ReservationState.comentarios,
                    on_change=ReservationState.set_comentarios,
                    width="100%",
                ),

                rx.button(
                    "Guardar Reserva",
                    on_click=ReservationState.guardar_reserva,
                    width="100%",
                    color_scheme="green",
                ),

                rx.text(ReservationState.mensaje, color="blue"),

                width="600px",
                spacing="4",
                padding="2rem",
            ),
            min_height="100vh",
        ),
    )