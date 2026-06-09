import reflex as rx
from turismo_reservas.states.auth_state import AuthState

CREAM = "#F5EFE6"
GOLD = "#C9A84C"
GOLD_LT = "#F0D080"
GOLD_BOR = "rgba(201,168,76,0.35)"
TEXT_DARK = "#1B1B1B"
TEXT_SOFT = "#5E554D"

CSS = """
.admin-usuarios {
    min-height: 100vh;
    background:
        radial-gradient(circle at top left, rgba(201,168,76,.20), transparent 35%),
        radial-gradient(circle at bottom right, rgba(11,110,110,.12), transparent 35%),
        linear-gradient(135deg, #F5EFE6, #EFE3D4);
}
.user-card {
    background: rgba(255,255,255,.92);
    border: 1px solid rgba(201,168,76,.28);
    border-radius: 28px;
    box-shadow: 0 20px 60px rgba(43,36,26,.12);
    transition: all .25s ease;
}
.user-card:hover {
    transform: translateY(-5px);
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


def usuario_card(u):
    return rx.box(
        rx.hstack(
            rx.vstack(
                rx.text(
                    rx.fragment("USUARIO #", u["id"].to_string()),
                    color=GOLD,
                    font_size="0.75rem",
                    font_weight="900",
                    letter_spacing="2px",
                ),
                rx.heading(
                    u["nombre"],
                    color=TEXT_DARK,
                    font_family="'Playfair Display', serif",
                    font_size="1.7rem",
                    font_weight="900",
                ),
                rx.text(u["email"], color=TEXT_SOFT, font_weight="800"),
                rx.hstack(
                    rx.badge(
                        u["rol"],
                        color_scheme=rx.cond(u["rol"] == "admin", "purple", "blue"),
                        variant="soft",
                    ),
                    rx.badge(
                        rx.cond(u["activo"], "Activo", "Inactivo"),
                        color_scheme=rx.cond(u["activo"], "green", "red"),
                        variant="soft",
                    ),
                    spacing="2",
                ),
                spacing="8",
                align="start",
                flex="1",
            ),

            rx.vstack(
                rx.button(
                    "🔁 Cambiar rol",
                    on_click=lambda: AuthState.cambiar_rol_usuario_admin(u["id"], u["rol"]),
                    class_name="outline-btn",
                    width="170px",
                ),
                rx.button(
                    "👁️ Activar/Desactivar",
                    on_click=lambda: AuthState.toggle_usuario_admin(u["id"]),
                    class_name="outline-btn",
                    width="200px",
                ),
                rx.button(
                    "🗑️ Eliminar",
                    on_click=lambda: AuthState.eliminar_usuario_admin(u["id"]),
                    class_name="danger-btn",
                    width="170px",
                ),
                spacing="3",
                align="end",
            ),

            width="100%",
            align="center",
            spacing="5",
        ),
        class_name="user-card",
        padding="1.5rem",
        width="100%",
    )


def admin_usuarios():
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
                            "Gestión de Usuarios",
                            color=TEXT_DARK,
                            font_family="'Playfair Display', serif",
                            font_size="clamp(2.5rem, 5vw, 4rem)",
                            font_weight="900",
                        ),
                        rx.text(
                            "Administra clientes, roles y accesos del sistema.",
                            color=TEXT_SOFT,
                        ),
                        spacing="2",
                        align="start",
                    ),
                    rx.spacer(),
                    rx.button(
                        "Actualizar",
                        on_click=AuthState.cargar_usuarios_admin,
                        class_name="gold-btn",
                    ),
                    width="100%",
                    align="center",
                ),

                rx.cond(
                    AuthState.admin_usuarios.length() > 0,
                    rx.vstack(
                        rx.foreach(AuthState.admin_usuarios, usuario_card),
                        spacing="4",
                        width="100%",
                    ),
                    rx.box(
                        rx.text(
                            "No hay usuarios cargados. Pulsa Actualizar.",
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
                max_width="1100px",
                width="100%",
                margin="0 auto",
                padding="3rem 2rem",
            ),
            class_name="admin-usuarios",
        ),
        rx.center(rx.heading("Acceso denegado"), min_height="100vh"),
    )