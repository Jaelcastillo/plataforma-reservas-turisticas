import reflex as rx


def destination_card(image, title, description):
    return rx.card(
        rx.vstack(
            rx.image(
                src=image,
                width="100%",
                height="220px",
                object_fit="cover",
                border_radius="12px",
            ),

            rx.heading(title),

            rx.text(
                description,
                color="gray",
            ),

            rx.button(
                "Explorar",
                color_scheme="blue",
                width="100%",
            ),

            spacing="4",
            align_items="start",
        ),

        width="100%",
    )


def offer_card(image, title, old_price, new_price, discount):
    return rx.card(
        rx.vstack(

            rx.badge(
                f"{discount}% OFF",
                color_scheme="red",
            ),

            rx.image(
                src=image,
                width="100%",
                height="220px",
                object_fit="cover",
                border_radius="12px",
            ),

            rx.heading(title),

            rx.hstack(

                rx.text(
                    f"${old_price}",
                    text_decoration="line-through",
                    color="gray",
                ),

                rx.text(
                    f"${new_price}",
                    color="green",
                    weight="bold",
                ),
            ),

            rx.button(
                "Reservar ahora",
                color_scheme="green",
                width="100%",
            ),

            spacing="4",
            align_items="start",
        ),

        width="100%",
    )


def navbar():
    return rx.hstack(

        rx.heading(
            "TravelWorld",
            color="white",
        ),

        rx.spacer(),

        rx.hstack(
            rx.link("Inicio", href="/", color="white"),
            rx.link("Destinos", color="white"),
            rx.link("Ofertas", color="white"),
            rx.link("Reservas", color="white"),
            rx.link("Admin", color="white"),
            spacing="6",
        ),

        padding="1.5em",
        width="100%",
        position="fixed",
        top="0",
        z_index="999",
        bg="rgba(0,0,0,0.55)",
    )


def home():

    return rx.box(

        navbar(),

        # HERO SECTION
        rx.box(

            rx.center(

                rx.vstack(

                    rx.heading(
                        "Descubre el Mundo con TravelWorld",
                        size="9",
                        color="white",
                        text_align="center",
                    ),

                    rx.text(
                        "Hoteles, resorts, Disney, excursiones y experiencias inolvidables.",
                        size="5",
                        color="white",
                        text_align="center",
                    ),

                    rx.hstack(

                        rx.input(
                            placeholder="Buscar destino...",
                            width="300px",
                            bg="white",
                        ),

                        rx.button(
                            "Buscar",
                            color_scheme="blue",
                        ),
                    ),

                    spacing="6",
                    align="center",
                ),

                height="100%",
            ),

            height="100vh",
            background="linear-gradient(rgba(0,0,0,0.45), rgba(0,0,0,0.45)), url('/travel-bg.jpg')",
            background_size="cover",
            background_position="center",
        ),

        # DESTINOS
        rx.box(

            rx.vstack(

                rx.heading(
                    "Destinos Populares",
                    size="8",
                ),

                rx.grid(

                    destination_card(
                        "/rd.jpg",
                        "República Dominicana",
                        "Playas paradisíacas, buggy y resorts.",
                    ),

                    destination_card(
                        "/cancun.jpg",
                        "Cancún",
                        "Riviera Maya y lujo tropical.",
                    ),

                    destination_card(
                        "/disney.jpg",
                        "Disney Orlando",
                        "Parques mágicos y hoteles familiares.",
                    ),

                    columns="3",
                    spacing="6",
                    width="100%",
                ),

                spacing="8",
                width="100%",
            ),

            padding="5em",
        ),

        # OFERTAS
        rx.box(

            rx.vstack(

                rx.heading(
                    "🔥 Ofertas del Momento",
                    size="8",
                ),

                rx.grid(

                    offer_card(
                        "/hotel.jpg",
                        "Resort Punta Cana",
                        "480",
                        "350",
                        "25",
                    ),

                    offer_card(
                        "/buggy.jpg",
                        "Tour Buggy Extremo",
                        "150",
                        "120",
                        "20",
                    ),

                    offer_card(
                        "/disney_offer.jpg",
                        "Disney Package",
                        "1299",
                        "899",
                        "30",
                    ),

                    columns="3",
                    spacing="6",
                    width="100%",
                ),

                spacing="8",
                width="100%",
            ),

            padding="5em",
            bg="#f8fafc",
        ),

        # FOOTER
        rx.box(

            rx.center(

                rx.vstack(

                    rx.heading(
                        "TravelWorld",
                        color="white",
                    ),

                    rx.text(
                        "La mejor plataforma turística del mundo.",
                        color="white",
                    ),

                    rx.text(
                        "© 2026 TravelWorld",
                        color="gray",
                    ),

                    spacing="3",
                ),

                padding="4em",
            ),

            bg="#0f172a",
        ),

        bg="white",
    )