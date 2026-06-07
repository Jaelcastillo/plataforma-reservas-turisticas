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
from turismo_reservas.states.auth_state import AuthState
from turismo_reservas.pages.reservas import CheckoutState
from turismo_reservas.pages.reservas import CheckoutState

# ─── Paleta de colores ────────────────────────────────────────────────────────
DARK = "#1F2A35"
CREAM = "#F5EFE6"
BEIGE = "#E8DDCF"
TEXT_DARK = "#1B1B1B"
TEXT_SOFT = "#5E554D"
TEAL = "#0B6E6E"
TEAL_LT = "#1A9E9E"
GOLD = "#C9A84C"
GOLD_LT = "#F0D080"
CORAL = "#C9785B"
PURPLE = "#8B6FC7"
GLASS_BG = "rgba(255,255,255,0.16)"
GLASS_BOR = "rgba(255,255,255,0.28)"
GOLD_BOR = "rgba(201,168,76,0.35)"

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
    nav_links = rx.hstack(
        rx.link("Destinos", href="#destinos", style=NAV_LINK),
        rx.link("Ofertas", href="#ofertas", style=NAV_LINK),
        rx.link("Resorts", href="#resorts", style=NAV_LINK),
        rx.link("Tours", href="#tours", style=NAV_LINK),
        rx.link("Disney", href="#disney", style=NAV_LINK),
        spacing="7",
        align="center",
        margin_left="160px",
    )

    logged_buttons = rx.hstack(
       rx.link(
    rx.button(
        "👤 " + AuthState.nombre,
        background="white",
        color=TEXT_DARK,
        border=f"1px solid {GOLD_BOR}",
        padding="0.5rem 1rem",
        border_radius="25px",
        font_weight="700",
        font_size="0.8rem",
        cursor="pointer",
    ),
    href=rx.cond(
        AuthState.es_admin,
        "/admin/dashboard",
        "/mis-reservas",
    ),
),
        rx.button(
            "Cerrar sesión",
            on_click=AuthState.logout,
            background="transparent",
            color=TEXT_DARK,
            border=f"1px solid {GOLD_BOR}",
            padding="0.5rem 1rem",
            border_radius="25px",
            font_weight="700",
            font_size="0.8rem",
            cursor="pointer",
        ),
        rx.link(
            rx.button(
                "Reservar Ahora",
                background=f"linear-gradient(135deg, {GOLD}, {GOLD_LT})",
                color=DARK,
                border="none",
                padding="0.5rem 1.4rem",
                border_radius="25px",
                font_weight="700",
                font_size="0.8rem",
                cursor="pointer",
            ),
            href="/reservas",
        ),
        spacing="3",
        align="center",
    )

    guest_buttons = rx.hstack(
        rx.link(
            rx.button(
                "Iniciar sesión",
                background="transparent",
                color=TEXT_DARK,
                border=f"1px solid {GOLD_BOR}",
                padding="0.5rem 1rem",
                border_radius="25px",
                font_weight="700",
                font_size="0.8rem",
                cursor="pointer",
            ),
            href="/login",
        ),
        rx.link(
            rx.button(
                "Registrarse",
                background="white",
                color=TEXT_DARK,
                border=f"1px solid {GOLD_BOR}",
                padding="0.5rem 1rem",
                border_radius="25px",
                font_weight="700",
                font_size="0.8rem",
                cursor="pointer",
            ),
            href="/registro",
        ),
        rx.link(
            rx.button(
                "Reservar Ahora",
                background=f"linear-gradient(135deg, {GOLD}, {GOLD_LT})",
                color=DARK,
                border="none",
                padding="0.5rem 1.4rem",
                border_radius="25px",
                font_weight="700",
                font_size="0.8rem",
                cursor="pointer",
            ),
            href="/reservas",
        ),
        spacing="3",
        align="center",
    )

    return rx.box(
        rx.hstack(
            rx.text(
                "TravelWorld",
                style={
                    "fontFamily": "'Playfair Display', serif",
                    "fontSize": "1.5rem",
                    "fontWeight": "900",
                    "background": "linear-gradient(135deg, #8B6A2E, #C9A84C, #A8753B)",
                    "WebkitBackgroundClip": "text",
                    "WebkitTextFillColor": "transparent",
                    "backgroundClip": "text",
                    "letterSpacing": "2px",
                    "cursor": "pointer",
                },
            ),
            nav_links,
            rx.spacer(),
            rx.cond(AuthState.esta_logueado, logged_buttons, guest_buttons),
            width="100%",
            align="center",
            max_width="1280px",
            margin="0 auto",
            padding="0 1rem",
        ),
        position="sticky",
        top="0",
        z_index="100",
        background="rgba(245,239,230,0.72)",
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

def date_search_field(label: str, input_id: str) -> rx.Component:
    return rx.vstack(
        rx.text(
            label,
            font_size="0.62rem",
            text_transform="uppercase",
            letter_spacing="1.2px",
            color=GOLD,
            font_weight="700",
        ),
        rx.input(
            id=input_id,
            type="date",
            read_only=True,
            on_focus=rx.call_script(f"document.getElementById('{input_id}').showPicker()"),
            on_click=rx.call_script(f"document.getElementById('{input_id}').showPicker()"),
            background="transparent",
            border="none",
            border_bottom="1px solid rgba(255,255,255,0.2)",
            border_radius="0",
            color="white",
            font_size="0.88rem",
            padding="0.3rem 0",
            width="100%",
            cursor="pointer",
        ),
        spacing="1",
        flex="1",
        min_width="110px",
    )


def hero_section() -> rx.Component:
    return rx.box(
        rx.html(
            """
            <video class="autoVideo" autoplay muted loop playsinline preload="auto"
            style="position:absolute;top:0;left:0;width:100%;height:100%;object-fit:cover;z-index:0;">
                <source src="/images/beach_video.mp4?v=1000" type="video/mp4">
            </video>

            <script>
                document.querySelectorAll(".autoVideo").forEach((video) => {
                    video.muted = true;
                    video.setAttribute("muted", "");
                    video.setAttribute("playsinline", "");
                    video.play().catch(() => {});
                });
            </script>
            """
        ),

        rx.box(
            position="absolute",
            inset="0",
            background="rgba(0,0,0,0.45)",
            z_index="1",
        ),

        rx.box(
            position="absolute",
            bottom="0",
            left="0",
            right="0",
            height="140px",
            style={
                "background": "linear-gradient(180deg, transparent 0%, rgba(13,27,42,0.85) 100%)"
            },
            z_index="1",
        ),

        rx.vstack(
            rx.box(
                rx.text(
                    " Plataforma Premium de Viajes ",
                    font_size="0.72rem",
                    font_weight="600",
                    letter_spacing="1.5px",
                ),
                background="rgba(201,168,76,0.12)",
                border="1px solid rgba(201,168,76,0.4)",
                color=GOLD,
                padding="0.4rem 1.3rem",
                border_radius="25px",
                style={"animation": "fadeInDown 0.8s ease both"},
            ),

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
                gold_gradient_text(
                    "Sin Límites",
                    size="clamp(3rem, 7vw, 5rem)",
                ),
                spacing="1",
                align="center",
                style={"animation": "fadeInUp 0.9s ease 0.1s both"},
            ),

            rx.text(
                "Destinos únicos, resorts de lujo, tours extremos y experiencias mágicas. "
                "Tu aventura perfecta comienza aquí.",
                color="#F8F1E7",
                font_size="1.05rem",
                text_align="center",
                max_width="520px",
                line_height="1.75",
                style={"animation": "fadeInUp 0.9s ease 0.2s both"},
            ),

            rx.box(
                rx.hstack(
                    rx.text(
                        "✈️ Explora más destinos exclusivos",
                        color="white",
                        font_size="1rem",
                        font_weight="800",
                    ),

                    rx.spacer(),

                    rx.link(
                        rx.button(
                            "Reservar ahora",
                            background=f"linear-gradient(135deg, {CORAL}, {GOLD})",
                            color="white",
                            border="none",
                            border_radius="999px",
                            padding="0.8rem 1.8rem",
                            font_weight="900",
                            cursor="pointer",
                        ),
                        href="/reservas",
                    ),

                    spacing="4",
                    align="center",
                    width="100%",
                    flex_wrap="wrap",
                ),

                background="rgba(255,255,255,0.12)",
                style={
                    "backdropFilter": "blur(18px)",
                    "animation": "fadeInUp 0.9s ease 0.3s both",
                },
                border="1px solid rgba(255,255,255,0.2)",
                border_radius="20px",
                padding="1rem 1.5rem",
                max_width="700px",
                width="100%",
                box_shadow="0 18px 45px rgba(0,0,0,0.35)",
            ),

            spacing="7",
            align="center",
            justify="center",
            position="relative",
            z_index="2",
            padding="0 1.5rem",
            max_width="860px",
            text_align="center",
            margin="0 auto",
        ),

        position="relative",
        min_height="100vh",
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


def stats_section() -> rx.Component:
    stats = [
        ("1,200+", "DESTINOS DISPONIBLES"),
        ("98%", "CLIENTES SATISFECHOS"),
        ("50K+", "RESERVAS REALIZADAS"),
        ("24/7", "SOPORTE PREMIUM"),
    ]

    return rx.box(

        # Glow elegante detrás
        rx.box(
            position="absolute",
            top="-120px",
            left="50%",
            transform="translateX(-50%)",
            width="700px",
            height="250px",
            background="radial-gradient(circle, rgba(212,175,55,0.18) 0%, transparent 70%)",
            filter="blur(70px)",
        ),

        rx.hstack(
            *[
                rx.vstack(
                    rx.heading(
                        num,
                        color="#D4AF37",
                        font_size="2.3rem",
                        font_weight="700",
                        font_family="'Playfair Display', serif",
                    ),

                    rx.text(
                        label,
                        color="rgba(255,255,255,0.75)",
                        font_size="0.85rem",
                        letter_spacing="3px",
                        text_align="center",
                    ),

                    spacing="1",
                    align="center",
                )

                for num, label in stats
            ],

            justify="between",
            align="center",
            width="100%",
            flex_wrap="wrap",
        ),

        position="relative",

        background="""
        linear-gradient(
            135deg,
            rgba(7,24,38,0.96),
            rgba(11,38,53,0.94),
            rgba(8,28,43,0.97)
        )
        """,

        border_top="1px solid rgba(212,175,55,0.18)",
        border_bottom="1px solid rgba(212,175,55,0.18)",

        padding="2rem 4rem",
        width="100%",
        overflow="hidden",
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

def destination_card_db(dest) -> rx.Component:
    return rx.box(
        rx.image(
            src=dest["imagen"],
            width="100%",
            height="100%",
            object_fit="cover",
            position="absolute",
            inset="0",
        ),

        rx.box(
            position="absolute",
            inset="0",
            style={
                "background": "linear-gradient(180deg, transparent 35%, rgba(0,0,0,0.88) 100%)"
            },
        ),

        rx.box(
            rx.box(
                rx.text(
                    "⭐ DESTACADO",
                    font_size="0.6rem",
                    font_weight="700",
                    color=DARK,
                    letter_spacing="0.5px",
                    text_transform="uppercase",
                ),
                background="rgba(201,168,76,0.92)",
                padding="3px 10px",
                border_radius="20px",
                display="inline-block",
                margin_bottom="0.5rem",
            ),
            rx.heading(
                dest["ciudad"],
                style={
                    "fontFamily": "'Playfair Display', serif",
                    "fontSize": "1.2rem",
                    "fontWeight": "700",
                    "color": "white",
                    "lineHeight": "1.2",
                },
            ),
            rx.text(
                dest["pais"],
                font_size="0.72rem",
                color="rgba(255,255,255,0.75)",
                margin_top="2px",
            ),
            rx.text(
                dest["titulo"],
                font_size="0.78rem",
                color=GOLD,
                font_weight="700",
                margin_top="0.5rem",
            ),
            position="absolute",
            bottom="0",
            left="0",
            right="0",
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

        rx.html("""
<video id="worldVideo" autoplay muted loop playsinline preload="auto"
    style="
        position:absolute;
        top:0;
        left:0;
        width:100%;
        height:100%;
        object-fit:cover;
        z-index:0;
    ">
    <source src="/images/world_video.mp4?v=1" type="video/mp4">
</video>

<script>
window.addEventListener("load", () => {
    const v = document.getElementById("worldVideo");
    if(v){
        v.muted = true;
        v.play().catch(err => console.log(err));
    }
});
</script>
"""),

        # OVERLAY OSCURO
        rx.box(
            position="absolute",
            inset="0",
            background="""
            linear-gradient(
                rgba(5,15,25,0.82),
                rgba(5,15,25,0.88)
            )
            """,
            z_index="1",
        ),

        # CONTENIDO
        rx.box(

            section_header(
                "✦ Explora el mundo ✦",
                "Destinos",
                "Exclusivos"
            ),

            rx.cond(
    AuthState.destinos_destacados.length() > 0,
    rx.grid(
        rx.foreach(AuthState.destinos_destacados, destination_card_db),
        columns="5",
        spacing="4",
        max_width="1200px",
        margin="0 auto",
        style={
            "gridTemplateColumns": "repeat(auto-fit, minmax(210px, 1fr))"
        },
    ),
    rx.center(
        rx.text(
            "No hay destinos destacados todavía.",
            color="white",
            font_weight="800",
        ),
        padding="2rem",
    ),
),

            position="relative",
            z_index="2",
        ),

        id="destinos",

        padding="5rem 3rem",

        width="100%",

        position="relative",

        overflow="hidden",
    )


# ─────────────────────────────────────────────────────────────────────────────
#  OFERTAS DEL MOMENTO
# ─────────────────────────────────────────────────────────────────────────────

def offer_card_db(offer) -> rx.Component:
    return rx.box(
        rx.box(
            rx.image(
                src=offer["imagen"],
                width="100%",
                height="220px",
                object_fit="cover",
            ),
            rx.box(
                rx.text(
                    rx.fragment("-", offer["descuento"].to_string(), "% HOY"),
                    font_size="0.78rem",
                    font_weight="800",
                    color="white",
                ),
                position="absolute",
                top="14px",
                right="14px",
                background=f"linear-gradient(135deg, {CORAL}, {GOLD})",
                padding="6px 14px",
                border_radius="20px",
                z_index="2",
            ),
            height="220px",
            position="relative",
            overflow="hidden",
        ),

        rx.vstack(
            rx.text(offer["titulo"], font_weight="800", font_size="1.1rem", color="#2A2118"),
            rx.text(offer["categoria"], font_size="0.86rem", color="#6B5A45"),
            rx.text(rx.fragment("★★★★★ ", offer["rating"].to_string()), font_size="0.8rem", color=GOLD),

            rx.hstack(
                rx.vstack(
                    rx.text(
                        rx.fragment("$", offer["precio_anterior"].to_string(), " / persona"),
                        font_size="0.76rem",
                        color="#A99882",
                        text_decoration="line-through",
                    ),
                    rx.text(
                        rx.fragment("$", offer["precio"].to_string()),
                        style={
                            "fontFamily": "'Playfair Display', serif",
                            "fontSize": "1.8rem",
                            "fontWeight": "800",
                            "color": GOLD,
                        },
                    ),
                    rx.text(offer["duracion"], font_size="0.72rem", color="#7A6A55"),
                    spacing="0",
                    align="start",
                ),
                rx.spacer(),
                rx.text("¡Disponible!", font_size="0.78rem", font_weight="800", color=CORAL),
                width="100%",
                align="center",
            ),

            rx.link(
                rx.button(
                    "Reservar Ahora",
                    width="100%",
                    background=f"linear-gradient(135deg, {TEAL}, {TEAL_LT})",
                    color="white",
                    border="none",
                    border_radius="14px",
                    font_weight="800",
                    font_size="0.9rem",
                    padding="0.75rem",
                    cursor="pointer",
                ),
                href="/reservas",
                width="100%",
            ),

            spacing="3",
            padding="1.4rem",
            align="start",
            width="100%",
        ),

        min_width="360px",
        max_width="360px",
        background="rgba(255,255,255,0.78)",
        border="1px solid rgba(201,168,76,0.35)",
        border_radius="24px",
        overflow="hidden",
        box_shadow="0 20px 55px rgba(70,55,35,0.15)",
    )


def offers_section() -> rx.Component:
    return rx.box(
        section_header(
            "⚡ Tiempo limitado",
            "Ofertas del",
            "Momento",
        ),

        rx.box(
            rx.cond(
                AuthState.ofertas_publicas.length() > 0,
                rx.box(
                    rx.foreach(AuthState.ofertas_publicas, offer_card_db),
                    rx.foreach(AuthState.ofertas_publicas, offer_card_db),
                    class_name="offers-track",
                ),
                rx.center(
                    rx.text(
                        "No hay ofertas activas disponibles.",
                        color=TEXT_SOFT,
                        font_weight="800",
                    ),
                    padding="2rem",
                ),
            ),
            overflow="hidden",
            width="100%",
            position="relative",
        ),

        # 👇 BOTÓN NUEVO
        rx.center(
            rx.link(
                rx.button(
                    "Ver todas las ofertas →",
                    background=f"linear-gradient(135deg, {GOLD}, {GOLD_LT})",
                    color="#1B1B1B",
                    border="none",
                    border_radius="14px",
                    font_weight="800",
                    padding="0.9rem 1.8rem",
                    cursor="pointer",
                ),
                href="/ofertas",
            ),
            margin_top="2rem",
        ),

        id="ofertas",
        padding="5rem 2rem",
        background="""
            linear-gradient(
                180deg,
                rgba(245,240,232,0.98),
                rgba(239,232,220,1)
            )
        """,
        border_top="1px solid rgba(201,168,76,0.15)",
        width="100%",
    )
# ─────────────────────────────────────────────────────────────────────────────
#  SECCIÓN DISNEY
# ─────────────────────────────────────────────────────────────────────────────

DISNEY_PARKS = [
    {
        "name": "Magic Kingdom",
        "image": "url('/images/magic_kingdom.jpg') center/cover no-repeat",
    },
    {
        "name": "EPCOT",
        "image": "url('/images/epcot.jpg') center/cover no-repeat",
    },
    {
        "name": "Hollywood Studios",
        "image": "url('/images/hollywood_studios.jpg') center/cover no-repeat",
    },
    {
        "name": "Animal Kingdom",
        "image": "url('/images/animal_kingdom.jpg') center/cover no-repeat",
    },
]


DISNEY_FEATURES = [
    "Acceso a todos los 4 parques principales",
    "Hotel dentro del resort de Disney",
    "Traslados aeropuerto incluidos",
    "Desayuno con personajes de Disney",
    "Fast Pass y reservaciones prioritarias",
]


def disney_park_card(park: dict) -> rx.Component:
    return rx.box(
        rx.box(
            position="absolute",
            inset="0",
            background="linear-gradient(180deg, transparent 30%, rgba(0,0,0,0.85) 100%)",
            z_index="1",
        ),

        rx.text(
            park.get("name"),
            color="white",
            font_size="1rem",
            font_weight="700",
            position="absolute",
            bottom="1rem",
            left="0",
            right="0",
            text_align="center",
            z_index="2",
        ),

        style={
            "background": park.get("image"),
        },

        border_radius="18px",
        overflow="hidden",
        height="220px",
        position="relative",
        cursor="pointer",
        border="1px solid rgba(255,255,255,0.22)",

        _hover={
            "transform": "scale(1.04)",
            "box_shadow": "0 20px 50px rgba(0,0,0,0.4)",
        },

        transition="all 0.3s",
    )


def disney_section() -> rx.Component:
    return rx.box(
      rx.html(
    """
   <video id="disneyVideo" autoplay muted loop playsinline preload="auto"
    oncanplay="this.muted=true; this.play();"
    style="
        position:absolute;
        top:0;
        left:0;
        width:100%;
        height:100%;
        object-fit:cover;
        z-index:0;
    ">
    <source src="/images/disney_video.mp4?v=100" type="video/mp4">
</video>

    <script>
        const disneyVideo = document.getElementById("disneyVideo");
        if (disneyVideo) {
            disneyVideo.muted = true;
            disneyVideo.play().catch(() => {});
        }
    </script>
    """
),

        rx.box(
            position="absolute",
            inset="0",
            background="rgba(20, 10, 40, 0.72)",
            z_index="1",
        ),

        rx.grid(
            rx.vstack(
                rx.text(
                    "✦  La magia te espera  ✦",
                    color=GOLD,
                    font_size="0.75rem",
                    text_transform="uppercase",
                    letter_spacing="2px",
                    font_weight="700",
                ),

                rx.hstack(
                    rx.heading(
                        "Vive la Magia de ",
                        style={
                            "fontFamily": "'Playfair Display', serif",
                            "fontSize": "clamp(2rem,4vw,2.8rem)",
                            "fontWeight": "700",
                            "color": "white",
                        },
                    ),
                    rx.text(
                        "Disney World",
                        style={
                            "fontFamily": "'Playfair Display', serif",
                            "fontSize": "clamp(2rem,4vw,2.8rem)",
                            "fontWeight": "700",
                            "background": f"linear-gradient(135deg, {GOLD_LT}, {GOLD}, {CORAL})",
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
                    color="rgba(255,255,255,0.86)",
                    font_size="1rem",
                    line_height="1.8",
                    max_width="480px",
                ),

                rx.vstack(
                    *[
                        rx.hstack(
                            rx.text("✦", color=GOLD, font_size="0.8rem"),
                            rx.text(
                                feat,
                                font_size="0.95rem",
                                color="rgba(255,255,255,0.92)",
                            ),
                            spacing="2",
                            align="center",
                        )
                        for feat in DISNEY_FEATURES
                    ],
                    spacing="3",
                    align="start",
                ),

                
rx.button(
    "Ver Paquetes Disney ✨",
    background=f"linear-gradient(135deg, {GOLD}, {CORAL})",
    color="white",
    border="none",
    padding="0.8rem 2.2rem",
    border_radius="30px",
    font_weight="800",
    font_size="0.95rem",
    letter_spacing="0.5px",
    cursor="pointer",
    box_shadow="0 12px 30px rgba(0,0,0,0.35)",
    _hover={
        "opacity": "0.92",
        "transform": "translateY(-2px)",
    },
    transition="all 0.2s",
    on_click=CheckoutState.ir_disney,
),

                spacing="5",
                align="start",
                position="relative",
                z_index="2",
            ),

            rx.grid(
                *[disney_park_card(park) for park in DISNEY_PARKS],
                columns="2",
                gap="0.9rem",
                position="relative",
                z_index="2",
            ),

            columns="2",
            gap="3rem",
            align="center",
            max_width="1100px",
            margin="0 auto",
            position="relative",
            z_index="2",
        ),

        id="disney",
        padding="5rem 2rem",
        border_top=f"1px solid {GOLD_BOR}",
        border_bottom=f"1px solid {GOLD_BOR}",
        width="100%",
        position="relative",
        overflow="hidden",
        min_height="650px",
    )

# ─────────────────────────────────────────────────────────────────────────────
#  TOURS BUGGY
# ─────────────────────────────────────────────────────────────────────────────

class BuggyState(rx.State):
    selected: int = 1

    def select_buggy(self, index: int):
        self.selected = index


BUGGY_TOURS = [
    {
        "label": "Tour Ecológico",
        "name": "Buggy Cenotes",
        "location": "Cancún · 6 horas",
        "price": "$79 / persona",
        "image": "buggy_cenotes.jpg",
        "action": "cancun",
    },
    {
        "label": "Más Vendido",
        "name": "Safari Buggy Punta Cana",
        "location": "Punta Cana · 8 horas · Todo incluido",
        "price": "$89 / persona",
        "image": "buggy_punta_cana.jpg",
        "action": "punta_cana",
    },
    {
        "label": "Aventura Nocturna",
        "name": "Buggy Night Tour",
        "location": "Punta Cana · 4 horas",
        "price": "$65 / persona",
        "image": "buggy_night.jpg",
        "action": "punta_cana",
    },
]


def buggy_reserva_button(tour: dict) -> rx.Component:
    return rx.cond(
        tour["action"] == "cancun",
        rx.button(
            "Reservar ahora",
            background=f"linear-gradient(135deg, {GOLD}, {GOLD_LT})",
            color="#1F2A35",
            border="none",
            padding="0.7rem 1.7rem",
            border_radius="26px",
            font_weight="900",
            cursor="pointer",
            on_click=CheckoutState.ir_cancun,
        ),
        rx.button(
            "Reservar ahora",
            background=f"linear-gradient(135deg, {GOLD}, {GOLD_LT})",
            color="#1F2A35",
            border="none",
            padding="0.7rem 1.7rem",
            border_radius="26px",
            font_weight="900",
            cursor="pointer",
            on_click=CheckoutState.ir_punta_cana,
        ),
    )


def buggy_tour_card(tour: dict, index: int) -> rx.Component:
    is_selected = BuggyState.selected == index

    return rx.box(
        rx.box(
            position="absolute",
            inset="0",
            background=rx.cond(
                is_selected,
                "linear-gradient(180deg, rgba(0,0,0,0.08) 15%, rgba(0,0,0,0.72) 100%)",
                "linear-gradient(180deg, rgba(0,0,0,0.18) 15%, rgba(0,0,0,0.82) 100%)",
            ),
            z_index="1",
        ),

        rx.vstack(
            rx.box(
                rx.text(
                    tour["label"].upper(),
                    font_size="0.72rem",
                    font_weight="800",
                    color="white",
                    letter_spacing="1px",
                ),
                background=f"linear-gradient(135deg, {CORAL}, {GOLD})",
                padding="6px 14px",
                border_radius="20px",
            ),

            rx.heading(
                tour["name"],
                style={
                    "fontFamily": "'Playfair Display', serif",
                    "fontSize": rx.cond(is_selected, "2.35rem", "1.35rem"),
                    "fontWeight": "800",
                    "color": "white",
                    "lineHeight": "1.1",
                },
            ),

            rx.text(
                tour["location"],
                color="rgba(255,255,255,0.9)",
                font_size=rx.cond(is_selected, "1rem", "0.86rem"),
            ),

            rx.text(
                tour["price"],
                color=GOLD,
                font_weight="900",
                font_size=rx.cond(is_selected, "1.65rem", "1.15rem"),
            ),

            rx.cond(
                is_selected,
                buggy_reserva_button(tour),
                rx.box(),
            ),

            spacing="3",
            align="start",
            position="relative",
            z_index="2",
            padding=rx.cond(is_selected, "2rem", "1.4rem"),
        ),

        background=f"url('/images/{tour['image']}') center/cover no-repeat",
        border_radius="30px",
        overflow="hidden",
        position="relative",
        height=rx.cond(is_selected, "430px", "340px"),
        width="100%",
        display="flex",
        align="end",
        border=rx.cond(
            is_selected,
            "2px solid rgba(201,168,76,0.7)",
            "1px solid rgba(255,255,255,0.18)",
        ),
        box_shadow=rx.cond(
            is_selected,
            "0 30px 90px rgba(0,0,0,0.55)",
            "0 18px 45px rgba(0,0,0,0.28)",
        ),
        transform=rx.cond(is_selected, "scale(1.04)", "scale(0.92)"),
        transition="all 0.35s ease",
        cursor="pointer",
        on_click=lambda: BuggyState.select_buggy(index),
    )


def tours_section() -> rx.Component:
    return rx.box(
        rx.box(
            position="absolute",
            inset="0",
            background="""
            linear-gradient(
                rgba(8,16,24,0.58),
                rgba(8,16,24,0.78)
            ),
            url('/images/buggy_bg.jpg') center/cover no-repeat
            """,
            z_index="0",
        ),

        rx.box(
            section_header("🏎 Aventura extrema", "Tours Extremos", "en Buggy"),

            rx.grid(
                buggy_tour_card(BUGGY_TOURS[0], 0),
                buggy_tour_card(BUGGY_TOURS[1], 1),
                buggy_tour_card(BUGGY_TOURS[2], 2),
                style={
                    "gridTemplateColumns": "0.8fr 1.35fr 0.8fr",
                    "alignItems": "center",
                },
                gap="1.4rem",
                max_width="1250px",
                margin="0 auto",
            ),

            position="relative",
            z_index="2",
        ),

        id="tours",
        padding="5rem 2rem",
        width="100%",
        position="relative",
        overflow="hidden",
    )
# ─────────────────────────────────────────────────────────────────────────────
#  RESORTS PREMIUM
# ─────────────────────────────────────────────────────────────────────────────

RESORTS = [
    {
        "name": "Sanctuary Cap Cana",
        "location": "Cap Cana, Rep. Dominicana",
        "score": "9.8 Excepcional",
        "price": "$420",
        "type": "All-Inclusive",
        "amenities": ["🏊 Infinity Pool", "🍽 Gourmet"],
        "image": "url('/images/resort_cap_cana.jpg') center/cover no-repeat",
        "action": "cap_cana",
    },
    {
        "name": "Hard Rock Cancún",
        "location": "Zona Hotelera, Cancún",
        "score": "9.5 Excepcional",
        "price": "$380",
        "type": "All-Inclusive",
        "amenities": ["🎰 Casino", "🎵 Shows"],
        "image": "url('/images/resort_hardrock.jpg') center/cover no-repeat",
        "action": "cancun",
    },
    {
        "name": "Dorado Beach, Ritz-Carlton",
        "location": "Dorado, Puerto Rico",
        "score": "9.9 Excepcional",
        "price": "$850",
        "type": "Ultra Premium",
        "amenities": ["⛳ Golf", "🧖 Spa"],
        "image": "url('/images/resort_ritz.jpg') center/cover no-repeat",
        "action": "puerto_rico",
    },
]


def resort_reserva_button(resort: dict) -> rx.Component:
    return rx.cond(
        resort["action"] == "cap_cana",
        rx.button(
            "Ver disponibilidad",
            width="100%",
            background=f"linear-gradient(135deg, {GOLD}, {CORAL})",
            color="white",
            border="none",
            border_radius="14px",
            padding="0.75rem",
            font_weight="800",
            cursor="pointer",
            on_click=CheckoutState.ir_cap_cana,
        ),
        rx.cond(
            resort["action"] == "cancun",
            rx.button(
                "Ver disponibilidad",
                width="100%",
                background=f"linear-gradient(135deg, {GOLD}, {CORAL})",
                color="white",
                border="none",
                border_radius="14px",
                padding="0.75rem",
                font_weight="800",
                cursor="pointer",
                on_click=CheckoutState.ir_resort_cancun,
            ),
            rx.button(
                "Ver disponibilidad",
                width="100%",
                background=f"linear-gradient(135deg, {GOLD}, {CORAL})",
                color="white",
                border="none",
                border_radius="14px",
                padding="0.75rem",
                font_weight="800",
                cursor="pointer",
                on_click=CheckoutState.ir_dorado_pr,
            ),
        ),
    )


def resort_card(resort: dict) -> rx.Component:
    return rx.box(
        rx.box(
            rx.hstack(
                *[
                    rx.box(
                        rx.text(a, font_size="0.7rem", color="white"),
                        background="rgba(0,0,0,0.55)",
                        padding="5px 10px",
                        border_radius="999px",
                        border="1px solid rgba(255,255,255,0.25)",
                    )
                    for a in resort["amenities"]
                ],
                position="absolute",
                top="14px",
                left="14px",
                spacing="2",
                z_index="2",
            ),

            rx.box(
                position="absolute",
                inset="0",
                background="linear-gradient(180deg, transparent 35%, rgba(0,0,0,0.82) 100%)",
                z_index="1",
            ),

            rx.vstack(
                rx.text(
                    resort["name"],
                    font_weight="800",
                    font_size="1.25rem",
                    color="white",
                ),
                rx.text(
                    f"📍 {resort['location']}",
                    font_size="0.82rem",
                    color="rgba(255,255,255,0.78)",
                ),
                position="absolute",
                bottom="16px",
                left="18px",
                right="18px",
                spacing="1",
                z_index="2",
                align="start",
            ),

            background=resort["image"],
            height="260px",
            position="relative",
            overflow="hidden",
        ),

        rx.vstack(
            rx.hstack(
                rx.text("★★★★★", color=GOLD, font_size="0.85rem"),
                rx.box(
                    rx.text(
                        resort["score"],
                        font_size="0.75rem",
                        font_weight="800",
                        color="white",
                    ),
                    background=TEAL,
                    padding="3px 10px",
                    border_radius="999px",
                ),
                spacing="2",
                align="center",
            ),

            rx.hstack(
                rx.text(
                    resort["price"],
                    style={
                        "fontFamily": "'Playfair Display', serif",
                        "fontSize": "2rem",
                        "fontWeight": "800",
                        "color": GOLD,
                    },
                ),
                rx.text(
                    f"/ noche · {resort['type']}",
                    font_size="0.78rem",
                    color="#D8C7B0",
                    align_self="end",
                    margin_bottom="0.35rem",
                ),
                spacing="1",
                align="end",
            ),

            resort_reserva_button(resort),

            spacing="3",
            padding="1.3rem",
            align="start",
        ),

        background="rgba(255,255,255,0.08)",
        border="1px solid rgba(255,255,255,0.12)",
        border_radius="24px",
        overflow="hidden",
        box_shadow="0 20px 60px rgba(0,0,0,0.35)",
        transition="all 0.3s",
        _hover={
            "transform": "translateY(-10px)",
            "box_shadow": "0 32px 80px rgba(0,0,0,0.5)",
        },
    )


def resorts_section() -> rx.Component:
    return rx.box(
        rx.box(
            position="absolute",
            inset="0",
            background="""
            linear-gradient(
                rgba(10,18,25,0.82),
                rgba(10,18,25,0.90)
            ),
            url('/images/resort_bg.jpg') center/cover no-repeat
            """,
            z_index="0",
        ),

        rx.box(
            section_header("👑 Lujo absoluto", "Resorts", "Premium"),

            rx.grid(
                *[resort_card(r) for r in RESORTS],
                style={
                    "gridTemplateColumns": "repeat(auto-fit, minmax(300px, 1fr))"
                },
                gap="1.5rem",
                max_width="1200px",
                margin="0 auto",
            ),

            position="relative",
            z_index="2",
        ),

        id="resorts",
        padding="5rem 2rem",
        width="100%",
        position="relative",
        overflow="hidden",
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

@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Inter:wght@300;400;500;600;700;800&display=swap');

html {
    scroll-behavior: smooth;
}

body {
    margin: 0;
    padding: 0;
    overflow-x: hidden;
    background: #F5EFE6;
    color: #1F1F1F;
    font-family: 'Inter', sans-serif;
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 10px;
}

::-webkit-scrollbar-track {
    background: #EFE6D8;
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(
        180deg,
        #C9A84C,
        #A67C2E
    );
    border-radius: 20px;
}

/* Selección de texto */
::selection {
    background: rgba(201,168,76,0.28);
}

/* Animaciones */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(45px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes fadeInDown {
    from {
        opacity: 0;
        transform: translateY(-45px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes glowPulse {
    0% {
        box-shadow: 0 0 0 rgba(201,168,76,0.0);
    }

    50% {
        box-shadow: 0 0 35px rgba(201,168,76,0.35);
    }

    100% {
        box-shadow: 0 0 0 rgba(201,168,76,0.0);
    }
}

/* Carrusel ofertas */
@keyframes offersScroll {

    0% {
        transform: translateX(0);
    }

    100% {
        transform: translateX(-50%);
    }
}

.offers-track {
    display: flex;
    gap: 1.5rem;
    width: max-content;
    animation: offersScroll 38s linear infinite;
    padding: 1rem 0;
}

.offers-track:hover {
    animation-play-state: paused;
}

/* Glass effect */
.glass {
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
}

/* Hover cards */
.hover-lift {
    transition:
        transform 0.28s ease,
        box-shadow 0.28s ease;
}

.hover-lift:hover {
    transform: translateY(-8px);
    box-shadow: 0 22px 55px rgba(0,0,0,0.18);
}

/* Botones premium */
.gold-button {
    background: linear-gradient(
        135deg,
        #C9A84C,
        #F0D080
    );

    color: white;

    transition: all 0.25s ease;
}

.gold-button:hover {
    transform: translateY(-2px);
    filter: brightness(1.05);
}

/* Videos */
video {
    object-fit: cover;
}

/* Navbar blur */
.nav-blur {
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
}

/* Responsive */
@media (max-width: 768px) {

    .offers-track {
        animation-duration: 50s;
    }

    body {
        overflow-x: hidden;
    }
}

"""


# ─────────────────────────────────────────────────────────────────────────────
#  PÁGINA PRINCIPAL
# ─────────────────────────────────────────────────────────────────────────────

def index() -> rx.Component:
    return rx.box(
        rx.html(f"<style>{GLOBAL_CSS}</style>"),
        navbar(),
        hero_section(),
        stats_section(),
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