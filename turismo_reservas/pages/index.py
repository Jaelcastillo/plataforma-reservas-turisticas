"""
TravelWorld - Home Page Premium
Archivo: pages/index.py  (o donde tengas tu home en tu proyecto Reflex)

Uso en tu app principal (travelworld.py o similar):
    import reflex as rx
    from .pages.index import index
    app = rx.App()
    app.add_page(index, route="/")
"""

import reflex as rx

# ─── Paleta de colores ────────────────────────────────────────────────────────
DARK      = "#0D1B2A"
TEAL      = "#0B6E6E"
TEAL_LT   = "#1A9E9E"
GOLD      = "#C9A84C"
GOLD_LT   = "#F0D080"
CORAL     = "#E8735A"
PURPLE    = "#9B7FD4"
GLASS_BG  = "rgba(255,255,255,0.06)"
GLASS_BOR = "rgba(255,255,255,0.12)"
GOLD_BOR  = "rgba(201,168,76,0.25)"

# ─── Estilos compartidos ──────────────────────────────────────────────────────
NAV_LINK = dict(
    color="rgba(255,255,255,0.72)",
    font_size="0.85rem",
    font_weight="500",
    letter_spacing="0.5px",
    text_decoration="none",
    cursor="pointer",
    _hover={"color": GOLD},
    transition="color 0.2s",
)

SECTION_TAG_STYLE = dict(
    display="inline_block",
    color=GOLD,
    font_size="0.7rem",
    text_transform="uppercase",
    letter_spacing="2px",
    font_weight="600",
    margin_bottom="0.5rem",
)

CARD_HOVER = dict(
    transition="transform 0.3s, box-shadow 0.3s",
    _hover={
        "transform": "translateY(-8px) scale(1.015)",
        "box_shadow": "0 28px 60px rgba(0,0,0,0.55)",
    },
)

# ─────────────────────────────────────────────────────────────────────────────
#  COMPONENTES REUTILIZABLES
# ─────────────────────────────────────────────────────────────────────────────

def gold_gradient_text(text: str, size: str = "1rem") -> rx.Component:
    """Texto con gradiente dorado."""
    return rx.text(
        text,
        style={
            "background": f"linear-gradient(135deg, {GOLD}, {GOLD_LT}, {CORAL})",
            "WebkitBackgroundClip": "text",
            "WebkitTextFillColor": "transparent",
            "backgroundClip": "text",
            "fontSize": size,
            "fontFamily": "'Playfair Display', serif",
            "fontWeight": "900",
            "display": "inline",
        },
    )


def section_header(tag: str, title_plain: str, title_accent: str) -> rx.Component:
    return rx.vstack(
        rx.text(tag, style=SECTION_TAG_STYLE),
        rx.hstack(
            rx.heading(
                title_plain,
                style={
                    "fontFamily": "'Playfair Display', serif",
                    "fontSize": "clamp(1.8rem, 4vw, 2.5rem)",
                    "fontWeight": "700",
                    "color": "white",
                    "marginRight": "0.4rem",
                },
            ),
            gold_gradient_text(title_accent, size="clamp(1.8rem, 4vw, 2.5rem)"),
            align="center",
            spacing="1",
        ),
        align="center",
        spacing="2",
        margin_bottom="2.5rem",
    )


# ─────────────────────────────────────────────────────────────────────────────
#  NAVBAR
# ─────────────────────────────────────────────────────────────────────────────

def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            # Logo
            rx.text(
                "TravelWorld",
                style={
                    "fontFamily": "'Playfair Display', serif",
                    "fontSize": "1.5rem",
                    "fontWeight": "900",
                    "background": f"linear-gradient(135deg, {GOLD}, {GOLD_LT}, {GOLD})",
                    "WebkitBackgroundClip": "text",
                    "WebkitTextFillColor": "transparent",
                    "backgroundClip": "text",
                    "letterSpacing": "2px",
                    "cursor": "pointer",
                },
            ),
            rx.spacer(),
            # Links
            rx.hstack(
                rx.link("Destinos",   href="#destinos",   style=NAV_LINK),
                rx.link("Ofertas",    href="#ofertas",    style=NAV_LINK),
                rx.link("Resorts",    href="#resorts",    style=NAV_LINK),
                rx.link("Tours",      href="#tours",      style=NAV_LINK),
                rx.link("Disney",     href="#disney",     style=NAV_LINK),
                spacing="7",
                display=["none", "none", "flex"],
            ),
            rx.spacer(),
            # CTA
            rx.button(
                "Reservar Ahora",
                background=f"linear-gradient(135deg, {GOLD}, {GOLD_LT})",
                color=DARK,
                border="none",
                padding="0.5rem 1.4rem",
                border_radius="25px",
                font_weight="700",
                font_size="0.8rem",
                letter_spacing="0.5px",
                cursor="pointer",
                _hover={"opacity": "0.9", "transform": "translateY(-1px)"},
                transition="all 0.2s",
            ),
            width="100%",
            align="center",
            max_width="1200px",
            margin="0 auto",
            padding="0 1rem",
        ),
        position="sticky",
        top="0",
        z_index="100",
        background="rgba(13,27,42,0.9)",
        style={"backdropFilter": "blur(20px)"},
        border_bottom=f"1px solid {GOLD_BOR}",
        height="64px",
        display="flex",
        align="center",
        width="100%",
    )


# ─────────────────────────────────────────────────────────────────────────────
#  HERO
# ─────────────────────────────────────────────────────────────────────────────

def search_field(label: str, placeholder: str) -> rx.Component:
    return rx.vstack(
        rx.text(
            label,
            style={
                "fontSize": "0.62rem",
                "textTransform": "uppercase",
                "letterSpacing": "1.2px",
                "color": GOLD,
                "fontWeight": "700",
            },
        ),
        rx.input(
            placeholder=placeholder,
            background="transparent",
            border="none",
            border_bottom="1px solid rgba(255,255,255,0.2)",
            border_radius="0",
            color="white",
            font_size="0.88rem",
            padding="0.3rem 0",
            width="100%",
            _placeholder={"color": "rgba(255,255,255,0.4)"},
            _focus={"border_bottom": f"1px solid {GOLD}", "box_shadow": "none"},
        ),
        spacing="1",
        flex="1",
        min_width="110px",
    )


def hero_section() -> rx.Component:
    return rx.box(
        # Fondo con capas de gradiente

        
       rx.box(
    position="absolute",
    inset="0",
    style={
        "background": (
            "linear-gradient(rgba(13,27,42,0.55), rgba(13,27,42,0.78)), "
            "url('/images/hero_bg.png') center/cover no-repeat"
        ),
    },
),
        # Overlay inferior
        rx.box(
            position="absolute", bottom="0", left="0", right="0", height="140px",
            style={"background": f"linear-gradient(180deg, transparent 0%, rgba(13,27,42,0.85) 100%)"},
        ),
        # Contenido principal
        rx.vstack(
            # Badge superior
            rx.box(
                rx.text("✦  Plataforma Premium de Viajes  ✦",
                        font_size="0.72rem", font_weight="600", letter_spacing="1.5px"),
                background="rgba(201,168,76,0.12)",
                border=f"1px solid rgba(201,168,76,0.4)",
                color=GOLD,
                padding="0.4rem 1.3rem",
                border_radius="25px",
                style={"animation": "fadeInDown 0.8s ease both"},
            ),
            # Título
            rx.vstack(
                rx.heading(
                    "Descubre el Mundo",
                    style={
                        "fontFamily": "'Playfair Display', serif",
                        "fontSize": "clamp(3rem, 7vw, 5rem)",
                        "fontWeight": "900",
                        "color": "white",
                        "lineHeight": "1.1",
                    },
                ),
                gold_gradient_text("Sin Límites", size="clamp(3rem, 7vw, 5rem)"),
                spacing="1",
                align="center",
                style={"animation": "fadeInUp 0.9s ease 0.1s both"},
            ),
            # Subtítulo
            rx.text(
                "Destinos únicos, resorts de lujo, tours extremos y experiencias mágicas."
                " Tu aventura perfecta comienza aquí.",
                color="rgba(255,255,255,0.68)",
                font_size="1.05rem",
                text_align="center",
                max_width="520px",
                line_height="1.75",
                style={"animation": "fadeInUp 0.9s ease 0.2s both"},
            ),
            # Search box
            rx.box(
                rx.hstack(
                    search_field("Destino",  "¿A dónde quieres ir?"),
                    rx.divider(orientation="vertical", height="44px", border_color="rgba(255,255,255,0.15)"),
                    search_field("Llegada",  "Fecha de llegada"),
                    rx.divider(orientation="vertical", height="44px", border_color="rgba(255,255,255,0.15)"),
                    search_field("Salida",   "Fecha de salida"),
                    rx.divider(orientation="vertical", height="44px", border_color="rgba(255,255,255,0.15)"),
                    search_field("Viajeros", "2 adultos"),
                    rx.button(
                        "🔍  Buscar",
                        background=f"linear-gradient(135deg, {GOLD}, {GOLD_LT})",
                        color=DARK,
                        border="none",
                        padding="0.75rem 1.75rem",
                        border_radius="12px",
                        font_weight="700",
                        font_size="0.85rem",
                        white_space="nowrap",
                        align_self="flex-end",
                        cursor="pointer",
                        _hover={"transform": "translateY(-2px)", "box_shadow": f"0 8px 25px rgba(201,168,76,0.4)"},
                        transition="all 0.15s",
                    ),
                    spacing="4",
                    align="end",
                    width="100%",
                    flex_wrap="wrap",
                ),
                background=GLASS_BG,
                style={"backdropFilter": "blur(20px)"},
                border=f"1px solid {GLASS_BOR}",
                border_radius="20px",
                padding="1.4rem 1.8rem",
                max_width="760px",
                width="100%",
                box_shadow="0 20px 60px rgba(0,0,0,0.45)",
                style_={"animation": "fadeInUp 0.9s ease 0.3s both"},
            ),
            spacing="7",
            align="center",
            position="relative",
            z_index="2",
            padding="0 1.5rem",
            max_width="860px",
            text_align="center",
        ),
        position="relative",
        min_height="92vh",
        display="flex",
        align="center",
        justify="center",
        overflow="hidden",
        width="100%",
    )


# ─────────────────────────────────────────────────────────────────────────────
#  STATS BAR
# ─────────────────────────────────────────────────────────────────────────────

def stat_item(number: str, label: str) -> rx.Component:
    return rx.vstack(
        rx.text(
            number,
            style={
                "fontFamily": "'Playfair Display', serif",
                "fontSize": "1.7rem",
                "fontWeight": "700",
                "color": GOLD,
            },
        ),
        rx.text(
            label,
            font_size="0.68rem",
            text_transform="uppercase",
            letter_spacing="1px",
            color="rgba(255,255,255,0.45)",
        ),
        spacing="1",
        align="center",
    )


def stats_bar() -> rx.Component:
    return rx.flex(
        stat_item("1,200+", "Destinos disponibles"),
        stat_item("98%",    "Clientes satisfechos"),
        stat_item("50K+",   "Reservas realizadas"),
        stat_item("24/7",   "Soporte premium"),
        justify="center",
        gap="3rem",
        flex_wrap="wrap",
        padding="1.4rem 2rem",
        background=f"linear-gradient(135deg, rgba(11,110,110,0.25), rgba(201,168,76,0.08))",
        border_top=f"1px solid {GOLD_BOR}",
        border_bottom=f"1px solid {GOLD_BOR}",
        width="100%",
    )


# ─────────────────────────────────────────────────────────────────────────────
#  TARJETAS DE DESTINOS
# ─────────────────────────────────────────────────────────────────────────────

# Datos de destinos — reemplaza las URLs con tus imágenes locales
DESTINATIONS = [
    {
        "name": "Punta Cana",
        "country": "República Dominicana",
        "badge": "🏝 Playa",
        "price": "$899",
        "bg": "url('/images/punta_cana.png') center/cover no-repeat",
    },
    {
        "name": "Cancún",
        "country": "México",
        "badge": "🌊 Resort",
        "price": "$1,199",
        "bg": "url('/images/cancun.jpg.jpg') center/cover no-repeat",
    },
    {
        "name": "Walt Disney World",
        "country": "Orlando, Florida",
        "badge": "✨ Mágico",
        "price": "$2,499",
        "bg": "url('/images/disney.jpg') center/cover no-repeat",
    },
    {
        "name": "Cartagena",
        "country": "Colombia",
        "badge": "🌿 Cultura",
        "price": "$749",
        "bg": "url('/images/cartagena.jpg') center/cover no-repeat",
    },
    {
        "name": "San Juan",
        "country": "Puerto Rico",
        "badge": "🌺 Tropical",
        "price": "$999",
        "bg": "url('/images/puerto_rico.jpg') center/cover no-repeat",
    },
]

def destination_card(dest: dict) -> rx.Component:
    return rx.box(
        # Fondo con imagen o gradiente
        rx.box(
            position="absolute", inset="0",
            style={"background": dest["bg"], "transition": "transform 0.4s"},
        ),
        # Overlay oscuro inferior
        rx.box(
            position="absolute", inset="0",
            style={"background": "linear-gradient(180deg, transparent 35%, rgba(0,0,0,0.88) 100%)"},
        ),
        # Contenido
        rx.box(
            rx.box(
                rx.text(dest["badge"],
                        font_size="0.6rem", font_weight="700",
                        color=DARK, letter_spacing="0.5px",
                        text_transform="uppercase"),
                background="rgba(201,168,76,0.92)",
                padding="3px 10px",
                border_radius="20px",
                display="inline-block",
                margin_bottom="0.5rem",
            ),
            rx.heading(
                dest["name"],
                style={"fontFamily": "'Playfair Display', serif",
                       "fontSize": "1.2rem", "fontWeight": "700",
                       "color": "white", "lineHeight": "1.2"},
            ),
            rx.text(dest["country"], font_size="0.72rem",
                    color="rgba(255,255,255,0.62)", margin_top="2px"),
            rx.text(
                rx.fragment("Desde ", rx.text.span(dest["price"],
                    color=GOLD, font_weight="700", font_size="1rem")),
                font_size="0.78rem", color="rgba(255,255,255,0.55)",
                margin_top="0.5rem",
            ),
            position="absolute", bottom="0", left="0", right="0",
            padding="1.25rem",
        ),
        position="relative",
        border_radius="20px",
        overflow="hidden",
        aspect_ratio="3/4",
        cursor="pointer",
        border=f"1px solid rgba(255,255,255,0.08)",
        **CARD_HOVER,
    )


def destinations_section() -> rx.Component:
    return rx.box(
        section_header("✦ Explora el mundo ✦", "Destinos", "Exclusivos"),
        rx.grid(
            *[destination_card(d) for d in DESTINATIONS],
            columns="5",
            spacing="4",
            max_width="1100px",
            margin="0 auto",
            style={"gridTemplateColumns": "repeat(auto-fit, minmax(185px, 1fr))"},
        ),
        id="destinos",
        padding="4rem 2rem",
        width="100%",
    )


# ─────────────────────────────────────────────────────────────────────────────
#  OFERTAS DEL MOMENTO
# ─────────────────────────────────────────────────────────────────────────────

OFFERS = [
    {
        "name":       "Hard Rock Hotel Punta Cana",
        "sub":        "All-Inclusive · Punta Cana, RD",
        "old_price":  "$1,399",
        "new_price":  "$899",
        "nights":     "por persona · 7 noches",
        "rating":     "4.9",
        "reviews":    "2,341",
        "discount":   "-35% HOY",
        "left":       "¡Quedan 3!",
        "bg":         "linear-gradient(160deg,#0B5E6B,#1A9E9E,#065A4D)",
    },
    {
        "name":       "Marriott Cancún Resort",
        "sub":        "Vista al Mar · Cancún, México",
        "old_price":  "$1,650",
        "new_price":  "$1,199",
        "nights":     "por persona · 5 noches",
        "rating":     "4.8",
        "reviews":    "1,890",
        "discount":   "-28% HOY",
        "left":       "¡Quedan 5!",
        "bg":         "linear-gradient(160deg,#0B4E8A,#1A7AC0,#0B6E3A)",
    },
    {
        "name":       "Disney World + Hotel Premium",
        "sub":        "Paquete Completo · Orlando, FL",
        "old_price":  "$3,099",
        "new_price":  "$2,499",
        "nights":     "por persona · 6 noches",
        "rating":     "5.0",
        "reviews":    "8,721",
        "discount":   "-20% HOY",
        "left":       "¡Popular!",
        "bg":         "linear-gradient(160deg,#2D0E5C,#5A2A9A,#1A4A8A)",
    },
]


def offer_card(offer: dict) -> rx.Component:
    return rx.box(
        # Imagen/fondo
        rx.box(
            rx.box(
                rx.text(offer["discount"], font_size="0.73rem", font_weight="700",
                        color="white"),
                position="absolute", top="12px", right="12px",
                background=f"linear-gradient(135deg, {CORAL}, #C9584A)",
                padding="4px 12px", border_radius="20px",
            ),
            style={"background": offer["bg"]},
            height="160px",
            position="relative",
            overflow="hidden",
        ),
        # Body
        rx.vstack(
            rx.text(offer["name"], font_weight="600", font_size="0.96rem", color="white"),
            rx.text(offer["sub"],  font_size="0.78rem",
                    color="rgba(255,255,255,0.52)"),
            rx.text(
                f"★★★★★  {offer['rating']}  ({offer['reviews']} reseñas)",
                font_size="0.73rem", color=GOLD,
            ),
            rx.hstack(
                rx.vstack(
                    rx.text(f"{offer['old_price']} / persona",
                            font_size="0.72rem",
                            color="rgba(255,255,255,0.33)",
                            text_decoration="line-through"),
                    rx.text(offer["new_price"],
                            style={"fontFamily": "'Playfair Display', serif",
                                   "fontSize": "1.45rem", "fontWeight": "700",
                                   "color": GOLD}),
                    rx.text(offer["nights"],
                            font_size="0.63rem",
                            color="rgba(255,255,255,0.4)"),
                    spacing="0",
                    align="start",
                ),
                rx.spacer(),
                rx.text(offer["left"], font_size="0.65rem",
                        font_weight="700", color=CORAL),
                width="100%",
            ),
            rx.button(
                "Reservar Ahora",
                width="100%",
                background=f"linear-gradient(135deg, {TEAL}, {TEAL_LT})",
                color="white",
                border="none",
                border_radius="10px",
                font_weight="600",
                font_size="0.85rem",
                padding="0.6rem",
                cursor="pointer",
                _hover={"opacity": "0.85"},
                transition="opacity 0.2s",
            ),
            spacing="3",
            padding="1.1rem",
            align="start",
            width="100%",
        ),
        background="rgba(255,255,255,0.05)",
        border=f"1px solid rgba(255,255,255,0.1)",
        border_radius="18px",
        overflow="hidden",
        transition="transform 0.3s, border-color 0.3s",
        _hover={
            "transform": "translateY(-5px)",
            "border_color": "rgba(201,168,76,0.4)",
        },
    )


def offers_section() -> rx.Component:
    return rx.box(
        section_header("⚡ Tiempo limitado", "Ofertas del", "Momento"),
        rx.grid(
            *[offer_card(o) for o in OFFERS],
            style={"gridTemplateColumns": "repeat(auto-fit, minmax(280px, 1fr))"},
            gap="1.25rem",
            max_width="1100px",
            margin="0 auto",
        ),
        id="ofertas",
        padding="4rem 2rem",
        background="rgba(255,255,255,0.02)",
        border_top="1px solid rgba(255,255,255,0.06)",
        border_bottom="1px solid rgba(255,255,255,0.06)",
        width="100%",
    )


# ─────────────────────────────────────────────────────────────────────────────
#  SECCIÓN DISNEY
# ─────────────────────────────────────────────────────────────────────────────

DISNEY_PARKS = [
    ("Magic Kingdom",    "linear-gradient(135deg,#2D0E5C,#5A2A9A)"),
    ("EPCOT",            "linear-gradient(135deg,#1A3A8A,#2D5CAA)"),
    ("Hollywood Studios","linear-gradient(135deg,#3A1A5C,#6A3A9A)"),
    ("Animal Kingdom",   "linear-gradient(135deg,#1A5C2A,#3A9A4A)"),
]

DISNEY_FEATURES = [
    "Acceso a todos los 4 parques principales",
    "Hotel dentro del resort de Disney",
    "Traslados aeropuerto incluidos",
    "Desayuno con personajes de Disney",
    "Fast Pass y reservaciones prioritarias",
]


def disney_park_card(name: str, bg: str) -> rx.Component:
    return rx.flex(
        rx.text(name, font_size="0.73rem", font_weight="600",
                text_align="center", color="white",
                padding="0 0.5rem", line_height="1.3"),
        style={"background": bg},
        border_radius="14px",
        border=f"1px solid rgba(155,127,212,0.3)",
        aspect_ratio="16/10",
        align="end",
        justify="center",
        padding_bottom="0.75rem",
        cursor="pointer",
        transition="transform 0.25s",
        _hover={"transform": "scale(1.04)"},
    )


def disney_section() -> rx.Component:
    return rx.box(
        rx.grid(
            # Texto izquierdo
            rx.vstack(
                rx.text("✦  La magia te espera  ✦",
                        style={**SECTION_TAG_STYLE, "color": PURPLE}),
                rx.hstack(
                    rx.heading(
                        "Vive la Magia de ",
                        style={"fontFamily": "'Playfair Display', serif",
                               "fontSize": "clamp(1.8rem,4vw,2.4rem)",
                               "fontWeight": "700", "color": "white"},
                    ),
                    rx.text(
                        "Disney World",
                        style={
                            "fontFamily": "'Playfair Display', serif",
                            "fontSize": "clamp(1.8rem,4vw,2.4rem)",
                            "fontWeight": "700",
                            "background": f"linear-gradient(135deg, {PURPLE}, {GOLD})",
                            "WebkitBackgroundClip": "text",
                            "WebkitTextFillColor": "transparent",
                            "backgroundClip": "text",
                        },
                    ),
                    flex_wrap="wrap",
                    spacing="0",
                    align="baseline",
                ),
                rx.text(
                    "Paquetes completos con hotel, boletos y experiencias exclusivas. "
                    "La aventura más mágica del mundo te espera en Orlando, Florida.",
                    color="rgba(255,255,255,0.6)", font_size="0.9rem",
                    line_height="1.8", max_width="440px",
                ),
                rx.vstack(
                    *[
                        rx.hstack(
                            rx.text("✦", color=GOLD, font_size="0.7rem"),
                            rx.text(feat, font_size="0.88rem",
                                    color="rgba(255,255,255,0.8)"),
                            spacing="2", align="center",
                        )
                        for feat in DISNEY_FEATURES
                    ],
                    spacing="3",
                    align="start",
                ),
                rx.button(
                    "Ver Paquetes Disney ✨",
                    background=f"linear-gradient(135deg, {PURPLE}, {GOLD})",
                    color="white", border="none",
                    padding="0.75rem 2rem", border_radius="30px",
                    font_weight="700", font_size="0.9rem",
                    letter_spacing="0.5px", cursor="pointer",
                    _hover={"opacity": "0.9", "transform": "translateY(-2px)"},
                    transition="all 0.2s",
                ),
                spacing="5", align="start",
            ),
            # Grid parques derecho
            rx.grid(
                *[disney_park_card(name, bg) for name, bg in DISNEY_PARKS],
                columns="2",
                gap="0.75rem",
            ),
            columns="2",
            gap="3rem",
            align="center",
            max_width="1100px",
            margin="0 auto",
        ),
        id="disney",
        padding="4rem 2rem",
        style={
            "background": f"linear-gradient(135deg, {DARK}, #1A1040, #2D0E5C, #0B3D5E)",
        },
        border_top=f"1px solid {GOLD_BOR}",
        border_bottom=f"1px solid {GOLD_BOR}",
        width="100%",
    )


# ─────────────────────────────────────────────────────────────────────────────
#  TOURS BUGGY
# ─────────────────────────────────────────────────────────────────────────────

def buggy_main_card() -> rx.Component:
    return rx.box(
        rx.box(
            position="absolute", inset="0",
            style={"background": "linear-gradient(180deg, transparent 40%, rgba(0,0,0,0.82) 100%)"},
        ),
        rx.vstack(
            rx.box(
                rx.text("⚡  MÁS VENDIDO", font_size="0.63rem",
                        font_weight="700", color="white",
                        letter_spacing="1px", text_transform="uppercase"),
                background=f"rgba(232,115,90,0.9)",
                padding="4px 12px", border_radius="20px",
                display="inline-block",
            ),
            rx.heading(
                "Safari Buggy Punta Cana",
                style={"fontFamily": "'Playfair Display', serif",
                       "fontSize": "1.5rem", "fontWeight": "700",
                       "color": "white"},
            ),
            rx.text("8 horas · Todo incluido · Guía bilingüe",
                    color="rgba(255,255,255,0.6)", font_size="0.8rem"),
            rx.hstack(
                rx.text("$89",
                        style={"fontFamily": "'Playfair Display', serif",
                               "fontSize": "1.7rem", "fontWeight": "700",
                               "color": GOLD}),
                rx.text("por persona",
                        font_size="0.7rem", color="rgba(255,255,255,0.45)",
                        align_self="flex-end", margin_bottom="0.3rem"),
                rx.button(
                    "Reservar",
                    background="rgba(201,168,76,0.9)",
                    color=DARK, border="none",
                    padding="0.5rem 1.3rem", border_radius="20px",
                    font_weight="700", font_size="0.8rem",
                    cursor="pointer",
                ),
                spacing="3", align="end",
            ),
            spacing="3", align="start",
            position="relative", z_index="2",
            padding="1.5rem",
        ),
        position="relative",
        border_radius="20px",
        overflow="hidden",
        style={"background": "linear-gradient(135deg,#2A1800,#5C3800,#8B5E00)"},
        min_height="320px",
        display="flex",
        align="end",
        border=f"1px solid rgba(201,168,76,0.2)",
        **CARD_HOVER,
    )


def buggy_side_card(label: str, name: str, location: str,
                    price: str, bg: str) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(label, font_size="0.63rem", text_transform="uppercase",
                    letter_spacing="1px", color="rgba(255,255,255,0.45)"),
            rx.text(name, font_weight="600", font_size="0.9rem", color="white"),
            rx.text(location, font_size="0.7rem",
                    color="rgba(255,255,255,0.45)"),
            rx.text(price, color=GOLD, font_weight="700"),
            spacing="2", align="start",
            position="relative", z_index="2",
        ),
        border_radius="16px",
        overflow="hidden",
        style={"background": bg},
        display="flex",
        align="end",
        padding="1rem",
        border="1px solid rgba(255,255,255,0.09)",
        min_height="320px",
        cursor="pointer",
        transition="transform 0.25s",
        _hover={"transform": "translateY(-4px)"},
    )


def tours_section() -> rx.Component:
    return rx.box(
        section_header("🏎 Aventura extrema", "Tours Extremos", "en Buggy"),
        rx.grid(
            buggy_main_card(),
            buggy_side_card(
                "Tour Ecológico", "Buggy Cenotes",
                "Cancún · 6 horas", "$79 / persona",
                "linear-gradient(135deg,#1A3A2A,#2D6A4A)",
            ),
            buggy_side_card(
                "Aventura Nocturna", "Buggy Night Tour",
                "Punta Cana · 4 horas", "$65 / persona",
                "linear-gradient(135deg,#3A1A00,#8B4500)",
            ),
            style={"gridTemplateColumns": "2fr 1fr 1fr"},
            gap="1rem",
            max_width="1100px",
            margin="0 auto",
        ),
        id="tours",
        padding="4rem 2rem",
        width="100%",
    )


# ─────────────────────────────────────────────────────────────────────────────
#  RESORTS PREMIUM
# ─────────────────────────────────────────────────────────────────────────────

RESORTS = [
    {
        "name":     "Sanctuary Cap Cana",
        "location": "Cap Cana, Rep. Dominicana",
        "score":    "9.8  Excepcional",
        "price":    "$420",
        "type":     "All-Inclusive",
        "amenities":["🏊 Infinity Pool", "🍽 Gourmet"],
        "bg":       "linear-gradient(160deg,#0B3E3E,#1A6E6E,#0B2E4E)",
    },
    {
        "name":     "Hard Rock Cancún",
        "location": "Zona Hotelera, Cancún",
        "score":    "9.5  Excepcional",
        "price":    "$380",
        "type":     "All-Inclusive",
        "amenities":["🎰 Casino", "🎵 Shows"],
        "bg":       "linear-gradient(160deg,#2A1800,#6B4500,#1A0B00)",
    },
    {
        "name":     "Dorado Beach, Ritz-Carlton",
        "location": "Dorado, Puerto Rico",
        "score":    "9.9  Excepcional",
        "price":    "$850",
        "type":     "Ultra Premium",
        "amenities":["⛳ Golf", "🧖 Spa"],
        "bg":       "linear-gradient(160deg,#0B1A3E,#1A3A8A,#0B0E2A)",
    },
]


def resort_card(resort: dict) -> rx.Component:
    return rx.box(
        # Imagen / fondo
        rx.box(
            rx.hstack(
                *[
                    rx.box(
                        rx.text(a, font_size="0.6rem", color="white"),
                        background="rgba(0,0,0,0.68)",
                        style={"backdropFilter": "blur(8px)"},
                        padding="3px 8px",
                        border_radius="10px",
                        border="1px solid rgba(255,255,255,0.18)",
                    )
                    for a in resort["amenities"]
                ],
                position="absolute", top="10px", left="10px",
                spacing="1",
            ),
            style={"background": resort["bg"]},
            height="180px",
            position="relative",
        ),
        # Cuerpo
        rx.vstack(
            rx.text(resort["name"], font_weight="600", font_size="0.94rem",
                    color="white"),
            rx.text(f"📍  {resort['location']}", font_size="0.73rem",
                    color="rgba(255,255,255,0.48)"),
            rx.hstack(
                rx.text("★★★★★", color=GOLD, font_size="0.7rem"),
                rx.box(
                    rx.text(resort["score"], font_size="0.68rem",
                            font_weight="600", color="white"),
                    background=TEAL, padding="2px 8px", border_radius="8px",
                ),
                spacing="2", align="center",
            ),
            rx.hstack(
                rx.text(resort["price"],
                        style={"fontFamily": "'Playfair Display', serif",
                               "fontSize": "1.25rem", "fontWeight": "700",
                               "color": GOLD}),
                rx.text(f"/ noche · {resort['type']}",
                        font_size="0.63rem",
                        color="rgba(255,255,255,0.38)",
                        align_self="flex-end",
                        margin_bottom="2px"),
                spacing="1",
                align="end",
            ),
            spacing="2",
            align="start",
            padding="1rem",
        ),
        background="rgba(255,255,255,0.04)",
        border="1px solid rgba(255,255,255,0.09)",
        border_radius="18px",
        overflow="hidden",
        transition="transform 0.3s",
        _hover={"transform": "translateY(-6px)"},
        cursor="pointer",
    )


def resorts_section() -> rx.Component:
    return rx.box(
        section_header("👑 Lujo absoluto", "Resorts", "Premium"),
        rx.grid(
            *[resort_card(r) for r in RESORTS],
            style={"gridTemplateColumns": "repeat(auto-fit, minmax(270px, 1fr))"},
            gap="1.25rem",
            max_width="1100px",
            margin="0 auto",
        ),
        id="resorts",
        padding="4rem 2rem",
        background="rgba(0,0,0,0.18)",
        border_top="1px solid rgba(255,255,255,0.06)",
        width="100%",
    )


# ─────────────────────────────────────────────────────────────────────────────
#  FOOTER
# ─────────────────────────────────────────────────────────────────────────────

def footer_col(title: str, links: list[str]) -> rx.Component:
    return rx.vstack(
        rx.text(title, font_size="0.72rem", text_transform="uppercase",
                letter_spacing="1.5px", color=GOLD, font_weight="600"),
        *[
            rx.text(
                lnk,
                font_size="0.78rem",
                color="rgba(255,255,255,0.42)",
                cursor="pointer",
                _hover={"color": "white"},
                transition="color 0.2s",
            )
            for lnk in links
        ],
        spacing="3",
        align="start",
    )


def footer() -> rx.Component:
    return rx.box(
        # Filas principales
        rx.grid(
            # Marca
            rx.vstack(
                rx.text(
                    "TravelWorld",
                    style={
                        "fontFamily": "'Playfair Display', serif",
                        "fontSize": "1.3rem",
                        "fontWeight": "900",
                        "background": f"linear-gradient(135deg, {GOLD}, {GOLD_LT})",
                        "WebkitBackgroundClip": "text",
                        "WebkitTextFillColor": "transparent",
                        "backgroundClip": "text",
                        "letterSpacing": "2px",
                    },
                ),
                rx.text(
                    "La plataforma turística premium del Caribe y las Américas. "
                    "Conectamos viajeros con experiencias inolvidables.",
                    font_size="0.78rem",
                    color="rgba(255,255,255,0.4)",
                    line_height="1.7",
                    max_width="240px",
                    margin_top="0.5rem",
                ),
                spacing="2",
                align="start",
            ),
            footer_col("Destinos", [
                "Punta Cana", "Cancún", "Puerto Rico",
                "Colombia", "Orlando",
            ]),
            footer_col("Servicios", [
                "Vuelos + Hotel", "Tours & Excursiones",
                "Traslados", "Seguros de viaje", "Grupos",
            ]),
            footer_col("Empresa", [
                "Sobre nosotros", "Trabaja con nosotros",
                "Blog de viajes", "Afiliados", "Contacto",
            ]),
            style={"gridTemplateColumns": "2fr 1fr 1fr 1fr"},
            gap="2rem",
            max_width="1100px",
            margin="0 auto",
            padding_bottom="2rem",
            border_bottom="1px solid rgba(255,255,255,0.07)",
        ),
        # Barra inferior
        rx.hstack(
            rx.text(
                "© 2024 TravelWorld. Todos los derechos reservados. · Términos · Privacidad",
                font_size="0.7rem",
                color="rgba(255,255,255,0.28)",
            ),
            rx.spacer(),
            rx.hstack(
                *[
                    rx.box(
                        rx.text(s, font_size="0.68rem",
                                color="rgba(255,255,255,0.48)"),
                        width="32px", height="32px",
                        border_radius="50%",
                        background="rgba(255,255,255,0.06)",
                        border="1px solid rgba(255,255,255,0.12)",
                        display="flex",
                        align="center",
                        justify="center",
                        cursor="pointer",
                        _hover={
                            "background": "rgba(201,168,76,0.2)",
                            "border_color": GOLD,
                        },
                        transition="all 0.2s",
                    )
                    for s in ["ig", "fb", "tw", "yt"]
                ],
                spacing="2",
            ),
            max_width="1100px",
            margin="1.5rem auto 0",
            width="100%",
            flex_wrap="wrap",
            gap="1rem",
        ),
        padding="3rem 2rem 1.5rem",
        background="#060F18",
        border_top=f"1px solid {GOLD_BOR}",
        width="100%",
    )


# ─────────────────────────────────────────────────────────────────────────────
#  CSS GLOBAL (fuentes + animaciones)
# ─────────────────────────────────────────────────────────────────────────────

GLOBAL_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500;600&display=swap');

*, *::before, *::after { box-sizing: border-box; }

body {
    background-color: #0D1B2A;
    color: white;
    font-family: 'DM Sans', sans-serif;
    margin: 0;
    overflow-x: hidden;
}

@keyframes fadeInDown {
    from { opacity: 0; transform: translateY(-20px); }
    to   { opacity: 1; transform: translateY(0); }
}

@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(30px); }
    to   { opacity: 1; transform: translateY(0); }
}

@keyframes float {
    0%, 100% { transform: translateY(0); }
    50%       { transform: translateY(-12px); }
}

/* Scrollbar estilizado */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #0D1B2A; }
::-webkit-scrollbar-thumb { background: #C9A84C; border-radius: 3px; }
"""


# ─────────────────────────────────────────────────────────────────────────────
#  PÁGINA PRINCIPAL
# ─────────────────────────────────────────────────────────────────────────────

def index() -> rx.Component:
    return rx.box(
        # CSS global
        rx.html(f"<style>{GLOBAL_CSS}</style>"),
        # Componentes
        navbar(),
        hero_section(),
        stats_bar(),
        destinations_section(),
        offers_section(),
        disney_section(),
        tours_section(),
        resorts_section(),
        footer(),
        width="100%",
        background=DARK,
        min_height="100vh",
    )
