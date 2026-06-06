import reflex as rx
from turismo_reservas.states.auth_state import AuthState

CREAM = "#F5EFE6"
GOLD = "#C9A84C"
GOLD_LT = "#F0D080"
GOLD_BOR = "rgba(201,168,76,0.35)"
TEXT_DARK = "#1B1B1B"
TEXT_SOFT = "#5E554D"
TEAL = "#0B6E6E"
TEAL_LT = "#1A9E9E"
CORAL = "#C9785B"

CSS = """
.ofertas-page {
    min-height: 100vh;
    background:
        radial-gradient(circle at top left, rgba(201,168,76,.18), transparent 35%),
        radial-gradient(circle at bottom right, rgba(11,110,110,.14), transparent 35%),
        linear-gradient(135deg, #F5EFE6, #EFE3D4);
}
.oferta-card {
    background: rgba(255,255,255,.88);
    border: 1px solid rgba(201,168,76,.28);
    border-radius: 28px;
    overflow: hidden;
    box-shadow: 0 20px 60px rgba(43,36,26,.12);
    transition: all .25s ease;
}
.oferta-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 32px 85px rgba(43,36,26,.20);
}
.gold-btn {
    background: linear-gradient(135deg, #8B6A2E, #C9A84C, #F0D080);
    color: #1B1B1B;
    border: none;
    border-radius: 999px;
    font-weight: 900;
    padding: .85rem 1.6rem;
}
.outline-btn {
    background: white;
    color: #1B1B1B;
    border: 1px solid rgba(201,168,76,.35);
    border-radius: 999px;
    font-weight: 900;
    padding: .85rem 1.6rem;
}
"""


def oferta_card(o):
    return rx.box(
        rx.box(
            rx.image(
                src=o["imagen"],
                width="100%",
                height="240px",
                object_fit="cover",
            ),
            rx.box(
                rx.text(
                    rx.fragment("-", o["descuento"].to_string(), "%"),
                    color="white",
                    font_weight="900",
                    font_size="0.8rem",
                ),
                position="absolute",
                top="16px",
                right="16px",
                background=f"linear-gradient(135deg, {CORAL}, {GOLD})",
                padding="0.45rem 0.9rem",
                border_radius="999px",
            ),
            position="relative",
        ),

        rx.vstack(
            rx.text(
                o["categoria"],
                color=GOLD,
                font_size="0.75rem",
                font_weight="900",
                letter_spacing="1.5px",
                text_transform="uppercase",
            ),
            rx.heading(
                o["titulo"],
                color=TEXT_DARK,
                font_family="'Playfair Display', serif",
                font_size="1.6rem",
                font_weight="900",
                line_height="1.1",
            ),
            rx.text(
                o["descripcion"],
                color=TEXT_SOFT,
                font_size="0.9rem",
                line_height="1.6",
                min_height="58px",
            ),
            rx.hstack(
                rx.vstack(
                    rx.text(
                        rx.fragment("$", o["precio_anterior"].to_string(), " USD"),
                        color="#A99882",
                        font_size="0.8rem",
                        text_decoration="line-through",
                    ),
                    rx.text(
                        rx.fragment("$", o["precio"].to_string()),
                        color=GOLD,
                        font_family="'Playfair Display', serif",
                        font_size="2rem",
                        font_weight="900",
                    ),
                    spacing="0",
                    align="start",
                ),
                rx.spacer(),
                rx.vstack(
                    rx.text("★★★★★", color=GOLD, font_size="0.9rem"),
                    rx.text(o["duracion"], color=TEXT_SOFT, font_size="0.8rem"),
                    spacing="1",
                    align="end",
                ),
                width="100%",
                align="center",
            ),
            rx.link(
                rx.button(
                    "Reservar ahora",
                    width="100%",
                    background=f"linear-gradient(135deg, {TEAL}, {TEAL_LT})",
                    color="white",
                    border="none",
                    border_radius="16px",
                    padding="0.9rem",
                    font_weight="900",
                    cursor="pointer",
                ),
                href="/reservas",
                width="100%",
            ),
            spacing="3",
            padding="1.5rem",
            align="start",
            width="100%",
        ),

        class_name="oferta-card",
        width="100%",
    )


def ofertas():
    return rx.box(
        rx.html(f"<style>{CSS}</style>"),

        rx.vstack(
            rx.hstack(
                rx.vstack(
                    rx.text(
                        "✦ TravelWorld Premium ✦",
                        color=GOLD,
                        font_size="0.8rem",
                        font_weight="900",
                        letter_spacing="2px",
                        text_transform="uppercase",
                    ),
                    rx.heading(
                        "Todas las Ofertas",
                        color=TEXT_DARK,
                        font_family="'Playfair Display', serif",
                        font_size="clamp(2.8rem, 6vw, 5rem)",
                        font_weight="999",
                    ),
                    rx.text(
                        "Explora todas las experiencias, resorts, tours y paquetes disponibles.",
                        color=TEXT_SOFT,
                        font_size="1rem",
                    ),
                    spacing="7",
                    align="start",
                ),
                rx.spacer(),
                rx.link(
                    rx.button("← Volver al inicio", class_name="outline-btn"),
                    href="/",
                ),
                width="100%",
                align="center",
            ),

            rx.cond(
                AuthState.ofertas_publicas.length() > 0,
                rx.grid(
                    rx.foreach(AuthState.ofertas_publicas, oferta_card),
                    style={"gridTemplateColumns": "repeat(auto-fit, minmax(310px, 1fr))"},
                    gap="1.5rem",
                    width="100%",
                ),
                rx.center(
                    rx.text("No hay ofertas activas disponibles.", color=TEXT_SOFT),
                    padding="4rem",
                ),
            ),

            spacing="6",
            max_width="1250px",
            width="100%",
            margin="0 auto",
            padding="3rem 2rem",
        ),

        class_name="ofertas-page",
        width="100%",
    )