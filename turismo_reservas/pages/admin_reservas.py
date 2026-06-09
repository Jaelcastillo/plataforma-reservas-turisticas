import reflex as rx
from turismo_reservas.states.auth_state import AuthState

CREAM = "#F5EFE6"
GOLD = "#C9A84C"
TEXT_DARK = "#1B1B1B"


def admin_reservas():
    return rx.cond(
        AuthState.es_admin,
        rx.box(
            rx.vstack(
                rx.heading(
                    "Gestión de Reservas",
                    font_size="3rem",
                    color=TEXT_DARK,
                ),

                rx.button(
                    "Actualizar",
                    on_click=AuthState.cargar_todas_reservas,
                ),

                rx.table.root(
                    rx.table.header(
                        rx.table.row(
                            rx.table.column_header_cell("ID"),
                            rx.table.column_header_cell("Cliente"),
                            rx.table.column_header_cell("Oferta"),
                            rx.table.column_header_cell("Fecha"),
                            rx.table.column_header_cell("Total"),
                            rx.table.column_header_cell("Estado"),
                        )
                    ),
                    rx.table.body(
                        rx.foreach(
                            AuthState.admin_reservas,
                            lambda r: rx.table.row(
                                rx.table.cell(r["id"]),
                                rx.table.cell(r["nombre"]),
                                rx.table.cell(r["oferta"]),
                                rx.table.cell(r["fecha_viaje"]),
                                rx.table.cell(f"${r['total']}"),
                                rx.table.cell(r["estado"]),
                            )
                        )
                    ),
                    width="100%",
                ),

                rx.link(
                    rx.button("← Volver Dashboard"),
                    href="/admin/dashboard",
                ),

                spacing="5",
                padding="2rem",
            ),
            min_height="100vh",
            background=CREAM,
        ),
        rx.center(
            rx.heading("Acceso denegado"),
            min_height="100vh",
        ),
    )