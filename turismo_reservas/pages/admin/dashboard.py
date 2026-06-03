import reflex as rx
from turismo_reservas.states.auth_state import AuthState

CREAM = "#F5EFE6"
GOLD = "#C9A84C"
GOLD_LT = "#F0D080"
GOLD_BOR = "rgba(201,168,76,0.35)"
TEXT_DARK = "#1B1B1B"
TEXT_SOFT = "#5E554D"

ADMIN_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500;600;700;800&display=swap');

.admin-page {
    min-height: 100vh;
    background:
        radial-gradient(circle at top left, rgba(201,168,76,.18), transparent 32%),
        radial-gradient(circle at bottom right, rgba(11,110,110,.15), transparent 35%),
        linear-gradient(135deg, #F5EFE6, #EFE3D4);
    font-family: 'DM Sans', sans-serif;
}

.admin-hero {
    position: relative;
    overflow: hidden;
    border-radius: 34px;
    background:
        linear-gradient(135deg, rgba(8,18,28,.92), rgba(18,42,50,.88)),
        url('/images/resort_bg.jpg') center/cover no-repeat;
    border: 1px solid rgba(201,168,76,.35);
    box-shadow: 0 30px 90px rgba(43,36,26,.22);
}

.admin-hero::before {
    content: "";
    position: absolute;
    inset: -40%;
    background: conic-gradient(from 180deg, transparent, rgba(201,168,76,.24), transparent, rgba(240,208,128,.12), transparent);
    animation: spinGlow 14s linear infinite;
}

.admin-hero-inner {
    position: relative;
    z-index: 2;
}

.admin-card {
    background: rgba(255,255,255,.78);
    border: 1px solid rgba(201,168,76,.28);
    border-radius: 26px;
    box-shadow: 0 18px 55px rgba(43,36,26,.12);
    backdrop-filter: blur(16px);
    transition: all .25s ease;
}

.admin-card:hover {
    transform: translateY(-7px);
    box-shadow: 0 28px 75px rgba(43,36,26,.18);
}

.admin-action {
    background: rgba(255,255,255,.82);
    border: 1px solid rgba(201,168,76,.28);
    border-radius: 24px;
    transition: all .25s ease;
}

.admin-action:hover {
    transform: translateY(-6px) scale(1.01);
    border-color: rgba(201,168,76,.65);
    box-shadow: 0 25px 65px rgba(43,36,26,.16);
}

.admin-btn {
    background: linear-gradient(135deg, #8B6A2E, #C9A84C, #F0D080);
    color: #1F2A35;
    border: none;
    border-radius: 999px;
    font-weight: 900;
    padding: .8rem 1.4rem;
    cursor: pointer;
    box-shadow: 0 14px 35px rgba(201,168,76,.32);
}

.admin-outline {
    background: transparent;
    color: white;
    border: 1px solid rgba(255,255,255,.35);
    border-radius: 999px;
    font-weight: 800;
    padding: .8rem 1.4rem;
    cursor: pointer;
}

@keyframes spinGlow {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

@keyframes fadeUp {
    from { opacity: 0; transform: translateY(28px); }
    to { opacity: 1; transform: translateY(0); }
}

.fade-up {
    animation: fadeUp .65s ease both;
}
"""


def stat_card(icon: str, label: str, value: str, accent: str) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.box(
                rx.center(
                    rx.text(
                        icon,
                        font_size="1.7rem",
                        line_height="1",
                    ),
                    width="100%",
                    height="100%",
                ),
                width="64px",
                height="64px",
                border_radius="20px",
                background=f"linear-gradient(135deg, {accent}, rgba(255,255,255,.35))",
                display="flex",
                align_items="center",
                justify_content="center",
                flex_shrink="0",
            ),

            rx.vstack(
                rx.text(
                    label,
                    color=TEXT_SOFT,
                    font_size="0.78rem",
                    font_weight="800",
                    text_transform="uppercase",
                    letter_spacing="1.2px",
                ),
                rx.heading(
                    value,
                    color=TEXT_DARK,
                    font_size="1.85rem",
                    font_family="'Playfair Display', serif",
                    font_weight="900",
                ),
                spacing="0",
                align="start",
            ),

            spacing="4",
            align="center",
        ),

        class_name="admin-card fade-up",
        padding="1.35rem",
        width="100%",
    )


def action_card(icon: str, title: str, desc: str, href: str) -> rx.Component:
    return rx.link(
        rx.box(
            rx.vstack(
                rx.center(
                    rx.html(
                        f"""
                        <div style="
                            width:72px;
                            height:72px;
                            border-radius:24px;
                            background:rgba(201,168,76,0.10);
                            border:1px solid {GOLD_BOR};
                            display:flex;
                            align-items:center;
                            justify-content:center;
                        ">
                            <span style="
                                display:flex;
                                align-items:center;
                                justify-content:center;
                                width:72px;
                                height:72px;
                                font-size:2rem;
                                font-weight:900;
                                color:{GOLD};
                                line-height:1;
                                text-align:center;
                                font-family:'DM Sans', sans-serif;
                            ">{icon}</span>
                        </div>
                        """
                    ),
                    width="100%",
                ),
                rx.heading(
                    title,
                    color=TEXT_DARK,
                    font_size="1.35rem",
                    font_family="'Playfair Display', serif",
                    font_weight="900",
                    text_align="center",
                    width="100%",
                ),
                rx.text(
                    desc,
                    color=TEXT_SOFT,
                    font_size="0.9rem",
                    line_height="1.55",
                    text_align="center",
                ),
                rx.center(
                    rx.button("Abrir panel →", class_name="admin-btn"),
                    width="100%",
                ),
                spacing="3",
                align="center",
                width="100%",
            ),
            class_name="admin-action fade-up",
            padding="1.5rem",
            height="100%",
            text_align="center",
        ),
        href=href,
        text_decoration="none",
    )


def admin_content() -> rx.Component:
    return rx.box(
        rx.html(f"<style>{ADMIN_CSS}</style>"),
        rx.vstack(
            rx.box(
                rx.box(
                    rx.hstack(
                        rx.vstack(
                            rx.text(
                                "✦ Panel privado TravelWorld ✦",
                                color=GOLD_LT,
                                font_size="0.78rem",
                                font_weight="900",
                                letter_spacing="2px",
                                text_transform="uppercase",
                            ),
                            rx.heading(
                                "Dashboard Administrativo",
                                color="white",
                                font_size="clamp(2.2rem, 5vw, 4rem)",
                                font_family="'Playfair Display', serif",
                                font_weight="900",
                                line_height="1.05",
                            ),
                            rx.text(
                                "Gestiona reservas, clientes, ingresos y ofertas desde un solo lugar.",
                                color="rgba(255,255,255,.78)",
                                font_size="1rem",
                                line_height="1.7",
                                max_width="560px",
                            ),
                            rx.hstack(
                                rx.link(rx.button("Ver reservas", class_name="admin-btn"), href="/admin/reservas"),
                                rx.link(rx.button("Gestionar ofertas", class_name="admin-outline"), href="/admin/ofertas"),
                                spacing="3",
                                margin_top="0.8rem",
                            ),
                            spacing="4",
                            align="start",
                        ),
                        rx.spacer(),
                        rx.box(
                            rx.vstack(
                                rx.text("👑", font_size="3rem"),
                                rx.text("Administrador", color=GOLD_LT, font_weight="900"),
                                rx.text(AuthState.nombre, color="white", font_size="1.2rem", font_weight="800"),
                                spacing="2",
                                align="center",
                            ),
                            background="rgba(255,255,255,.10)",
                            border="1px solid rgba(255,255,255,.18)",
                            border_radius="26px",
                            padding="1.5rem",
                            min_width="220px",
                        ),
                        width="100%",
                        align="center",
                    ),
                    class_name="admin-hero-inner",
                    padding="2.5rem",
                ),
                class_name="admin-hero fade-up",
                width="100%",
            ),

            rx.grid(
stat_card("📅", "Reservas", AuthState.admin_total_reservas.to_string(), "rgba(201,168,76,.30)"),
stat_card("💰", "Ingresos", "$" + AuthState.admin_total_ingresos.to_string(), "rgba(11,110,110,.24)"),
stat_card("👥", "Clientes", AuthState.admin_total_clientes.to_string(), "rgba(201,120,91,.24)"),
stat_card("🏷️", "Ofertas", AuthState.admin_total_ofertas.to_string(), "rgba(139,111,199,.22)"),
                style={"gridTemplateColumns": "repeat(auto-fit, minmax(220px, 1fr))"},
                gap="1rem",
                width="100%",
            ),

            rx.grid(
                action_card(
                    "R",
                    "Reservas",
                    "Ver, actualizar estados, revisar pagos y eliminar reservas de prueba.",
                    "/admin/reservas",
                ),
                action_card(
                    "O",
                    "Ofertas",
                    "Agregar, editar, activar, desactivar y eliminar ofertas turísticas.",
                    "/admin/ofertas",
                ),
                action_card(
                    "U",
                    "Usuarios",
                    "Consultar clientes registrados y diferenciar clientes de administradores.",
                    "/admin/usuarios",
                ),
                action_card(
                    "D",
                    "Destinos",
                    "Administrar países, ciudades, imágenes y experiencias destacadas.",
                    "/admin/destinos",
                ),
                style={"gridTemplateColumns": "repeat(auto-fit, minmax(260px, 1fr))"},
                gap="1.2rem",
                width="100%",
            ),

            rx.hstack(
                rx.link(
                    rx.button(
                        "← Volver al inicio",
                        background="white",
                        color=TEXT_DARK,
                        border=f"1px solid {GOLD_BOR}",
                        border_radius="999px",
                        padding="0.8rem 1.4rem",
                        font_weight="900",
                    ),
                    href="/",
                ),
                rx.button(
                    "Cerrar sesión",
                    on_click=AuthState.logout,
                    background="transparent",
                    color=TEXT_DARK,
                    border=f"1px solid {GOLD_BOR}",
                    border_radius="999px",
                    padding="0.8rem 1.4rem",
                    font_weight="900",
                ),
                spacing="3",
            ),

            spacing="6",
            max_width="1180px",
            width="100%",
            margin="0 auto",
            padding="2rem",
        ),
        class_name="admin-page",
        width="100%",
    )


def dashboard():
    return rx.cond(
        AuthState.es_admin,
        admin_content(),
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