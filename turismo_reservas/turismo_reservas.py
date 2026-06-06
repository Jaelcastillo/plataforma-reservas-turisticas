import reflex as rx

from turismo_reservas.states.auth_state import AuthState

from turismo_reservas.pages.index import index
from turismo_reservas.pages.reservas import reservas
from turismo_reservas.pages.login import login
from turismo_reservas.pages.registro import registro
from turismo_reservas.pages.admin.dashboard import dashboard
from turismo_reservas.pages.mis_reservas import mis_reservas
from turismo_reservas.pages.admin_reservas import admin_reservas
from turismo_reservas.pages.admin_ofertas import admin_ofertas
from turismo_reservas.pages.ofertas import ofertas
from turismo_reservas.pages.admin_usuarios import admin_usuarios
from turismo_reservas.states.auth_state import AuthState
from turismo_reservas.pages.admin_destinos import admin_destinos


app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500;600&display=swap"
    ]
)

app.add_page(
    index,
    route="/",
    title="TravelWorld - Plataforma Turística Premium",
    on_load=AuthState.cargar_ofertas_publicas,
)

app.add_page(
    reservas,
    route="/reservas",
    title="Reservas - TravelWorld",
    on_load=AuthState.cargar_destinos_reserva,
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

app.add_page(
    mis_reservas,
    route="/mis-reservas",
    title="Mis Reservas - TravelWorld",
)

app.add_page(
    admin_reservas,
    route="/admin/reservas",
    title="Reservas Admin",
)

app.add_page(
    admin_ofertas,
    route="/admin/ofertas",
    title="Ofertas Admin",
)

app.add_page(
    ofertas,
    route="/ofertas",
    title="Todas las ofertas",
    on_load=AuthState.cargar_ofertas_publicas,
)

app.add_page(
    admin_usuarios,
    route="/admin/usuarios",
    title="Usuarios Admin",
    on_load=AuthState.cargar_usuarios_admin,
)

app.add_page(
    admin_destinos,
    route="/admin/destinos",
    title="Destinos Admin",
    on_load=AuthState.cargar_destinos_admin,
)