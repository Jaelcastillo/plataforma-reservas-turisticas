import reflex as rx
from turismo_reservas.states.auth_state import AuthState

GOLD = "#C9A84C"
GOLD_LT = "#F0D080"
GOLD_BOR = "rgba(201,168,76,0.35)"
TEXT_DARK = "#1B1B1B"
TEXT_SOFT = "#5E554D"
CORAL = "#C9785B"

CSS = """
.admin-destinos {
    min-height: 100vh;
    background:
        radial-gradient(circle at top left, rgba(201,168,76,.20), transparent 35%),
        radial-gradient(circle at bottom right, rgba(11,110,110,.12), transparent 35%),
        linear-gradient(135deg, #F5EFE6, #EFE3D4);
}
.destino-card, .create-card {
    background: rgba(255,255,255,.92);
    border: 1px solid rgba(201,168,76,.28);
    border-radius: 28px;
    box-shadow: 0 20px 60px rgba(43,36,26,.12);
}
.destino-card {
    overflow: hidden;
    transition: all .25s ease;
}
.destino-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 30px 80px rgba(43,36,26,.18);
}
.gold-btn {
    background: linear-gradient(135deg, #8B6A2E, #C9A84C, #F0D080);
    color: #1B1B1B;
    border: none;
    border-radius: 999px;
    font-weight: 900;
    padding: .75rem 1.4rem;
}
.outline-btn {
    background: white;
    color: #1B1B1B;
    border: 1px solid rgba(201,168,76,.35);
    border-radius: 999px;
    font-weight: 900;
    padding: .75rem 1.4rem;
}
.danger-btn {
    background: #FFE2E2;
    color: #A61B1B;
    border: none;
    border-radius: 999px;
    font-weight: 900;
    padding: .75rem 1.4rem;
}
"""


def admin_input(label, value, on_change, placeholder=""):
    return rx.vstack(
        rx.text(label, color=TEXT_DARK, font_weight="900", font_size="0.85rem"),
        rx.input(
            value=value,
            on_change=on_change,
            placeholder=placeholder,
            background="white",
            color=TEXT_DARK,
            border=f"1px solid {GOLD_BOR}",
            border_radius="14px",
            padding="0.85rem 1rem",
            height="48px",
            width="100%",
            font_size="1rem",
            font_weight="700",
        ),
        spacing="2",
        width="100%",
        align="start",
    )


def crear_destino_form():
    return rx.box(
        rx.vstack(
            rx.heading(
                "Agregar nuevo destino",
                color=TEXT_DARK,
                font_family="'Playfair Display', serif",
                font_size="2rem",
                font_weight="900",
            ),
            rx.grid(
                admin_input("País", AuthState.nuevo_pais_destino, AuthState.set_nuevo_pais_destino, "República Dominicana"),
                admin_input("Ciudad", AuthState.nuevo_ciudad_destino, AuthState.set_nuevo_ciudad_destino, "Punta Cana"),
                admin_input("Título", AuthState.nuevo_titulo_destino, AuthState.set_nuevo_titulo_destino, "Paraíso Caribeño"),
                admin_input("Imagen", AuthState.nuevo_imagen_destino, AuthState.set_nuevo_imagen_destino, "offer_punta_cana.jpg"),
                style={"gridTemplateColumns": "repeat(auto-fit, minmax(220px, 1fr))"},
                gap="1rem",
                width="100%",
            ),
            rx.vstack(
                rx.text("Descripción", color=TEXT_DARK, font_weight="900", font_size="0.85rem"),
                rx.text_area(
                    value=AuthState.nuevo_descripcion_destino,
                    on_change=AuthState.set_nuevo_descripcion_destino,
                    placeholder="Describe el destino...",
                    background="white",
                    color=TEXT_DARK,
                    border=f"1px solid {GOLD_BOR}",
                    border_radius="14px",
                    padding="1rem",
                    width="100%",
                    min_height="110px",
                ),
                spacing="2",
                width="100%",
                align="start",
            ),
            rx.button(
                "➕ Crear destino",
                on_click=AuthState.crear_destino_admin,
                class_name="gold-btn",
            ),
            rx.cond(
                AuthState.mensaje != "",
                rx.text(AuthState.mensaje, color=CORAL, font_weight="800"),
                rx.box(),
            ),
            spacing="4",
            align="start",
            width="100%",
        ),
        class_name="create-card",
        padding="1.5rem",
        width="100%",
    )


def destino_card(d):
    return rx.box(
        rx.box(
            rx.image(
              src=d["imagen"],
              width="100%",
              height="230px",
              object_fit="cover",
),
            rx.box(
                rx.text(
                    rx.cond(d["destacado"], "⭐ Destacado", "Destino"),
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
                rx.fragment(d["pais"], " · ", d["ciudad"]),
                color=GOLD,
                font_size="0.78rem",
                font_weight="900",
                letter_spacing="1.5px",
                text_transform="uppercase",
            ),
            rx.heading(
                d["titulo"],
                color=TEXT_DARK,
                font_family="'Playfair Display', serif",
                font_size="1.5rem",
                font_weight="900",
            ),
            rx.text(
                d["descripcion"],
                color=TEXT_SOFT,
                font_size="0.9rem",
                line_height="1.55",
                min_height="70px",
            ),
            rx.hstack(
                rx.badge(
                    rx.cond(d["activo"], "Activo", "Inactivo"),
                    color_scheme=rx.cond(d["activo"], "green", "red"),
                    variant="soft",
                ),
                rx.badge(
                    rx.cond(d["destacado"], "Destacado", "Normal"),
                    color_scheme=rx.cond(d["destacado"], "yellow", "gray"),
                    variant="soft",
                ),
                spacing="2",
            ),
            rx.vstack(
                rx.button(
                    "⭐ Destacar/Normal",
                    on_click=lambda: AuthState.toggle_destacado_destino_admin(d["id"]),
                    class_name="outline-btn",
                    width="100%",
                ),
                rx.button(
                    "👁️ Activar/Desactivar",
                    on_click=lambda: AuthState.toggle_destino_admin(d["id"]),
                    class_name="outline-btn",
                    width="100%",
                ),
                rx.button(
                    "🗑️ Eliminar",
                    on_click=lambda: AuthState.eliminar_destino_admin(d["id"]),
                    class_name="danger-btn",
                    width="100%",
                ),
                spacing="2",
                width="100%",
            ),
            spacing="3",
            padding="1.4rem",
            align="start",
            width="100%",
        ),

        class_name="destino-card",
        width="100%",
    )


def admin_destinos():
    return rx.cond(
        AuthState.es_admin,
        rx.box(
            rx.html(f"<style>{CSS}</style>"),
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
                            "Gestión de Destinos",
                            color=TEXT_DARK,
                            font_family="'Playfair Display', serif",
                            font_size="clamp(2.5rem, 5vw, 4rem)",
                            font_weight="900",
                        ),
                        rx.text(
                            "Agrega países, ciudades, imágenes y destinos destacados.",
                            color=TEXT_SOFT,
                        ),
                        spacing="3",
                        align="start",
                    ),
                    rx.spacer(),
                    rx.button(
                        "Actualizar",
                        on_click=AuthState.cargar_destinos_admin,
                        class_name="gold-btn",
                    ),
                    width="100%",
                    align="center",
                ),

                crear_destino_form(),

                rx.cond(
                    AuthState.admin_destinos.length() > 0,
                    rx.grid(
                        rx.foreach(AuthState.admin_destinos, destino_card),
                        style={"gridTemplateColumns": "repeat(auto-fit, minmax(310px, 1fr))"},
                        gap="1.5rem",
                        width="100%",
                    ),
                    rx.box(
                        rx.text(
                            "No hay destinos cargados. Pulsa Actualizar.",
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

                rx.link(
                    rx.button("← Volver Dashboard", class_name="outline-btn"),
                    href="/admin/dashboard",
                ),

                spacing="6",
                max_width="1200px",
                width="100%",
                margin="0 auto",
                padding="3rem 2rem",
            ),
            class_name="admin-destinos",
        ),
        rx.center(rx.heading("Acceso denegado"), min_height="100vh"),
    )