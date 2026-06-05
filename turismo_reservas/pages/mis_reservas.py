import reflex as rx
from turismo_reservas.states.auth_state import AuthState

GOLD = "#C9A84C"
GOLD_LT = "#E8CF84"
CREAM = "#F5EFE6"
TEXT_DARK = "#2B241A"
TEXT_MUTED = "#6E6254"
GOLD_BOR = "rgba(201,168,76,0.35)"


def info_line(icon: str, label: str, value) -> rx.Component:
    return rx.hstack(
        rx.text(icon, font_size="1rem"),
        rx.text(label, color=TEXT_MUTED, font_weight="800"),
        rx.text(value, color=TEXT_DARK, font_weight="700"),
        spacing="2",
        align="center",
    )


def reserva_card(r):
    return rx.box(
        rx.hstack(
            rx.image(
                src=rx.cond(
                    r["oferta_imagen"] != "",
                    r["oferta_imagen"],
                    "/images/familia_viajando.jpg",
                ),
                width="260px",
                height="190px",
                object_fit="cover",
                border_radius="22px",
            ),
            rx.vstack(
                rx.text(
                    rx.cond(
                        r["codigo_reserva"] != "",
                        r["codigo_reserva"],
                        "Reserva TravelWorld",
                    ),
                    color=GOLD,
                    font_size="0.75rem",
                    font_weight="900",
                    letter_spacing="2px",
                ),
                rx.heading(
                    r["oferta"],
                    color=TEXT_DARK,
                    font_family="'Playfair Display', serif",
                    font_size="1.8rem",
                    font_weight="900",
                ),
                info_line("📍", "Destino:", r["pais_destino"]),
                info_line("📅", "Fecha:", r["fecha_viaje"].to_string()),
                info_line("👥", "Personas:", r["personas"].to_string()),
                info_line("💳", "Pago:", r["metodo_pago"]),
                rx.hstack(
                    rx.badge(
                        r["estado"],
                        color_scheme="yellow",
                        variant="soft",
                        size="2",
                    ),
                    rx.spacer(),
                    rx.hstack(
                        rx.text("$", color=TEXT_DARK, font_weight="900"),
                        rx.text(r["total"].to_string(), color=TEXT_DARK, font_size="1.5rem", font_weight="900"),
                        rx.text("USD", color=TEXT_DARK, font_weight="900"),
                        spacing="1",
                    ),
                    width="100%",
                ),
                rx.cond(
                    r["pdf_url"] != "",
                    rx.link(
                        rx.button(
                            "📄 Descargar PDF",
                            background=f"linear-gradient(135deg, {GOLD}, {GOLD_LT})",
                            color=TEXT_DARK,
                            border="none",
                            border_radius="999px",
                            padding="0.8rem 1.4rem",
                            font_weight="900",
                            cursor="pointer",
                        ),
                        href=r["pdf_url"],
                    ),
                    rx.text("PDF no disponible", color=TEXT_MUTED),
                ),
                spacing="3",
                align="start",
                flex="1",
            ),
            spacing="5",
            align="center",
            width="100%",
        ),
        background="white",
        border=f"1px solid {GOLD_BOR}",
        border_radius="28px",
        padding="1.4rem",
        width="100%",
        box_shadow="0 22px 60px rgba(43,36,26,0.10)",
    )


def mis_reservas():
    return rx.cond(
        AuthState.esta_logueado,
        rx.box(
            rx.vstack(
                rx.heading(
                    "Mis Reservas",
                    color=TEXT_DARK,
                    font_family="'Playfair Display', serif",
                    font_size="4rem",
                    font_weight="900",
                ),
                rx.text(
                    "Aquí verás tus viajes reservados, comprobantes y detalles.",
                    color=TEXT_MUTED,
                    font_size="1rem",
                ),
                rx.button(
                    "Actualizar reservas",
                    on_click=AuthState.cargar_mis_reservas,
                    background=f"linear-gradient(135deg, {GOLD}, {GOLD_LT})",
                    color=TEXT_DARK,
                    border="none",
                    border_radius="999px",
                    padding="0.85rem 1.7rem",
                    font_weight="900",
                    cursor="pointer",
                ),
                rx.cond(
                    AuthState.mis_reservas.length() > 0,
                    rx.vstack(
                        rx.foreach(AuthState.mis_reservas, reserva_card),
                        spacing="5",
                        width="100%",
                        max_width="1050px",
                    ),
                    rx.box(
                        rx.text("No tienes reservas registradas todavía.", color=TEXT_MUTED),
                        background="white",
                        border=f"1px solid {GOLD_BOR}",
                        border_radius="24px",
                        padding="2rem",
                        width="100%",
                        max_width="850px",
                    ),
                ),
                rx.link(
                    rx.button(
                        "← Volver al inicio",
                        background="white",
                        color=TEXT_DARK,
                        border=f"1px solid {GOLD_BOR}",
                        border_radius="999px",
                        padding="0.8rem 1.5rem",
                        font_weight="900",
                    ),
                    href="/",
                ),
                spacing="5",
                align="center",
                padding="4rem 2rem",
            ),
            min_height="100vh",
            background=CREAM,
        ),
        rx.center(
            rx.vstack(
                rx.heading("Debes iniciar sesión"),
                rx.link("Ir al login", href="/login"),
            ),
            min_height="100vh",
        ),
    )