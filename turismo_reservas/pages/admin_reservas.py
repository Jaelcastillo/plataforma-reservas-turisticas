import reflex as rx
from turismo_reservas.states.auth_state import AuthState

CREAM = "#F5EFE6"
GOLD = "#C9A84C"
GOLD_LT = "#F0D080"
GOLD_BOR = "rgba(201,168,76,0.35)"
TEXT_DARK = "#1B1B1B"
TEXT_SOFT = "#5E554D"

ADMIN_RESERVAS_CSS = """
.admin-reservas-page {
    min-height: 100vh;
    background:
        radial-gradient(circle at top left, rgba(201,168,76,.18), transparent 34%),
        radial-gradient(circle at bottom right, rgba(11,110,110,.12), transparent 34%),
        linear-gradient(135deg, #F5EFE6, #EFE3D4);
}

.reserva-card {
    background: rgba(255,255,255,.86);
    border: 1px solid rgba(201,168,76,.28);
    border-radius: 28px;
    box-shadow: 0 20px 60px rgba(43,36,26,.12);
    transition: all .25s ease;
}

.reserva-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 30px 80px rgba(43,36,26,.18);
}

.gold-btn {
    background: linear-gradient(135deg, #8B6A2E, #C9A84C, #F0D080);
    color: #1B1B1B;
    border: none;
    border-radius: 999px;
    font-weight: 900;
    padding: .75rem 1.3rem;
    cursor: pointer;
}

.outline-btn {
    background: white;
    color: #1B1B1B;
    border: 1px solid rgba(201,168,76,.35);
    border-radius: 999px;
    font-weight: 900;
    padding: .75rem 1.3rem;
    cursor: pointer;
}
"""


def reserva_card(r):
    return rx.box(
        rx.hstack(
            rx.vstack(
                rx.text(
                    "RESERVA #" + r["id"].to_string(),
                    color=GOLD,
                    font_size="0.75rem",
                    font_weight="900",
                    letter_spacing="2px",
                ),
                rx.heading(
                    r["oferta"],
                    color=TEXT_DARK,
                    font_family="'Playfair Display', serif",
                    font_size="1.7rem",
                    font_weight="900",
                ),
                rx.text(r["nombre"], color=TEXT_SOFT, font_weight="800"),
                rx.hstack(
                    rx.text("📅", font_size="1rem"),
                    rx.text(r["fecha_viaje"].to_string(), color=TEXT_SOFT),
                    spacing="2",
                ),
                rx.hstack(
                    rx.text("💰", font_size="1rem"),
                    rx.text(
                        "$" + r["total"].to_string() + " USD",
                        color=GOLD,
                        font_size="1.3rem",
                        font_weight="900",
                    ),
                    spacing="2",
                ),
                spacing="2",
                align="start",
                flex="1",
            ),

            rx.vstack(
                rx.badge(
                    r["estado"],
                    color_scheme="yellow",
                    variant="soft",
                    size="2",
                ),
               rx.button(
                    "✅ Confirmar",
                    on_click=lambda: AuthState.confirmar_reserva_admin(r["id"]),
                    background="#DDF7E8",
                    color="#146C43",
                    border="none",
                    border_radius="999px",
                    font_weight="900",
                    width="150px",
                ),
                rx.button(
                    "❌ Cancelar",
                    on_click=lambda: AuthState.cancelar_reserva_admin(r["id"]),
                    background="#FFF1D6",
                    color="#9A5B00",
                    border="none",
                    border_radius="999px",
                    font_weight="900",
                    width="150px",
                ),
                rx.button(
                    "🗑️ Eliminar",
                   on_click=lambda: AuthState.eliminar_reserva_admin(r["id"]),
                   background="#FFE2E2",
                   color="#A61B1B",
                   border="none",
                   border_radius="999px",
                   font_weight="900",
                   width="150px",
                ),
                spacing="3",
                align="end",
            ),

            width="100%",
            align="center",
            spacing="5",
        ),
        class_name="reserva-card",
        padding="1.5rem",
        width="100%",
    )


def admin_reservas():
    return rx.cond(
        AuthState.es_admin,
        rx.box(
            rx.html(f"<style>{ADMIN_RESERVAS_CSS}</style>"),

            rx.vstack(
                rx.hstack(
                    rx.vstack(
                        rx.text(
                            "✦ Panel administrativo ✦",
                            color=GOLD,
                            font_size="0.8rem",
                            font_weight="900",
                            letter_spacing="2px",
                            text_transform="uppercase",
                        ),
                        rx.heading(
                            "Gestión de Reservas",
                            color=TEXT_DARK,
                            font_family="'Playfair Display', serif",
                            font_size="clamp(2.5rem, 5vw, 4rem)",
                            font_weight="900",
                        ),
                        rx.text(
                            "Revisa, confirma, cancela o elimina reservas desde este panel.",
                            color=TEXT_SOFT,
                            font_size="1rem",
                        ),
                        spacing="2",
                        align="start",
                    ),
                    rx.spacer(),
                    rx.button(
                        "Actualizar reservas",
                        on_click=AuthState.cargar_todas_reservas,
                        class_name="gold-btn",
                    ),
                    width="100%",
                    align="center",
                ),

                rx.cond(
                    AuthState.admin_reservas.length() > 0,
                    rx.vstack(
                        rx.foreach(AuthState.admin_reservas, reserva_card),
                        spacing="4",
                        width="100%",
                    ),
                    rx.box(
                        rx.text(
                            "No hay reservas registradas todavía.",
                            color=TEXT_SOFT,
                            font_weight="800",
                        ),
                        background="white",
                        border=f"1px solid {GOLD_BOR}",
                        border_radius="24px",
                        padding="2rem",
                        width="100%",
                    ),
                ),

                rx.hstack(
                    rx.link(
                        rx.button("← Volver Dashboard", class_name="outline-btn"),
                        href="/admin/dashboard",
                    ),
                    rx.link(
                        rx.button("← Volver al inicio", class_name="outline-btn"),
                        href="/",
                    ),
                    spacing="3",
                ),

                spacing="6",
                max_width="1100px",
                width="100%",
                margin="0 auto",
                padding="3rem 2rem",
            ),

            class_name="admin-reservas-page",
            width="100%",
        ),
        rx.center(
            rx.vstack(
                rx.heading("Acceso denegado", color=TEXT_DARK),
                rx.text("Solo el administrador puede ver esta página.", color=TEXT_SOFT),
                rx.link("Volver al inicio", href="/"),
                spacing="4",
                align="center",
            ),
            min_height="100vh",
            background=CREAM,
        ),
    )