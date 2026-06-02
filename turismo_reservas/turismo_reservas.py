import reflex as rx

from turismo_reservas.pages.index import index
from turismo_reservas.pages.reservas import reservas
from turismo_reservas.pages.login import login
from turismo_reservas.pages.registro import registro
from turismo_reservas.pages.admin.dashboard import dashboard


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

app.add_page(
    reservas,
    route="/reservas",
    title="Reservas - TravelWorld",
)

app.add_page(
    login,
    route="/login",
    title="Iniciar Sesión - TravelWorld",
)

app.add_page(
    registro,
    route="/registro",
    title="Registro - TravelWorld",
)

app.add_page(
    dashboard,
    route="/admin/dashboard",
    title="Admin Dashboard - TravelWorld",
)