import reflex as rx
from turismo_reservas.states.auth_state import AuthState

CREAM = "#F5EFE6"
GOLD = "#C9A84C"
GOLD_LT = "#F0D080"
GOLD_BOR = "rgba(201,168,76,0.35)"
TEXT_DARK = "#1B1B1B"
TEXT_SOFT = "#5E554D"

CSS = """
.admin-ofertas {
    min-height: 100vh;
    background:
        radial-gradient(circle at top left, rgba(201,168,76,.20), transparent 35%),
        radial-gradient(circle at bottom right, rgba(11,110,110,.12), transparent 35%),
        linear-gradient(135deg, #F5EFE6, #EFE3D4);
}
.offer-card, .edit-card {
    background: rgba(255,255,255,.92);
    border: 1px solid rgba(201,168,76,.28);
    border-radius: 28px;
    box-shadow: 0 20px 60px rgba(43,36,26,.12);
}
.offer-card {
    transition: all .25s ease;
}
.offer-card:hover {
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


def admin_input(label, value, on_change):
    return rx.vstack(
        rx.text(label, color=TEXT_DARK, font_weight="900", font_size="0.85rem"),
        rx.input(
            value=value,
            on_change=on_change,
            background="#FFFFFF",
            color="#1B1B1B",
            border=f"1px solid {GOLD_BOR}",
            border_radius="14px",
            padding="0.85rem 1rem",
            height="48px",
            width="100%",
            font_size="1rem",
            font_weight="700",
            line_height="1.2",
        ),
        spacing="2",
        width="100%",
        align="start",
    )

def admin_select(label, value, on_change, items):
    return rx.vstack(
        rx.text(label, color=TEXT_DARK, font_weight="900", font_size="0.85rem"),
        rx.select(
            items,
            value=value,
            on_change=on_change,
            placeholder=f"Selecciona {label.lower()}",
            background="#FFFFFF",
            color="#1B1B1B",
            border=f"1px solid {GOLD_BOR}",
            border_radius="14px",
            height="48px",
            width="100%",
            font_size="1rem",
            font_weight="700",
        ),
        spacing="2",
        width="100%",
        align="start",
    )


def destino_option(d):
    return rx.fragment(
        d["id"].to_string(),
        " - ",
        d["pais"],
        " - ",
        d["ciudad"],
        " - ",
        d["titulo"],
    )

def crear_oferta_form():
    return rx.box(
        rx.vstack(
            rx.heading(
                "Agregar nueva oferta",
                color=TEXT_DARK,
                font_family="'Playfair Display', serif",
                font_size="2rem",
                font_weight="900",
            ),

            rx.text(
                "Completa los datos de la oferta. Elige primero el destino al que pertenece.",
                color=TEXT_SOFT,
                font_weight="700",
            ),

            rx.grid(
                rx.vstack(
                    rx.text("Destino", color=TEXT_DARK, font_weight="900", font_size="0.85rem"),
                    rx.select.root(
                        rx.select.trigger(
                            placeholder="Selecciona un destino",
                            width="100%",
                        ),
                        rx.select.content(
                            rx.foreach(
                                AuthState.admin_destinos,
                                lambda d: rx.select.item(
                                    rx.fragment(
                                        "ID ",
                                        d["id"].to_string(),
                                        " · ",
                                        d["pais"],
                                        " · ",
                                        d["ciudad"],
                                        " · ",
                                        d["titulo"],
                                    ),
                                    value=d["id"].to_string(),
                                ),
                            ),
                        ),
                        value=AuthState.nuevo_oferta_destino_id,
                        on_change=AuthState.set_nuevo_oferta_destino_id,
                        width="100%",
                    ),
                    spacing="2",
                    width="100%",
                    align="start",
                ),

                admin_select(
                    "Categoría",
                    AuthState.nuevo_oferta_categoria,
                    AuthState.set_nuevo_oferta_categoria,
                    ["Hotel", "Resort", "Tour", "Excursión", "Parque", "Aventura", "Paquete completo"],
                ),

                admin_input(
                    "Título",
                    AuthState.nuevo_oferta_titulo,
                    AuthState.set_nuevo_oferta_titulo,
                ),

                admin_input(
                    "Precio actual. Ej: 350",
                    AuthState.nuevo_oferta_precio,
                    AuthState.set_nuevo_oferta_precio,
                ),

                admin_input(
                    "Precio anterior. Ej: 499",
                    AuthState.nuevo_oferta_precio_anterior,
                    AuthState.set_nuevo_oferta_precio_anterior,
                ),

               

                admin_select(
                    "Duración",
                    AuthState.nuevo_oferta_duracion,
                    AuthState.set_nuevo_oferta_duracion,
                    ["1 día", "4 horas", "8 horas", "3 noches", "5 noches", "7 noches", "Paquete completo"],
                ),

                admin_select(
                    "Rating",
                    AuthState.nuevo_oferta_rating,
                    AuthState.set_nuevo_oferta_rating,
                    ["4.5", "4.6", "4.7", "4.8", "4.9", "5.0"],
                ),

                admin_input(
                    "Imagen. Ej: hotel_rd.jpg",
                    AuthState.nuevo_oferta_imagen,
                    AuthState.set_nuevo_oferta_imagen,
                ),

                style={"gridTemplateColumns": "repeat(auto-fit, minmax(250px, 1fr))"},
                gap="1rem",
                width="100%",
            ),

            rx.vstack(
                rx.text("Descripción", color=TEXT_DARK, font_weight="900", font_size="0.85rem"),
                rx.text_area(
                    value=AuthState.nuevo_oferta_descripcion,
                    on_change=AuthState.set_nuevo_oferta_descripcion,
                    placeholder="Ej: Paquete todo incluido con hotel, desayuno, traslado y actividades.",
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

            rx.box(
                rx.vstack(
                    rx.text("Ayuda rápida", color=GOLD, font_weight="900"),
                    rx.text("• La imagen debe existir en assets/images o en tu carpeta pública de imágenes.", color=TEXT_SOFT),
                    rx.text("• Ejemplo de imagen: punta_cana.png, hotel_rd.jpg, disney.jpg.", color=TEXT_SOFT),
                    rx.text("• El destino elegido conecta esta oferta con Reservar Ahora.", color=TEXT_SOFT),
                    spacing="1",
                    align="start",
                ),
                background="#FFF8E8",
                border=f"1px solid {GOLD_BOR}",
                border_radius="18px",
                padding="1rem",
                width="100%",
            ),

            rx.button(
                "➕ Crear oferta",
                on_click=AuthState.crear_oferta_admin,
                class_name="gold-btn",
            ),

            spacing="4",
            align="start",
            width="100%",
        ),
        class_name="edit-card",
        padding="1.5rem",
        width="100%",
    )


def edit_form():
        return rx.box(
            rx.vstack(
               rx.hstack(
                rx.vstack(
                    rx.text(
                        "Editando oferta seleccionada",
                        color=GOLD,
                        font_size="0.75rem",
                        font_weight="900",
                        letter_spacing="2px",
                        text_transform="uppercase",
                    ),
                    rx.heading(
                        "Editar Oferta",
                        color=TEXT_DARK,
                        font_family="'Playfair Display', serif",
                        font_size="2rem",
                        font_weight="900",
                    ),
                    rx.text(
                        "El descuento se calcula automáticamente con el precio anterior guardado.",
                        color=TEXT_SOFT,
                        font_weight="700",
                    ),
                    spacing="1",
                    align="start",
                ),
                rx.spacer(),
                rx.button(
                    "Cerrar",
                    on_click=AuthState.cancelar_edicion_oferta,
                    class_name="outline-btn",
                ),
                width="100%",
                align="center",
            ),

            rx.grid(
                admin_input("Título", AuthState.edit_titulo_oferta, AuthState.set_edit_titulo_oferta),
                admin_select(
                    "Categoría",
                    AuthState.edit_categoria_oferta,
                    AuthState.set_edit_categoria_oferta,
                    ["Hotel", "Resort", "Tour", "Excursión", "Parque", "Aventura", "Paquete completo"],
                ),
                admin_input("Precio actual", AuthState.edit_precio_oferta, AuthState.set_edit_precio_oferta),
                style={"gridTemplateColumns": "repeat(auto-fit, minmax(220px, 1fr))"},
                gap="1rem",
                width="100%",
            ),

            admin_input(
              "Precio anterior",
               AuthState.edit_precio_anterior_oferta,
               AuthState.set_edit_precio_anterior_oferta,
            ),

            rx.box(
                rx.text(
                    "Nota: el porcentaje de descuento se recalcula solo al guardar.",
                    color=TEXT_SOFT,
                    font_weight="800",
                ),
                background="#FFF8E8",
                border=f"1px solid {GOLD_BOR}",
                border_radius="18px",
                padding="1rem",
                width="100%",
            ),

            rx.hstack(
                rx.button("Guardar cambios", on_click=AuthState.actualizar_oferta_admin, class_name="gold-btn"),
                rx.button("Cancelar", on_click=AuthState.cancelar_edicion_oferta, class_name="outline-btn"),
                spacing="3",
            ),

            spacing="4",
            align="start",
            width="100%",
        ),
        class_name="edit-card",
        padding="1.5rem",
        width="100%",
    )

def oferta_card(o):
    return rx.box(
        rx.hstack(
            rx.vstack(
                rx.text(
                    rx.fragment("OFERTA #", o["id"].to_string()),
                    color=GOLD,
                    font_size="0.75rem",
                    font_weight="900",
                    letter_spacing="2px",
                ),
                rx.heading(
                    o["titulo"],
                    color=TEXT_DARK,
                    font_family="'Playfair Display', serif",
                    font_size="1.7rem",
                    font_weight="900",
                ),
                rx.text(o["categoria"], color=TEXT_SOFT, font_weight="800"),
                rx.hstack(
                    rx.text("$", color=GOLD, font_size="1.6rem", font_weight="900"),
                    rx.text(o["precio"].to_string(), color=GOLD, font_size="1.6rem", font_weight="900"),
                    rx.text("USD", color=TEXT_SOFT),
                    spacing="1",
                ),
                rx.hstack(
                    rx.text("Descuento:", color=TEXT_SOFT),
                    rx.text(o["descuento"].to_string(), color=TEXT_DARK, font_weight="900"),
                    rx.text("%", color=TEXT_DARK, font_weight="900"),
                    spacing="1",
                ),
                spacing="2",
                align="start",
                flex="1",
            ),

            rx.vstack(
                rx.badge(
                    rx.cond(o["activo"], "Activa", "Inactiva"),
                    color_scheme=rx.cond(o["activo"], "green", "red"),
                    variant="soft",
                    size="2",
                ),
                rx.button(
                    "✏️ Editar",
                    on_click=lambda: AuthState.cargar_oferta_para_editar(o["id"]),
                    class_name="outline-btn",
                    width="180px",
                ),
                rx.button(
                    "👁️ Activar/Desactivar",
                    on_click=lambda: AuthState.toggle_oferta_admin(o["id"]),
                    class_name="outline-btn",
                    width="200px",
                ),
                rx.button(
                    "🗑️ Eliminar",
                    on_click=lambda: AuthState.eliminar_oferta_admin(o["id"]),
                    class_name="danger-btn",
                    width="180px",
                ),
                spacing="3",
                align="end",
            ),

            width="100%",
            align="center",
            spacing="5",
        ),
        class_name="offer-card",
        padding="1.5rem",
        width="100%",
    )


def admin_ofertas():
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
                            "Gestión de Ofertas",
                            color=TEXT_DARK,
                            font_family="'Playfair Display', serif",
                            font_size="clamp(2.5rem, 5vw, 4rem)",
                            font_weight="900",
                        ),
                        rx.text(
                            "Crea, edita, activa, desactiva o elimina ofertas turísticas.",
                            color=TEXT_SOFT,
                        ),
                        spacing="6",
                        align="start",
                    ),
                    rx.spacer(),
                    rx.button(
                        "Actualizar",
                        on_click=AuthState.cargar_ofertas_admin,
                        class_name="gold-btn",
                    ),
                    width="100%",
                    align="center",
                ),

                rx.cond(
                    AuthState.editando_oferta,
                    edit_form(),
                    rx.box(),
                ),

                crear_oferta_form(),

                rx.cond(
                    AuthState.admin_ofertas.length() > 0,
                    rx.vstack(
                        rx.foreach(AuthState.admin_ofertas, oferta_card),
                        spacing="4",
                        width="100%",
                    ),
                    rx.box(
                        rx.text(
                            "No hay ofertas cargadas. Pulsa Actualizar.",
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
            class_name="admin-ofertas",
        ),
        rx.center(rx.heading("Acceso denegado"), min_height="100vh"),
    )