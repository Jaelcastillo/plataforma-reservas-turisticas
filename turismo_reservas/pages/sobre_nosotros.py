import reflex as rx

GOLD = "#C9A84C"
GOLD_LT = "#F0D080"
DARK = "#06111D"
DARK2 = "#0B1B2B"
TEXT = "#1E1A14"
MUTED = "#6D6254"
CREAM = "#F7F1E8"
WHITE = "#FFFFFF"
BORDER = "rgba(201,168,76,.28)"


CSS = """
.about-page {
    background: #F7F1E8;
    font-family: 'Inter', sans-serif;
}
.about-hero-card {
    background: linear-gradient(135deg, #071522, #0E2A42);
    border: 1px solid rgba(201,168,76,.35);
    box-shadow: 0 30px 90px rgba(0,0,0,.25);
}
.about-glass {
    background: rgba(255,255,255,.82);
    border: 1px solid rgba(201,168,76,.25);
    box-shadow: 0 18px 45px rgba(43,36,26,.08);
}
.about-dark-card {
    background: rgba(255,255,255,.06);
    border: 1px solid rgba(255,255,255,.12);
}
"""


def label(text: str):
    return rx.text(
        text,
        color=GOLD,
        font_size="0.75rem",
        font_weight="900",
        letter_spacing="2.5px",
        text_transform="uppercase",
    )


def section_title(title: str, subtitle: str = ""):
    return rx.vstack(
        label("TravelWorld Premium"),
        rx.heading(
            title,
            color=TEXT,
            font_family="'Playfair Display', serif",
            font_size="clamp(2rem, 4vw, 3.4rem)",
            font_weight="900",
            text_align="center",
        ),
        rx.cond(
            subtitle != "",
            rx.text(
                subtitle,
                color=MUTED,
                font_size="1rem",
                line_height="1.8",
                max_width="760px",
                text_align="center",
            ),
            rx.box(),
        ),
        spacing="3",
        align="center",
        width="100%",
    )


def stat_card(number: str, text: str):
    return rx.box(
        rx.vstack(
            rx.heading(
                number,
                color=GOLD,
                font_family="'Playfair Display', serif",
                font_size="2.6rem",
                font_weight="900",
            ),
            rx.text(
                text,
                color=MUTED,
                font_size="0.9rem",
                text_align="center",
                font_weight="700",
            ),
            spacing="1",
            align="center",
        ),
        class_name="about-glass",
        border_radius="22px",
        padding="2rem",
        width="100%",
    )


def service_card(icon: str, title: str, text: str):
    return rx.box(
        rx.vstack(
            rx.box(
                rx.text(icon, font_size="1.8rem"),
                width="58px",
                height="58px",
                border_radius="18px",
                background="rgba(201,168,76,.14)",
                display="flex",
                align_items="center",
                justify_content="center",
            ),
            rx.heading(
                title,
                color=TEXT,
                font_size="1.15rem",
                font_weight="900",
            ),
            rx.text(
                text,
                color=MUTED,
                font_size="0.9rem",
                line_height="1.7",
            ),
            spacing="3",
            align="start",
        ),
        class_name="about-glass",
        border_radius="24px",
        padding="1.6rem",
        width="100%",
        min_height="220px",
    )


def founder_card(name: str, role: str, text: str):
    initials = "".join([p[0] for p in name.split()[:2]])

    return rx.box(
        rx.vstack(
            rx.box(
                rx.text(
                    initials,
                    color=WHITE,
                    font_size="1.4rem",
                    font_weight="900",
                ),
                width="78px",
                height="78px",
                border_radius="50%",
                background=f"linear-gradient(135deg, {GOLD}, #8B6A2E)",
                display="flex",
                align_items="center",
                justify_content="center",
                box_shadow="0 14px 35px rgba(201,168,76,.35)",
            ),
            rx.heading(
                name,
                color=TEXT,
                font_family="'Playfair Display', serif",
                font_size="1.45rem",
                font_weight="900",
                text_align="center",
            ),
            rx.text(
                role,
                color=GOLD,
                font_weight="900",
                text_align="center",
            ),
            rx.text(
                text,
                color=MUTED,
                font_size="0.9rem",
                line_height="1.7",
                text_align="center",
            ),
            spacing="3",
            align="center",
        ),
        class_name="about-glass",
        border_radius="26px",
        padding="2rem",
        width="100%",
    )


def process_step(num: str, title: str, text: str):
    return rx.hstack(
        rx.box(
            rx.text(num, color=TEXT, font_weight="900"),
            width="46px",
            height="46px",
            border_radius="50%",
            background=f"linear-gradient(135deg, {GOLD}, {GOLD_LT})",
            display="flex",
            align_items="center",
            justify_content="center",
            flex_shrink="0",
        ),
        rx.vstack(
            rx.heading(title, color=WHITE, font_size="1.05rem", font_weight="900"),
            rx.text(text, color="rgba(255,255,255,.65)", font_size="0.9rem", line_height="1.6"),
            spacing="1",
            align="start",
        ),
        spacing="4",
        align="start",
        width="100%",
    )


def contact_card(icon: str, title: str, value: str):
    return rx.box(
        rx.vstack(
            rx.text(icon, font_size="2rem"),
            rx.text(title, color=GOLD, font_weight="900"),
            rx.text(value, color=TEXT, font_weight="800", text_align="center"),
            spacing="2",
            align="center",
        ),
        class_name="about-glass",
        border_radius="22px",
        padding="1.7rem",
        width="100%",
    )


def sobre_nosotros() -> rx.Component:
    return rx.box(
        rx.html(f"<style>{CSS}</style>"),

        # HERO
        rx.box(
            rx.grid(
                rx.vstack(
                    label("Sobre nosotros"),
                    rx.heading(
                        "Transformando la forma de reservar experiencias premium",
                        color=WHITE,
                        font_family="'Playfair Display', serif",
                        font_size="clamp(2.5rem, 5vw, 5rem)",
                        font_weight="900",
                        line_height="1.02",
                    ),
                    rx.text(
                        "TravelWorld conecta viajeros con destinos exclusivos, resorts, tours y paquetes cuidadosamente seleccionados en el Caribe y América.",
                        color="rgba(255,255,255,.75)",
                        font_size="1.05rem",
                        line_height="1.8",
                        max_width="640px",
                    ),
                    rx.hstack(
                        rx.link(
                            rx.button(
                                "Reservar ahora",
                                background=f"linear-gradient(135deg, {GOLD}, {GOLD_LT})",
                                color=TEXT,
                                border="none",
                                border_radius="999px",
                                padding="0.9rem 1.8rem",
                                font_weight="900",
                            ),
                            href="/reservas",
                        ),
                        rx.link(
                            rx.button(
                                "Contactar",
                                background="transparent",
                                color=WHITE,
                                border="1px solid rgba(255,255,255,.25)",
                                border_radius="999px",
                                padding="0.9rem 1.8rem",
                                font_weight="800",
                            ),
                            href="#contacto",
                        ),
                        spacing="3",
                    ),
                    spacing="5",
                    align="start",
                    justify="center",
                ),

                rx.box(
                    rx.box(
                        rx.heading(
                            "BlueMall Santo Domingo",
                            color=WHITE,
                            font_family="'Playfair Display', serif",
                            font_size="2rem",
                            font_weight="900",
                        ),
                        rx.text(
                            "Piso ejecutivo de oficinas",
                            color=GOLD_LT,
                            font_weight="800",
                        ),
                        rx.text(
                            "Desde nuestra oficina corporativa coordinamos alianzas, reservas y atención personalizada para nuestros viajeros.",
                            color="rgba(255,255,255,.75)",
                            line_height="1.7",
                            margin_top="1rem",
                        ),
                        position="absolute",
                        left="24px",
                        right="24px",
                        bottom="24px",
                        z_index="2",
                    ),
                    rx.box(
                        position="absolute",
                        inset="0",
                        background="linear-gradient(180deg, rgba(0,0,0,.05), rgba(0,0,0,.78))",
                        z_index="1",
                    ),
                    background="url('/images/world_bg.jpg') center/cover no-repeat",
                    min_height="480px",
                    border_radius="32px",
                    overflow="hidden",
                    position="relative",
                    border=f"1px solid {BORDER}",
                    box_shadow="0 30px 80px rgba(0,0,0,.35)",
                ),

                style={"gridTemplateColumns": "1fr 0.9fr"},
                gap="3rem",
                align_items="center",
                max_width="1250px",
                margin="0 auto",
                width="100%",
            ),
            class_name="about-hero-card",
            padding="5rem 2rem",
            width="100%",
        ),

        # QUIENES SOMOS
        rx.box(
            rx.vstack(
                section_title(
                    "Quiénes somos",
                    "Somos una plataforma turística premium enfocada en crear reservas simples, seguras y bien organizadas para viajeros que buscan experiencias confiables y memorables.",
                ),
                rx.grid(
                    service_card("🏝️", "Destinos seleccionados", "Trabajamos con destinos de alto interés turístico como Punta Cana, Cancún, Cartagena, San Juan y Orlando."),
                    service_card("🤝", "Alianzas estratégicas", "Coordinamos con resorts, operadores turísticos y proveedores locales para ofrecer experiencias completas."),
                    service_card("🔒", "Reservas seguras", "Nuestra plataforma permite gestionar reservas con datos claros, confirmación y comprobante digital."),
                    service_card("⭐", "Atención personalizada", "Acompañamos al cliente antes, durante y después de su reserva para mejorar su experiencia."),
                    style={"gridTemplateColumns": "repeat(auto-fit, minmax(240px, 1fr))"},
                    gap="1.5rem",
                    width="100%",
                ),
                spacing="5",
                max_width="1200px",
                margin="0 auto",
                width="100%",
            ),
            padding="5rem 2rem",
        ),

        # STATS
        rx.box(
            rx.grid(
                stat_card("+5", "Destinos premium"),
                stat_card("+20", "Experiencias disponibles"),
                stat_card("+500", "Reservas gestionadas"),
                stat_card("98%", "Satisfacción proyectada"),
                style={"gridTemplateColumns": "repeat(auto-fit, minmax(180px, 1fr))"},
                gap="1.3rem",
                max_width="1100px",
                margin="0 auto",
            ),
            background="#EFE5D7",
            padding="4rem 2rem",
        ),

        # COMO TRABAJAMOS
        rx.box(
            rx.grid(
                rx.vstack(
                    label("Proceso de trabajo"),
                    rx.heading(
                        "Así creamos experiencias de viaje confiables",
                        color=WHITE,
                        font_family="'Playfair Display', serif",
                        font_size="clamp(2rem, 4vw, 3.4rem)",
                        font_weight="900",
                        line_height="1.05",
                    ),
                    rx.text(
                        "Cada oferta publicada en TravelWorld pasa por una organización previa: selección del destino, revisión de servicios, precios claros y presentación al cliente.",
                        color="rgba(255,255,255,.7)",
                        line_height="1.8",
                    ),
                    spacing="4",
                    align="start",
                ),
                rx.vstack(
                    process_step("1", "Seleccionamos destinos", "Evaluamos destinos turísticos con alta demanda y valor para el viajero."),
                    process_step("2", "Organizamos ofertas", "Agrupamos resorts, tours y experiencias según destino y categoría."),
                    process_step("3", "Facilitamos la reserva", "El cliente selecciona destino, oferta, fecha y método de pago en pocos pasos."),
                    process_step("4", "Confirmamos la experiencia", "La reserva queda registrada y se genera un comprobante para el cliente."),
                    spacing="5",
                    class_name="about-dark-card",
                    border_radius="28px",
                    padding="2rem",
                ),
                style={"gridTemplateColumns": "0.9fr 1.1fr"},
                gap="3rem",
                max_width="1200px",
                margin="0 auto",
                align_items="center",
            ),
            background=DARK,
            padding="5rem 2rem",
        ),

        # FUNDADORES
        rx.box(
            rx.vstack(
                section_title(
                    "Socios fundadores",
                    "El equipo fundador combina visión tecnológica, gestión operativa y desarrollo comercial para impulsar TravelWorld como una plataforma turística moderna.",
                ),
                rx.grid(
                    founder_card(
                        "Jael Castillo",
                        "CEO & Fundador",
                        "Responsable de la visión general, estrategia tecnológica, desarrollo de la plataforma y crecimiento de TravelWorld.",
                    ),
                    founder_card(
                        "Alissa Marie",
                        "Directora de Operaciones",
                        "Encargada de la coordinación de experiencias, organización interna y mejora del servicio al cliente.",
                    ),
                    founder_card(
                        "José Luis Mañón",
                        "Director Comercial",
                        "Responsable de relaciones corporativas, alianzas estratégicas y expansión comercial de la marca.",
                    ),
                    style={"gridTemplateColumns": "repeat(auto-fit, minmax(260px, 1fr))"},
                    gap="1.5rem",
                    width="100%",
                ),
                spacing="5",
                max_width="1150px",
                margin="0 auto",
                width="100%",
            ),
            padding="5rem 2rem",
        ),

        # OFICINA
        rx.box(
            rx.grid(
                rx.box(
                    background="url('/images/familia_viajando.jpg') center/cover no-repeat",
                    min_height="420px",
                    border_radius="30px",
                    box_shadow="0 24px 70px rgba(0,0,0,.18)",
                    border=f"1px solid {BORDER}",
                ),
                rx.vstack(
                    label("Oficina corporativa"),
                    rx.heading(
                        "Ubicados en el piso de oficinas de BlueMall Santo Domingo",
                        color=TEXT,
                        font_family="'Playfair Display', serif",
                        font_size="clamp(2rem, 4vw, 3.2rem)",
                        font_weight="900",
                        line_height="1.08",
                    ),
                    rx.text(
                        "Desde nuestra oficina en BlueMall coordinamos operaciones, atención a clientes, organización de ofertas turísticas y relaciones con aliados estratégicos.",
                        color=MUTED,
                        line_height="1.8",
                        font_size="1rem",
                    ),
                    rx.vstack(
                        rx.text("📍 BlueMall Santo Domingo, República Dominicana", color=TEXT, font_weight="800"),
                        rx.text("🕘 Lunes a viernes · 8:00 AM - 6:00 PM", color=TEXT, font_weight="800"),
                        rx.text("🤝 Atención por cita y soporte digital", color=TEXT, font_weight="800"),
                        spacing="3",
                        align="start",
                    ),
                    spacing="4",
                    align="start",
                ),
                style={"gridTemplateColumns": "1fr 1fr"},
                gap="3rem",
                max_width="1200px",
                margin="0 auto",
                align_items="center",
            ),
            background="#EFE5D7",
            padding="5rem 2rem",
        ),

        # CONTACTO
        rx.box(
            rx.vstack(
                section_title(
                    "Contacto",
                    "Estamos disponibles para reservas, soporte, alianzas comerciales y consultas generales.",
                ),
                rx.grid(
                    contact_card("📧", "Correo general", "contacto@travelworld.com"),
                    contact_card("🎟️", "Reservas", "reservas@travelworld.com"),
                    contact_card("📞", "Teléfono", "+1 (809) 555-2026"),
                    contact_card("💬", "WhatsApp", "+1 (829) 555-2026"),
                    style={"gridTemplateColumns": "repeat(auto-fit, minmax(220px, 1fr))"},
                    gap="1.3rem",
                    width="100%",
                ),
                rx.link(
                    rx.button(
                        "Volver al inicio",
                        background=f"linear-gradient(135deg, {GOLD}, {GOLD_LT})",
                        color=TEXT,
                        border="none",
                        border_radius="999px",
                        padding="1rem 2rem",
                        font_weight="900",
                        margin_top="1rem",
                    ),
                    href="/",
                ),
                spacing="5",
                max_width="1100px",
                margin="0 auto",
                width="100%",
            ),
            id="contacto",
            padding="5rem 2rem",
        ),

        class_name="about-page",
        width="100%",
    )