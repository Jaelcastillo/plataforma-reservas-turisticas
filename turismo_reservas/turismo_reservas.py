import reflex as rx

from turismo_reservas.pages.index import index


app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500;600&display=swap"
    ]
)

app.add_page(
    index,
    route="/",
    title="TravelWorld - Plataforma Turística Premium",
)