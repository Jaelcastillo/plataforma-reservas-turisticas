"""
TravelWorld - Premium Checkout / Reservas
Archivo: pages/reservas.py

Reemplaza completamente tu reservas.py actual con este archivo.
"""

import reflex as rx
from turismo_reservas.states.reservation_state import ReservationState

# ─── Paleta (igual que index.py) ──────────────────────────────────────────────
DARK       = "#FDF9F3"
DARK2      = "#F5EFE6"
TEAL       = "#8B6A2E"
TEAL_LT    = "#C9A84C"
GOLD       = "#C9A84C"
GOLD_LT    = "#E8CF84"
CORAL      = "#B86B55"
CREAM      = "#FDF9F3"
GLASS_BG   = "rgba(255,255,255,0.72)"
GLASS_BOR  = "rgba(139,106,46,0.18)"
GOLD_BOR   = "rgba(201,168,76,0.35)"
TEXT_DARK  = "#2B241A"
TEXT_MUTED = "#6E6254"

# ─── Catálogo de destinos y ofertas ──────────────────────────────────────────
PAISES = [
    {"id": "rd", "nombre": "República Dominicana", "bandera": "🇩🇴", "imagen": "/images/punta_cana.png"},
    {"id": "pr", "nombre": "Puerto Rico", "bandera": "🇵🇷", "imagen": "/images/puerto_rico.jpg"},
    {"id": "co", "nombre": "Colombia", "bandera": "🇨🇴", "imagen": "/images/cartagena.jpg"},
    {"id": "mx", "nombre": "México", "bandera": "🇲🇽", "imagen": "/images/cancun.jpg.jpg"},
    {"id": "us", "nombre": "Estados Unidos", "bandera": "🇺🇸", "imagen": "/images/disney.jpg"},

]

OFERTAS_POR_PAIS = {
    "rd": [
        {"id": "buggy",   "nombre": "Tour en Buggy Punta Cana",     "precio": 120,  "original": 180,  "duracion": "8 horas",   "icono": "🏎️", "imagen": "/images/offer_buggy.jpg",       "estrellas": "4.9", "reviews": "984"},
        {"id": "bavaro",  "nombre": "Resort Todo Incluido Bávaro",   "precio": 350,  "original": 499,  "duracion": "7 noches",  "icono": "🏨", "imagen": "/images/offer_punta_cana.jpg",  "estrellas": "5.0", "reviews": "2,341"},
        {"id": "saona",   "nombre": "Isla Saona Excursión Privada",  "precio": 95,   "original": 140,  "duracion": "1 día",     "icono": "🏝️", "imagen": "/images/punta_cana.png",        "estrellas": "4.8", "reviews": "1,120"},
    ],
    "pr": [
        {"id": "sanjuan", "nombre": "Tour Viejo San Juan",           "precio": 85,   "original": 120,  "duracion": "1 día",     "icono": "🏰", "imagen": "/images/offer_pr.jpg",          "estrellas": "4.8", "reviews": "730"},
        {"id": "prresort","nombre": "San Juan Premium Escape",       "precio": 950,  "original": 1250, "duracion": "4 noches",  "icono": "🌺", "imagen": "/images/resort_ritz.jpg",       "estrellas": "4.9", "reviews": "1,502"},
    ],
    "co": [
        {"id": "rosario", "nombre": "Islas del Rosario",             "precio": 120,  "original": 180,  "duracion": "1 día",     "icono": "🌊", "imagen": "/images/offer_cartagena.jpg",   "estrellas": "4.8", "reviews": "1,204"},
        {"id": "cart_c",  "nombre": "Cartagena Ciudad Amurallada",   "precio": 75,   "original": 110,  "duracion": "Medio día", "icono": "🌿", "imagen": "/images/cartagena.jpg",         "estrellas": "4.7", "reviews": "890"},
    ],
    "mx": [
        {"id": "coco",    "nombre": "VIP Coco Bongo Experience",     "precio": 199,  "original": 320,  "duracion": "1 noche",   "icono": "🎉", "imagen": "/images/offer_cancun.jpg",      "estrellas": "4.9", "reviews": "5,842"},
        {"id": "hard_r",  "nombre": "Hard Rock Hotel Cancún",        "precio": 380,  "original": 520,  "duracion": "5 noches",  "icono": "🎸", "imagen": "/images/resort_hardrock.jpg",   "estrellas": "9.5", "reviews": "3,200"},
        {"id": "cenotes", "nombre": "Tour Cenotes + Tulum",          "precio": 110,  "original": 160,  "duracion": "1 día",     "icono": "💧", "imagen": "/images/offer_cancun.jpg",      "estrellas": "4.8", "reviews": "2,100"},
    ],
    "us": [
        {"id": "disney",  "nombre": "Disney World + Hotel Premium",  "precio": 2499, "original": 3099, "duracion": "6 noches",  "icono": "✨", "imagen": "/images/offer_disney.jpg",      "estrellas": "5.0", "reviews": "8,721"},
        {"id": "magic",   "nombre": "Universal Studios Orlando",     "precio": 899,  "original": 1200, "duracion": "4 noches",  "icono": "🎢", "imagen": "/images/disney.jpg",            "estrellas": "4.9", "reviews": "4,300"},
    ],
}

# ─── CSS Global para la página ────────────────────────────────────────────────
CHECKOUT_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Inter:wght@300;400;500;600;700;800&display=swap');

* { box-sizing: border-box; }

body {
    margin: 0;
    padding: 0;
    font-family: 'Inter', sans-serif;
    background: #FDF9F3;
    overflow-x: hidden;
}

/* Progress bar */
.step-connector {
    height: 2px;
    flex: 1;
    background: rgba(201,168,76,0.2);
    transition: background 0.4s;
}
.step-connector.active {
    background: linear-gradient(90deg, #C9A84C, #F0D080);
}

/* Animaciones */
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(30px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes slideInRight {
    from { opacity: 0; transform: translateX(30px); }
    to   { opacity: 1; transform: translateX(0); }
}
@keyframes shimmer {
    0%   { background-position: -200% 0; }
    100% { background-position: 200% 0; }
}
@keyframes glowPulse {
    0%   { box-shadow: 0 0 0   rgba(201,168,76,0); }
    50%  { box-shadow: 0 0 30px rgba(201,168,76,0.4); }
    100% { box-shadow: 0 0 0   rgba(201,168,76,0); }
}

.step-panel { animation: fadeInUp 0.45s ease both; }
.summary-panel { animation: slideInRight 0.45s ease both; }

/* Cards de país */
.country-card {
    background: rgba(255,255,255,0.78);
    border: 1.5px solid rgba(139,106,46,0.18);
    border-radius: 18px;
    padding: 1.1rem 1.4rem;
    cursor: pointer;
    transition: all 0.25s ease;
    display: flex;
    align-items: center;
    gap: 1rem;
    box-shadow: 0 12px 30px rgba(43,36,26,0.06);
}
.country-card:hover {
    border-color: rgba(201,168,76,0.7);
    background: rgba(255,255,255,0.95);
    transform: translateY(-2px);
}
.country-card.selected {
    border-color: #C9A84C;
    background: #FFF8E8;
    box-shadow: 0 12px 35px rgba(201,168,76,0.22);
}

/* Cards de oferta */
.offer-card {
    background: rgba(255,255,255,0.92);
    border: 1.5px solid rgba(139,106,46,0.15);
    border-radius: 20px;
    overflow: hidden;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 12px 35px rgba(43,36,26,0.07);
}
.offer-card:hover {
    border-color: rgba(201,168,76,0.55);
    transform: translateY(-4px);
    box-shadow: 0 20px 50px rgba(0,0,0,0.4);
}
.offer-card.selected {
    border-color: #C9A84C;
    box-shadow: 0 16px 50px rgba(201,168,76,0.25);
}

/* Input fields */
.premium-input {
    background: rgba(255,255,255,0.05) !important;
    border: 1.5px solid rgba(255,255,255,0.1) !important;
    border-radius: 12px !important;
    color: white !important;
    padding: 0.8rem 1.1rem !important;
    font-size: 0.92rem !important;
    width: 100%;
    transition: border-color 0.2s, background 0.2s !important;
    outline: none;
}
.premium-input:focus {
    border-color: #C9A84C !important;
    background: rgba(201,168,76,0.06) !important;
    box-shadow: 0 0 0 3px rgba(201,168,76,0.1) !important;
}
.premium-input::placeholder {
    color: rgba(255,255,255,0.3) !important;
}

/* Payment methods */
.pay-btn {
    background: rgba(255,255,255,0.05);
    border: 1.5px solid rgba(255,255,255,0.1);
    border-radius: 14px;
    padding: 0.8rem 1.4rem;
    cursor: pointer;
    transition: all 0.2s;
    color: rgba(255,255,255,0.7);
    font-size: 0.88rem;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.pay-btn:hover {
    border-color: rgba(201,168,76,0.5);
    color: white;
}
.pay-btn.selected {
    border-color: #C9A84C;
    background: rgba(201,168,76,0.1);
    color: #F0D080;
    box-shadow: 0 4px 20px rgba(201,168,76,0.15);
}

/* Card preview */
.credit-card-preview {
    background: linear-gradient(135deg, #1a2a3a 0%, #0d1b2a 40%, #1a3a2a 100%);
    border-radius: 18px;
    padding: 1.5rem;
    border: 1px solid rgba(201,168,76,0.3);
    box-shadow: 0 20px 60px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.05);
    position: relative;
    overflow: hidden;
}
.credit-card-preview::before {
    content: '';
    position: absolute;
    top: -50%;
    right: -20%;
    width: 200px;
    height: 200px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(201,168,76,0.12) 0%, transparent 70%);
}

/* Confirm button */
.confirm-btn {
    background: linear-gradient(135deg, #C9A84C, #F0D080, #C9A84C);
    background-size: 200% 100%;
    color: #0D1B2A;
    border: none;
    border-radius: 16px;
    padding: 1rem 2rem;
    font-weight: 900;
    font-size: 1rem;
    cursor: pointer;
    width: 100%;
    transition: all 0.3s;
    letter-spacing: 0.5px;
    animation: shimmer 3s infinite linear;
}
.confirm-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 15px 40px rgba(201,168,76,0.4);
    animation-play-state: paused;
}

/* Scrollbar */
::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: #0a1520; }
::-webkit-scrollbar-thumb { background: linear-gradient(180deg, #C9A84C, #8B6A2E); border-radius: 20px; }
"""


# ─── Estado ampliado ──────────────────────────────────────────────────────────
class CheckoutState(rx.State):
    # Wizard
    paso: int = 1

    # Paso 1 – País
    pais_id: str = ""
    pais_nombre: str = ""
    pais_imagen: str = ""

    # Paso 2 – Oferta
    oferta_id: str = ""
    oferta_nombre: str = ""
    oferta_precio: int = 0
    oferta_original: int = 0
    oferta_duracion: str = ""
    oferta_imagen: str = ""

    # Paso 3/4 – Viajero
    nombre: str = ""
    email: str = ""
    telefono: str = ""
    fecha_viaje: str = ""
    personas: str = "1"
    comentarios: str = ""

    # Paso 5 – Pago
    metodo_pago: str = "Tarjeta"
    card_num: str = ""
    card_name: str = ""
    card_exp: str = ""
    card_cvv: str = ""

    # Resultado
    mensaje: str = ""
    reserva_ok: bool = False

    # ── Setters simples ──────────────────────────────────────────────────────
    def set_nombre(self, v):    self.nombre = v
    def set_email(self, v):     self.email = v
    def set_telefono(self, v):  self.telefono = v
    def set_fecha(self, v):     self.fecha_viaje = v
    def set_personas(self, v):  self.personas = v
    def set_comentarios(self, v): self.comentarios = v
    def set_card_num(self, v):  self.card_num = v
    def set_card_name(self, v): self.card_name = v
    def set_card_exp(self, v):  self.card_exp = v
    def set_card_cvv(self, v):  self.card_cvv = v
    def set_metodo(self, v):    self.metodo_pago = v

    # ── Navegación ──────────────────────────────────────────────────────────
    def seleccionar_pais(self, pais: dict):
        self.pais_id     = pais["id"]
        self.pais_nombre = pais["nombre"]
        self.pais_imagen = pais["imagen"]
        self.oferta_id   = ""
        self.paso = 2

    def seleccionar_oferta(self, oferta: dict):
        self.oferta_id       = oferta["id"]
        self.oferta_nombre   = oferta["nombre"]
        self.oferta_precio   = oferta["precio"]
        self.oferta_original = oferta["original"]
        self.oferta_duracion = oferta["duracion"]
        self.oferta_imagen   = oferta["imagen"]
        self.paso = 3

    def ir_paso(self, p: int):
        self.paso = p

    # ── Confirmar reserva ────────────────────────────────────────────────────
    def confirmar_reserva(self):
        from datetime import datetime
        from api.services import crear_reserva
        try:
            if not self.nombre or not self.email or not self.fecha_viaje:
                self.mensaje = "❌ Completa los campos obligatorios."
                return
            crear_reserva(
                nombre      = self.nombre,
                email       = self.email,
                telefono    = self.telefono,
                pais_destino= self.pais_nombre,
                oferta      = self.oferta_nombre,
                fecha_viaje = datetime.strptime(self.fecha_viaje, "%Y-%m-%d").date(),
                personas    = int(self.personas),
                metodo_pago = self.metodo_pago,
                comentarios = self.comentarios,
            )
            self.reserva_ok = True
            self.mensaje = "✅ ¡Reserva confirmada! Te enviamos los detalles por email."
            self.paso = 6
        except Exception as e:
            self.mensaje = f"❌ Error: {str(e)}"

    # ── Precio final ─────────────────────────────────────────────────────────
    @rx.var
    def precio_total(self) -> int:
        try:
            return self.oferta_precio * int(self.personas)
        except:
            return self.oferta_precio

    @rx.var
    def descuento_pct(self) -> int:
        if self.oferta_original > 0:
            return round((1 - self.oferta_precio / self.oferta_original) * 100)
        return 0

    @rx.var
    def ofertas_disponibles(self) -> list:
        return OFERTAS_POR_PAIS.get(self.pais_id, [])


# ─────────────────────────────────────────────────────────────────────────────
#  HELPERS DE UI
# ─────────────────────────────────────────────────────────────────────────────

def gold_text(txt: str, size: str = "1rem") -> rx.Component:
    return rx.text(
        txt,
        style={
            "background": f"linear-gradient(135deg, {GOLD}, {GOLD_LT})",
            "WebkitBackgroundClip": "text",
            "WebkitTextFillColor": "transparent",
            "backgroundClip": "text",
            "fontSize": size,
            "fontFamily": "'Playfair Display', serif",
            "fontWeight": "900",
            "display": "inline",
        },
    )


def paso_indicator(num: int, label: str, activo: bool, completado: bool) -> rx.Component:
    circle_bg = rx.cond(
        completado,
        f"linear-gradient(135deg, {TEAL}, {TEAL_LT})",
        rx.cond(activo, f"linear-gradient(135deg, {GOLD}, {GOLD_LT})", "rgba(255,255,255,0.08)"),
    )
    circle_color = rx.cond(
        rx.cond(completado, True, activo),
        rx.cond(completado, "white", DARK),
        "rgba(255,255,255,0.3)",
    )
    label_color = rx.cond(
        activo,
        "white",
        rx.cond(completado, "rgba(255,255,255,0.6)", "rgba(255,255,255,0.25)"),
    )
    return rx.vstack(
       rx.box(
    rx.cond(
        completado,
        rx.text(
            "✓",
            color=TEXT_DARK,
            font_weight="900",
            font_size="1rem",
            line_height="1",
        ),
        rx.text(
            str(num),
            color=circle_color,
            font_weight="800",
            font_size="1rem",
            line_height="1",
        ),
    ),
    width="42px",
    height="42px",
    border_radius="50%",
    style={"background": circle_bg},
    display="flex",
    align_items="center",
    justify_content="center",
    box_shadow=rx.cond(activo, f"0 0 20px rgba(201,168,76,0.5)", "none"),
    transition="all 0.3s",
),
        rx.text(
            label,
            font_size="0.65rem",
            color=label_color,
            font_weight=rx.cond(activo, "700", "400"),
            text_align="center",
            letter_spacing="0.5px",
            text_transform="uppercase",
            transition="all 0.3s",
            white_space="nowrap",
        ),
        spacing="2",
        align="center",
    )


def progress_bar() -> rx.Component:
    labels = ["País", "Oferta", "Viajero", "Pago", "Confirmar"]
    steps = []
    for i, label in enumerate(labels, 1):
        steps.append(
            paso_indicator(
                i, label,
                activo=CheckoutState.paso == i,
                completado=CheckoutState.paso > i,
            )
        )
        if i < len(labels):
            steps.append(
                rx.box(
                    height="2px",
                    flex="1",
                    margin_bottom="18px",
                    background=rx.cond(
                        CheckoutState.paso > i,
                        f"linear-gradient(90deg, {TEAL}, {TEAL_LT})",
                        "rgba(255,255,255,0.08)",
                    ),
                    transition="background 0.4s",
                    min_width="20px",
                )
            )
    return rx.hstack(
        *steps,
        align="center",
        width="100%",
        max_width="520px",
        margin="0 auto",
    )


# ─────────────────────────────────────────────────────────────────────────────
#  PANEL RESUMEN (derecha) — con imagen dinámica
# ─────────────────────────────────────────────────────────────────────────────

def summary_panel():
    img = rx.cond(
        CheckoutState.oferta_imagen != "",
        CheckoutState.oferta_imagen,
        CheckoutState.pais_imagen,
    )

    return rx.box(
        rx.box(
            rx.box(
                position="absolute",
                inset="0",
                background="linear-gradient(180deg, rgba(0,0,0,.10), rgba(0,0,0,.65))",
            ),
            rx.vstack(
                rx.text(
                    rx.cond(
                        CheckoutState.oferta_nombre != "",
                        CheckoutState.oferta_nombre,
                        CheckoutState.pais_nombre,
                    ),
                    color="white",
                    font_size="1.15rem",
                    font_weight="900",
                    font_family="'Playfair Display', serif",
                ),
                rx.text(
                    rx.cond(
                        CheckoutState.pais_nombre != "",
                        CheckoutState.pais_nombre,
                        "TravelWorld Premium",
                    ),
                    color=GOLD_LT,
                    font_size=".85rem",
                ),
                position="absolute",
                bottom="20px",
                left="20px",
                spacing="1",
            ),
            style={
                "backgroundImage": "url(" + img + ")",
                "backgroundSize": "cover",
                "backgroundPosition": "center",
            },
            height="220px",
            position="relative",
        ),

        rx.vstack(
            rx.text(
                "Resumen de tu reserva",
                color=TEXT_DARK,
                font_weight="900",
                letter_spacing="2px",
                text_transform="uppercase",
            ),

            rx.text("📍 Destino", color=TEXT_MUTED),
            rx.text(
                rx.cond(
                    CheckoutState.pais_nombre != "",
                    CheckoutState.pais_nombre,
                    "Selecciona un país",
                ),
                color=TEXT_DARK,
                font_weight="800",
            ),

            rx.cond(
                CheckoutState.oferta_nombre != "",
                rx.vstack(
                    rx.text("🎯 Oferta", color=TEXT_MUTED),
                    rx.text(
                        CheckoutState.oferta_nombre,
                        color=TEXT_DARK,
                        font_weight="800",
                    ),

                    rx.text("⏱ Duración", color=TEXT_MUTED),
                    rx.text(
                        CheckoutState.oferta_duracion,
                        color=TEXT_DARK,
                        font_weight="800",
                    ),

                    rx.hstack(
                        rx.text("Precio base / persona", color=TEXT_MUTED),
                        rx.spacer(),
                        rx.text(
                            "$" + CheckoutState.oferta_precio.to_string(),
                            color=TEXT_DARK,
                            font_weight="900",
                        ),
                        width="100%",
                    ),

                    rx.hstack(
                        rx.text("Precio original", color=TEXT_MUTED),
                        rx.spacer(),
                        rx.text(
                            "$" + CheckoutState.oferta_original.to_string(),
                            color=TEXT_MUTED,
                            text_decoration="line-through",
                        ),
                        width="100%",
                    ),

                    rx.hstack(
                        rx.text("Descuento", color=CORAL, font_weight="900"),
                        rx.spacer(),
                        rx.text(
                            "-" + CheckoutState.descuento_pct.to_string() + "% OFF",
                            color=CORAL,
                            font_weight="900",
                        ),
                        width="100%",
                    ),

                    rx.box(height="1px", width="100%", background="rgba(139,106,46,.18)"),

                    rx.text("TOTAL", color=TEXT_MUTED, font_weight="800"),
                    rx.text(
                        "$" + CheckoutState.precio_total.to_string(),
                        color=GOLD,
                        font_size="2rem",
                        font_weight="900",
                    ),

                    spacing="3",
                    align="start",
                    width="100%",
                ),
                rx.text(
                    "Selecciona una oferta para ver el precio.",
                    color=TEXT_MUTED,
                ),
            ),

            rx.box(height="1px", width="100%", background="rgba(139,106,46,.18)"),

            rx.text("🔒 Pago 100% seguro", color=TEXT_MUTED),
            rx.text("✅ Cancelación flexible", color=TEXT_MUTED),
            rx.text("⭐ Soporte 24/7 en español", color=TEXT_MUTED),

            spacing="3",
            align="start",
            padding="1.5rem",
        ),

        background="white",
        border=f"1px solid {GOLD_BOR}",
        border_radius="24px",
        overflow="hidden",
        box_shadow="0 18px 45px rgba(43,36,26,.08)",
        width="100%",
        max_width="380px",
        position="sticky",
        top="95px",
    )
        # Contenido del resumen
        rx.vstack(
            rx.text(
                "Resumen de tu reserva",
                color="rgba(255,255,255,0.5)",
                font_size="0.68rem",
                text_transform="uppercase",
                letter_spacing="2px",
                font_weight="600",
            ),

            # Fila destino
            rx.cond(
                CheckoutState.pais_nombre != "",
                rx.hstack(
                    rx.text("📍", font_size="0.85rem"),
                    rx.vstack(
                        rx.text("Destino", color="rgba(255,255,255,0.4)", font_size="0.65rem", font_weight="600", letter_spacing="0.5px"),
                        rx.text(CheckoutState.pais_nombre,color=TEXT_DARK,  font_size="0.9rem", font_weight="700"),
                        spacing="0",
                        align="start",
                    ),
                    spacing="3",
                    align="center",
                    width="100%",
                ),
                rx.box(),
            ),

            # Fila oferta
            rx.cond(
                CheckoutState.oferta_nombre != "",
                rx.vstack(
                    rx.hstack(
                        rx.text("🎯", font_size="0.85rem"),
                        rx.vstack(
                            rx.text("Oferta", color="rgba(255,255,255,0.4)", font_size="0.65rem", font_weight="600", letter_spacing="0.5px"),
                            rx.text(CheckoutState.oferta_nombre, color=TEXT_DARK,font_size="0.88rem", font_weight="700"),
                            spacing="0",
                            align="start",
                        ),
                        spacing="3",
                        align="start",
                        width="100%",
                    ),
                    rx.hstack(
                        rx.text("⏱️", font_size="0.85rem"),
                        rx.vstack(
                            rx.text("Duración", color="rgba(255,255,255,0.4)", font_size="0.65rem", font_weight="600", letter_spacing="0.5px"),
                            rx.text(CheckoutState.oferta_duracion, color=TEXT_DARK, font_size="0.88rem", font_weight="700"),
                            spacing="0",
                            align="start",
                        ),
                        spacing="3",
                        align="center",
                        width="100%",
                    ),
                    rx.box(height="1px", width="100%", background="rgba(255,255,255,0.07)"),
                    # Precios
                    rx.hstack(
                        rx.text("Precio base / persona", color="rgba(255,255,255,0.4)", font_size="0.78rem"),
                        rx.spacer(),
                        rx.text(
                            rx.text.span("$", font_size="0.8rem"),
                            rx.text.span(CheckoutState.oferta_precio.to_string()),
                            color=TEXT_DARK, font_size="0.9rem", font_weight="700",
                        ),
                        width="100%",
                    ),
                    rx.hstack(
                        rx.text("Precio original", color="rgba(255,255,255,0.3)", font_size="0.78rem"),
                        rx.spacer(),
                        rx.text(
                            rx.text.span("$", font_size="0.75rem"),
                            rx.text.span(CheckoutState.oferta_original.to_string()),
                            color="rgba(255,255,255,0.3)",
                            text_decoration="line-through",
                            font_size="0.85rem",
                        ),
                        width="100%",
                    ),
                    rx.hstack(
                        rx.text("Descuento", color=CORAL, font_size="0.78rem", font_weight="600"),
                        rx.spacer(),
                        rx.text(
                            "-",
                            CheckoutState.descuento_pct.to_string(),
                            "% OFF",
                            color=CORAL, font_size="0.85rem", font_weight="700",
                        ),
                        width="100%",
                    ),
                    rx.box(height="1px", width="100%", background="rgba(255,255,255,0.07)"),
                    rx.hstack(
                        rx.vstack(
                            rx.text("TOTAL", color="rgba(255,255,255,0.4)", font_size="0.65rem", letter_spacing="2px"),
                            rx.text(
                                rx.text.span(CheckoutState.personas, " pax × $", font_size="0.78rem", color="rgba(255,255,255,0.4)"),
                                color=TEXT_DARK, font_size="0.8rem",
                            ),
                            spacing="0",
                        ),
                        rx.spacer(),
                        rx.text(
                            "$",
                            CheckoutState.precio_total.to_string(),
                            style={
                                "fontFamily": "'Playfair Display', serif",
                                "fontSize": "1.9rem",
                                "fontWeight": "900",
                                "background": f"linear-gradient(135deg, {GOLD}, {GOLD_LT})",
                                "WebkitBackgroundClip": "text",
                                "WebkitTextFillColor": "transparent",
                                "backgroundClip": "text",
                            },
                        ),
                        width="100%",
                        align="end",
                    ),
                    spacing="3",
                    width="100%",
                ),
                rx.box(),
            ),

            # Garantías
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.text("", font_size="0.8rem"),
                        rx.text("Pago 100% seguro", color=TEXT_MUTED, font_size="0.72rem"),
                        spacing="2",
                    ),
                    rx.hstack(
                        rx.text("✅", font_size="0.8rem"),
                        rx.text("Cancelación flexible", color=TEXT_MUTED, font_size="0.72rem"),
                        spacing="2",
                    ),
                    rx.hstack(
                        rx.text("⭐", font_size="0.8rem"),
                        rx.text("Soporte 24/7 en español", color=TEXT_MUTED, font_size="0.72rem"),
                        spacing="2",
                    ),
                    spacing="2",
                    align="start",
                ),
                background="rgba(255,255,255,0.03)",
                border="1px solid rgba(255,255,255,0.06)",
                border_radius="12px",
                padding="1rem",
                width="100%",
            ),

            spacing="4",
            align="start",
            width="100%",
            padding="1.5rem",
        ),

        background="rgba(255,255,255,0.04)",
        border=f"1px solid {GLASS_BOR}",
        border_radius="20px",
        overflow="hidden",
        class_name="summary-panel",
        width="100%",
        max_width="360px",
        position="sticky",
        top="100px",
    )


# ─────────────────────────────────────────────────────────────────────────────
#  PASO 1 – SELECCIÓN DE PAÍS
# ─────────────────────────────────────────────────────────────────────────────

def pais_card(p: dict) -> rx.Component:
    is_selected = CheckoutState.pais_id == p["id"]
    return rx.box(
        rx.hstack(
            rx.text(p["bandera"], font_size="2rem"),
            rx.text(
                p["nombre"],
                color=rx.cond(is_selected, GOLD, TEXT_DARK),
                font_size="1rem",
                font_weight=rx.cond(is_selected, "700", "500"),
            ),
            rx.spacer(),
            rx.cond(
                is_selected,
                rx.box(
    rx.text(
        "✓",
        color=DARK,
        font_size="0.9rem",
        font_weight="900",
        line_height="1",
    ),
    background=f"linear-gradient(135deg, {GOLD}, {GOLD_LT})",
    width="32px",
    height="32px",
    min_width="32px",
    min_height="32px",
    border_radius="50%",
    display="flex",
    align_items="center",
    justify_content="center",
),
                rx.box(),
            ),
            spacing="4",
            align="center",
            width="100%",
        ),
        class_name=rx.cond(is_selected, "country-card selected", "country-card"),
        on_click=CheckoutState.seleccionar_pais(p),
        width="100%",
    )


def paso1() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.text(
                "Paso 1 de 5",
                color=GOLD,
                font_size="0.7rem",
                text_transform="uppercase",
                letter_spacing="2px",
                font_weight="700",
            ),
            rx.heading(
                "¿A dónde quieres viajar?",
                style={
                    "fontFamily": "'Playfair Display', serif",
                    "fontSize": "clamp(1.6rem, 3vw, 2.2rem)",
                    "fontWeight": "800",
                    "color": TEXT_DARK,
                },
            ),
            rx.text(
                "Selecciona tu destino para ver las mejores experiencias disponibles",
                color=TEXT_MUTED,
                font_size="0.9rem",
            ),
            spacing="2",
            align="start",
            width="100%",
        ),
        rx.vstack(
            *[pais_card(p) for p in PAISES],
            spacing="3",
            width="100%",
        ),
        class_name="step-panel",
        spacing="6",
        width="100%",
        align="start",
    )


# ─────────────────────────────────────────────────────────────────────────────
#  PASO 2 – SELECCIÓN DE OFERTA
# ─────────────────────────────────────────────────────────────────────────────

def oferta_card_item(o: dict) -> rx.Component:
    is_selected = CheckoutState.oferta_id == o["id"]
    return rx.box(
        rx.box(
            rx.box(
                position="absolute",
                inset="0",
                background="linear-gradient(180deg, rgba(13,27,42,0.1) 0%, rgba(13,27,42,0.8) 100%)",
                z_index="1",
            ),
            rx.box(
                rx.text(
                    o["icono"] + " " + o["duracion"],
                    color=TEXT_DARK,
                    font_size="0.72rem",
                    font_weight="600",
                ),
                background="rgba(0,0,0,0.55)",
                border="1px solid rgba(255,255,255,0.15)",
                padding="4px 10px",
                border_radius="999px",
                position="absolute",
                top="12px",
                left="12px",
                z_index="2",
            ),
            rx.cond(
                is_selected,
                rx.box(
                    rx.text("✓ Seleccionado", color=DARK, font_size="0.7rem", font_weight="800"),
                    background=f"linear-gradient(135deg, {GOLD}, {GOLD_LT})",
                    padding="4px 10px",
                    border_radius="999px",
                    position="absolute",
                    top="12px",
                    right="12px",
                    z_index="2",
                ),
                rx.box(),
            ),
            style={"backgroundImage": f"url({o['imagen']})", "backgroundSize": "cover", "backgroundPosition": "center"},
            height="160px",
            position="relative",
            overflow="hidden",
        ),
        rx.vstack(
            rx.text(
                o["nombre"],
                color=TEXT_DARK,
                font_size="0.95rem",
                font_weight="800",
                font_family="'Playfair Display', serif",
            ),
            rx.text(
                f"★ {o['estrellas']}  ({o['reviews']} reseñas)",
                color=GOLD,
                font_size="0.75rem",
            ),
            rx.hstack(
                rx.text(
                    f"${o['precio']}",
                    style={
                        "fontFamily": "'Playfair Display', serif",
                        "fontSize": "1.5rem",
                        "fontWeight": "900",
                        "background": f"linear-gradient(135deg, {GOLD}, {GOLD_LT})",
                        "WebkitBackgroundClip": "text",
                        "WebkitTextFillColor": "transparent",
                        "backgroundClip": "text",
                    },
                ),
                rx.text(
                    f"${o['original']}",
                    color="rgba(255,255,255,0.3)",
                    text_decoration="line-through",
                    font_size="0.85rem",
                    align_self="end",
                    margin_bottom="4px",
                ),
                rx.spacer(),
                rx.text(
                    f"-{round((1 - o['precio']/o['original'])*100)}%",
                    color=CORAL,
                    font_size="0.78rem",
                    font_weight="800",
                    align_self="end",
                    margin_bottom="6px",
                ),
                width="100%",
                align="end",
                spacing="2",
            ),
            spacing="2",
            padding="1rem 1.1rem 1.1rem",
            align="start",
            width="100%",
        ),
        class_name=rx.cond(is_selected, "offer-card selected", "offer-card"),
        on_click=CheckoutState.seleccionar_oferta(o),
        cursor="pointer",
        width="100%",
    )


def paso2() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.button(
                "← Volver",
                on_click=CheckoutState.ir_paso(1),
                background="transparent",
                color="rgba(255,255,255,0.4)",
                border="1px solid rgba(255,255,255,0.1)",
                border_radius="8px",
                font_size="0.8rem",
                cursor="pointer",
                padding="0.4rem 0.8rem",
            ),
            rx.vstack(
                rx.text(
                    "Paso 2 de 5",
                    color=GOLD,
                    font_size="0.7rem",
                    text_transform="uppercase",
                    letter_spacing="2px",
                    font_weight="700",
                ),
                rx.heading(
                    "Elige tu experiencia",
                    style={
                        "fontFamily": "'Playfair Display', serif",
                        "fontSize": "clamp(1.5rem, 3vw, 2rem)",
                        "fontWeight": "800",
                        "color": TEXT_DARK,
                    },
                ),
                spacing="1",
                align="start",
            ),
            spacing="4",
            align="start",
            width="100%",
        ),

        rx.text(
            CheckoutState.pais_nombre,
            color=TEXT_MUTED,
            font_size="0.85rem",
        ),

        rx.cond(
            CheckoutState.pais_id == "rd",
            rx.grid(
                *[oferta_card_item(o) for o in OFERTAS_POR_PAIS["rd"]],
                style={"gridTemplateColumns": "repeat(auto-fit, minmax(260px, 1fr))"},
                gap="1rem",
                width="100%",
            ),
            rx.cond(
                CheckoutState.pais_id == "pr",
                rx.grid(
                    *[oferta_card_item(o) for o in OFERTAS_POR_PAIS["pr"]],
                    style={"gridTemplateColumns": "repeat(auto-fit, minmax(260px, 1fr))"},
                    gap="1rem",
                    width="100%",
                ),
                rx.cond(
                    CheckoutState.pais_id == "co",
                    rx.grid(
                        *[oferta_card_item(o) for o in OFERTAS_POR_PAIS["co"]],
                        style={"gridTemplateColumns": "repeat(auto-fit, minmax(260px, 1fr))"},
                        gap="1rem",
                        width="100%",
                    ),
                    rx.cond(
                        CheckoutState.pais_id == "mx",
                        rx.grid(
                            *[oferta_card_item(o) for o in OFERTAS_POR_PAIS["mx"]],
                            style={"gridTemplateColumns": "repeat(auto-fit, minmax(260px, 1fr))"},
                            gap="1rem",
                            width="100%",
                        ),
                        rx.grid(
                            *[oferta_card_item(o) for o in OFERTAS_POR_PAIS["us"]],
                            style={"gridTemplateColumns": "repeat(auto-fit, minmax(260px, 1fr))"},
                            gap="1rem",
                            width="100%",
                        ),
                    ),
                ),
            ),
        ),

        class_name="step-panel",
        spacing="5",
        width="100%",
        align="start",
    )

# ─────────────────────────────────────────────────────────────────────────────
#  PASO 3 – DATOS DEL VIAJERO
# ─────────────────────────────────────────────────────────────────────────────

def field(label: str, component: rx.Component) -> rx.Component:
    return rx.vstack(
        rx.text(
            label,
            color="rgba(255,255,255,0.5)",
            font_size="0.7rem",
            font_weight="600",
            text_transform="uppercase",
            letter_spacing="0.8px",
        ),
        component,
        spacing="1",
        width="100%",
        align="start",
    )


def styled_input(placeholder: str, value, on_change, input_type: str = "text") -> rx.Component:
    return rx.input(
        placeholder=placeholder,
        value=value,
        on_change=on_change,
        type=input_type,
        class_name="premium-input",
        style={
            "background": "rgba(255,255,255,0.05)",
            "border": "1.5px solid rgba(255,255,255,0.1)",
            "borderRadius": "12px",
          "color": TEXT_DARK,
            "padding": "0.8rem 1.1rem",
            "fontSize": "0.92rem",
            "width": "100%",
        },
    )


def paso3() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.button(
                "← Volver",
                on_click=CheckoutState.ir_paso(2),
                background="transparent",
                color="rgba(255,255,255,0.4)",
                border="1px solid rgba(255,255,255,0.1)",
                border_radius="8px",
                font_size="0.8rem",
                cursor="pointer",
                padding="0.4rem 0.8rem",
            ),
            rx.vstack(
                rx.text(
                    "Paso 3 de 5",
                    color=GOLD,
                    font_size="0.7rem",
                    text_transform="uppercase",
                    letter_spacing="2px",
                    font_weight="700",
                ),
                rx.heading(
                    "Datos del viajero",
                    style={
                        "fontFamily": "'Playfair Display', serif",
                        "fontSize": "clamp(1.5rem, 3vw, 2rem)",
                        "fontWeight": "800",
                       "color": TEXT_DARK,
                    },
                ),
                spacing="1",
                align="start",
            ),
            spacing="4",
            align="start",
            width="100%",
        ),

        rx.grid(
            field("Nombre completo *",
                styled_input("Ej: Juan García", CheckoutState.nombre, CheckoutState.set_nombre)
            ),
            field("Correo electrónico *",
                styled_input("tu@email.com", CheckoutState.email, CheckoutState.set_email, "email")
            ),
            field("Teléfono",
                styled_input("+1 (000) 000-0000", CheckoutState.telefono, CheckoutState.set_telefono, "tel")
            ),
            field("Fecha de viaje *",
                styled_input("", CheckoutState.fecha_viaje, CheckoutState.set_fecha, "date")
            ),
            field("Cantidad de personas",
                rx.select(
                    ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
                    value=CheckoutState.personas,
                    on_change=CheckoutState.set_personas,
                    style={
                        "background": "rgba(255,255,255,0.05)",
                        "border": "1.5px solid rgba(255,255,255,0.1)",
                        "borderRadius": "12px",
                        "color": TEXT_DARK,
                        "padding": "0.8rem 1.1rem",
                        "fontSize": "0.92rem",
                        "width": "100%",
                    },
                ),
            ),
            style={"gridTemplateColumns": "1fr 1fr"},
            gap="1.2rem",
            width="100%",
        ),

        field("Comentarios adicionales",
            rx.text_area(
                placeholder="Peticiones especiales, alergias, necesidades...",
                value=CheckoutState.comentarios,
                on_change=CheckoutState.set_comentarios,
                style={
                    "background": "rgba(255,255,255,0.05)",
                    "border": "1.5px solid rgba(255,255,255,0.1)",
                    "borderRadius": "12px",
                    "color": TEXT_DARK,
                    "padding": "0.8rem 1.1rem",
                    "fontSize": "0.88rem",
                    "width": "100%",
                    "minHeight": "100px",
                    "resize": "vertical",
                },
            ),
        ),

        rx.button(
            "Continuar al pago →",
            on_click=CheckoutState.ir_paso(4),
            style={
                "background": f"linear-gradient(135deg, {TEAL}, {TEAL_LT})",
                "color": TEXT_DARK,
                "border": "none",
                "borderRadius": "14px",
                "padding": "0.9rem 2rem",
                "fontWeight": "800",
                "fontSize": "0.95rem",
                "cursor": "pointer",
                "width": "100%",
                "transition": "all 0.25s",
            },
        ),

        class_name="step-panel",
        spacing="5",
        width="100%",
        align="start",
    )


# ─────────────────────────────────────────────────────────────────────────────
#  PASO 4 – MÉTODO DE PAGO
# ─────────────────────────────────────────────────────────────────────────────

def pay_method_btn(label: str, icon: str, value: str) -> rx.Component:
    is_selected = CheckoutState.metodo_pago == value
    return rx.box(
        rx.hstack(
            rx.text(icon, font_size="1.2rem"),
            rx.text(
                label,
                color=rx.cond(is_selected, GOLD_LT, "rgba(255,255,255,0.65)"),
                font_size="0.88rem",
                font_weight=rx.cond(is_selected, "700", "500"),
            ),
            spacing="2",
            align="center",
        ),
        class_name=rx.cond(is_selected, "pay-btn selected", "pay-btn"),
        on_click=CheckoutState.set_metodo(value),
        flex="1",
        justify="center",
        display="flex",
    )


def card_form() -> rx.Component:
    return rx.vstack(
        # Tarjeta visual preview
        rx.box(
            rx.hstack(
                rx.vstack(
                    rx.text("TRAVELWORLD CARD", color=GOLD, font_size="0.6rem", letter_spacing="2px", font_weight="700"),
                    rx.spacer(),
                    rx.text(
                        rx.cond(
                            CheckoutState.card_num != "",
                            CheckoutState.card_num,
                            "•••• •••• •••• ••••",
                        ),
                        color="rgba(255,255,255,0.9)",
                        font_size="1.15rem",
                        letter_spacing="3px",
                        font_family="monospace",
                    ),
                    rx.hstack(
                        rx.vstack(
                            rx.text("TITULAR", color="rgba(255,255,255,0.4)", font_size="0.55rem", letter_spacing="1px"),
                            rx.text(
                                rx.cond(
                                    CheckoutState.card_name != "",
                                    CheckoutState.card_name,
                                    "NOMBRE APELLIDO",
                                ),
                               color=TEXT_DARK, font_size="0.78rem", font_weight="600",
                            ),
                            spacing="0",
                        ),
                        rx.spacer(),
                        rx.vstack(
                            rx.text("VENCE", color="rgba(255,255,255,0.4)", font_size="0.55rem", letter_spacing="1px"),
                            rx.text(
                                rx.cond(CheckoutState.card_exp != "", CheckoutState.card_exp, "MM/AA"),
                               color=TEXT_DARK, font_size="0.78rem", font_weight="600",
                            ),
                            spacing="0",
                        ),
                        width="100%",
                        align="center",
                    ),
                    spacing="2",
                    flex="1",
                    height="100%",
                    justify="between",
                ),
                rx.text(
                    "VISA",
                    style={
                        "fontFamily": "'Playfair Display', serif",
                        "fontSize": "1.4rem",
                        "fontWeight": "900",
                        "background": f"linear-gradient(135deg, {GOLD_LT}, {GOLD})",
                        "WebkitBackgroundClip": "text",
                        "WebkitTextFillColor": "transparent",
                        "backgroundClip": "text",
                        "fontStyle": "italic",
                    },
                    align_self="end",
                ),
                width="100%",
                height="100%",
                padding="1.5rem",
                align="start",
            ),
            class_name="credit-card-preview",
            height="170px",
            width="100%",
        ),

        # Campos de tarjeta
        rx.grid(
            field("Número de tarjeta",
                styled_input("0000 0000 0000 0000", CheckoutState.card_num, CheckoutState.set_card_num)
            ),
            field("Nombre del titular",
                styled_input("Como aparece en la tarjeta", CheckoutState.card_name, CheckoutState.set_card_name)
            ),
            field("Fecha de vencimiento",
                styled_input("MM/AA", CheckoutState.card_exp, CheckoutState.set_card_exp)
            ),
            field("CVV",
                styled_input("•••", CheckoutState.card_cvv, CheckoutState.set_card_cvv)
            ),
            style={"gridTemplateColumns": "1fr 1fr"},
            gap="1.1rem",
            width="100%",
        ),

        spacing="4",
        width="100%",
    )


def paypal_form() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text("🅿️", font_size="3rem"),
            rx.text("PayPal", style={
                "fontFamily": "'Playfair Display', serif",
                "fontSize": "1.5rem",
                "fontWeight": "700",
                "color": "#003087",
            }),
            rx.text(
                "Serás redirigido a PayPal para completar el pago de forma segura.",
                color="rgba(255,255,255,0.5)",
                font_size="0.85rem",
                text_align="center",
                max_width="280px",
            ),
            spacing="3",
            align="center",
        ),
        background="rgba(0,48,135,0.1)",
        border="1px solid rgba(0,48,135,0.3)",
        border_radius="16px",
        padding="2rem",
        width="100%",
        display="flex",
        justify="center",
    )


def transfer_form() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text("🏦", font_size="2rem"),
            rx.text("Transferencia Bancaria", color=TEXT_DARK, font_weight="700", font_size="1rem"),
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.text("Banco:", color="rgba(255,255,255,0.4)", font_size="0.82rem", width="100px"),
                        rx.text("Banco Popular Dominicano",color=TEXT_DARK, font_size="0.82rem", font_weight="600"),
                    ),
                    rx.hstack(
                        rx.text("Cuenta:", color="rgba(255,255,255,0.4)", font_size="0.82rem", width="100px"),
                        rx.text("000-000000-0", color=TEXT_DARK, font_size="0.82rem", font_weight="600"),
                    ),
                    rx.hstack(
                        rx.text("Titular:", color="rgba(255,255,255,0.4)", font_size="0.82rem", width="100px"),
                        rx.text("TravelWorld SRL", color=TEXT_DARK, font_size="0.82rem", font_weight="600"),
                    ),
                    spacing="2",
                    align="start",
                ),
                background="rgba(255,255,255,0.04)",
                border="1px solid rgba(255,255,255,0.08)",
                border_radius="12px",
                padding="1rem",
                width="100%",
            ),
            rx.text(
                "Envía el comprobante a reservas@travelworld.com",
                color=GOLD,
                font_size="0.78rem",
                text_align="center",
            ),
            spacing="3",
            align="center",
            width="100%",
        ),
        width="100%",
    )


def paso4() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.button(
                "← Volver",
                on_click=CheckoutState.ir_paso(3),
                background="transparent",
                color="rgba(255,255,255,0.4)",
                border="1px solid rgba(255,255,255,0.1)",
                border_radius="8px",
                font_size="0.8rem",
                cursor="pointer",
                padding="0.4rem 0.8rem",
            ),
            rx.vstack(
                rx.text(
                    "Paso 4 de 5",
                    color=GOLD,
                    font_size="0.7rem",
                    text_transform="uppercase",
                    letter_spacing="2px",
                    font_weight="700",
                ),
                rx.heading(
                    "Método de pago",
                    style={
                        "fontFamily": "'Playfair Display', serif",
                        "fontSize": "clamp(1.5rem, 3vw, 2rem)",
                        "fontWeight": "800",
                        "color": TEXT_DARK,
                    },
                ),
                spacing="1",
                align="start",
            ),
            spacing="4",
            align="start",
            width="100%",
        ),

        # Selector de método
        rx.hstack(
            pay_method_btn("Tarjeta", "💳", "Tarjeta"),
            pay_method_btn("PayPal", "🅿️", "PayPal"),
            pay_method_btn("Transferencia", "🏦", "Transferencia"),
            spacing="3",
            width="100%",
        ),

        # Formulario dinámico por método
        rx.cond(
            CheckoutState.metodo_pago == "Tarjeta",
            card_form(),
            rx.cond(
                CheckoutState.metodo_pago == "PayPal",
                paypal_form(),
                transfer_form(),
            ),
        ),

        rx.button(
            "Revisar y confirmar →",
            on_click=CheckoutState.ir_paso(5),
            style={
                "background": f"linear-gradient(135deg, {TEAL}, {TEAL_LT})",
                "color": TEXT_DARK,
                "border": "none",
                "borderRadius": "14px",
                "padding": "0.9rem 2rem",
                "fontWeight": "800",
                "fontSize": "0.95rem",
                "cursor": "pointer",
                "width": "100%",
                "transition": "all 0.25s",
            },
        ),

        class_name="step-panel",
        spacing="5",
        width="100%",
        align="start",
    )


# ─────────────────────────────────────────────────────────────────────────────
#  PASO 5 – CONFIRMACIÓN FINAL
# ─────────────────────────────────────────────────────────────────────────────

def resumen_row(label: str, value) -> rx.Component:
    return rx.hstack(
        rx.text(label, color="rgba(255,255,255,0.4)", font_size="0.82rem", min_width="120px"),
        rx.text(value, color=TEXT_DARK, font_size="0.88rem", font_weight="600"),
        width="100%",
        spacing="3",
        align="start",
    )


def paso5() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.button(
                "← Volver",
                on_click=CheckoutState.ir_paso(4),
                background="transparent",
                color="rgba(255,255,255,0.4)",
                border="1px solid rgba(255,255,255,0.1)",
                border_radius="8px",
                font_size="0.8rem",
                cursor="pointer",
                padding="0.4rem 0.8rem",
            ),
            rx.vstack(
                rx.text(
                    "Paso 5 de 5",
                    color=GOLD,
                    font_size="0.7rem",
                    text_transform="uppercase",
                    letter_spacing="2px",
                    font_weight="700",
                ),
                rx.heading(
                    "Confirma tu reserva",
                    style={
                        "fontFamily": "'Playfair Display', serif",
                        "fontSize": "clamp(1.5rem, 3vw, 2rem)",
                        "fontWeight": "800",
                        "color": TEXT_DARK,
                    },
                ),
                spacing="1",
                align="start",
            ),
            spacing="4",
            align="start",
            width="100%",
        ),

        # Resumen completo
        rx.box(
            rx.vstack(
                rx.text(
                    "Detalle de tu reserva",
                    color="rgba(255,255,255,0.4)",
                    font_size="0.68rem",
                    text_transform="uppercase",
                    letter_spacing="2px",
                    font_weight="600",
                ),
                rx.box(height="1px", width="100%", background="rgba(255,255,255,0.07)"),
                resumen_row("Destino", CheckoutState.pais_nombre),
                resumen_row("Oferta", CheckoutState.oferta_nombre),
                resumen_row("Duración", CheckoutState.oferta_duracion),
                resumen_row("Nombre", CheckoutState.nombre),
                resumen_row("Email", CheckoutState.email),
                resumen_row("Teléfono", CheckoutState.telefono),
                resumen_row("Fecha de viaje", CheckoutState.fecha_viaje),
                resumen_row("Personas", CheckoutState.personas),
                resumen_row("Método de pago", CheckoutState.metodo_pago),
                rx.box(height="1px", width="100%", background="rgba(255,255,255,0.07)"),
                rx.hstack(
                    rx.text("TOTAL A PAGAR", color=TEXT_MUTED, font_size="0.75rem", font_weight="700", letter_spacing="1px"),
                    rx.spacer(),
                    rx.text(
                        "$",
                        CheckoutState.precio_total.to_string(),
                        " USD",
                        style={
                            "fontFamily": "'Playfair Display', serif",
                            "fontSize": "2rem",
                            "fontWeight": "900",
                            "background": f"linear-gradient(135deg, {GOLD}, {GOLD_LT})",
                            "WebkitBackgroundClip": "text",
                            "WebkitTextFillColor": "transparent",
                            "backgroundClip": "text",
                        },
                    ),
                    width="100%",
                    align="end",
                ),
                spacing="3",
                align="start",
                width="100%",
            ),
            background="rgba(255,255,255,0.04)",
            border=f"1px solid {GLASS_BOR}",
            border_radius="18px",
            padding="1.5rem",
            width="100%",
        ),

        # Mensaje de error si hay
        rx.cond(
            CheckoutState.mensaje != "",
            rx.text(CheckoutState.mensaje, color=CORAL, font_size="0.88rem"),
            rx.box(),
        ),

        # Botón confirmar
        rx.box(
            rx.button(
                "🔒  Confirmar y Reservar Ahora",
                on_click=CheckoutState.confirmar_reserva,
                class_name="confirm-btn",
                style={
                    "background": f"linear-gradient(135deg, {GOLD}, {GOLD_LT}, {GOLD})",
                    "backgroundSize": "200% 100%",
                    "color": DARK,
                    "border": "none",
                    "borderRadius": "16px",
                    "padding": "1.1rem 2rem",
                    "fontWeight": "900",
                    "fontSize": "1rem",
                    "cursor": "pointer",
                    "width": "100%",
                    "letterSpacing": "0.5px",
                    "boxShadow": f"0 12px 40px rgba(201,168,76,0.3)",
                    "transition": "all 0.3s",
                },
            ),
            width="100%",
        ),

        rx.text(
            "🔒 Pago seguro SSL · Datos encriptados · Cancelación flexible",
            color="rgba(255,255,255,0.25)",
            font_size="0.7rem",
            text_align="center",
            width="100%",
        ),

        class_name="step-panel",
        spacing="5",
        width="100%",
        align="start",
    )


# ─────────────────────────────────────────────────────────────────────────────
#  PASO 6 – ÉXITO
# ─────────────────────────────────────────────────────────────────────────────

def paso6_success() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.box(
                rx.text("✓", color=TEXT_DARK, font_size="2rem", font_weight="900"),
                width="72px",
                height="72px",
                border_radius="50%",
                background=f"linear-gradient(135deg, {TEAL}, {TEAL_LT})",
                display="flex",
                align="center",
                justify="center",
                box_shadow=f"0 0 40px rgba(11,110,110,0.5)",
                style={"animation": "glowPulse 2s infinite"},
            ),
            rx.heading(
                "¡Reserva Confirmada!",
                style={
                    "fontFamily": "'Playfair Display', serif",
                    "fontSize": "clamp(1.8rem, 4vw, 2.5rem)",
                    "fontWeight": "900",
                    "background": f"linear-gradient(135deg, {GOLD}, {GOLD_LT})",
                    "WebkitBackgroundClip": "text",
                    "WebkitTextFillColor": "transparent",
                    "backgroundClip": "text",
                },
            ),
            rx.text(
                CheckoutState.mensaje,
                color="rgba(255,255,255,0.65)",
                font_size="0.95rem",
                text_align="center",
                max_width="400px",
            ),
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.text("Destino", color="rgba(255,255,255,0.4)", font_size="0.8rem", min_width="90px"),
                        rx.text(CheckoutState.pais_nombre, color=TEXT_DARK, font_size="0.88rem", font_weight="700"),
                    ),
                    rx.hstack(
                        rx.text("Paquete", color="rgba(255,255,255,0.4)", font_size="0.8rem", min_width="90px"),
                        rx.text(CheckoutState.oferta_nombre, color=TEXT_DARK, font_size="0.88rem", font_weight="700"),
                    ),
                    rx.hstack(
                        rx.text("Fecha", color="rgba(255,255,255,0.4)", font_size="0.8rem", min_width="90px"),
                        rx.text(CheckoutState.fecha_viaje, color=TEXT_DARK, font_size="0.88rem", font_weight="700"),
                    ),
                    rx.hstack(
                        rx.text("Total", color="rgba(255,255,255,0.4)", font_size="0.8rem", min_width="90px"),
                        rx.text(
                            "$",
                            CheckoutState.precio_total.to_string(),
                            " USD",
                            color=GOLD,
                            font_size="1rem",
                            font_weight="900",
                            font_family="'Playfair Display', serif",
                        ),
                    ),
                    spacing="3",
                    align="start",
                ),
                background="rgba(255,255,255,0.05)",
                border=f"1px solid {GOLD_BOR}",
                border_radius="16px",
                padding="1.5rem 2rem",
                min_width="320px",
            ),
            rx.link(
                rx.button(
                    "← Volver al inicio",
                    style={
                        "background": f"linear-gradient(135deg, {GOLD}, {GOLD_LT})",
                        "color": DARK,
                        "border": "none",
                        "borderRadius": "14px",
                        "padding": "0.9rem 2.5rem",
                        "fontWeight": "800",
                        "fontSize": "0.95rem",
                        "cursor": "pointer",
                    },
                ),
                href="/",
            ),
            spacing="6",
            align="center",
            class_name="step-panel",
        ),
        min_height="70vh",
        width="100%",
    )


# ─────────────────────────────────────────────────────────────────────────────
#  NAVBAR
# ─────────────────────────────────────────────────────────────────────────────

def checkout_navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.link(
                rx.text(
                    "TravelWorld",
                    style={
                        "fontFamily": "'Playfair Display', serif",
                        "fontSize": "1.4rem",
                        "fontWeight": "900",
                        "background": f"linear-gradient(135deg, #8B6A2E, {GOLD}, #A8753B)",
                        "WebkitBackgroundClip": "text",
                        "WebkitTextFillColor": "transparent",
                        "backgroundClip": "text",
                        "letterSpacing": "2px",
                    },
                ),
                href="/",
            ),
            rx.spacer(),
            rx.hstack(
                rx.text("🔒", font_size="0.8rem"),
                rx.text(
                    "Checkout seguro",
                    color=TEXT_MUTED,
                    font_size="0.8rem",
                ),
                spacing="1",
                align="center",
            ),
            width="100%",
            max_width="1300px",
            margin="0 auto",
            padding="0 2rem",
            align="center",
        ),
        position="sticky",
        top="0",
        z_index="100",
        background="rgba(253,249,243,0.92)",
        style={"backdropFilter": "blur(20px)"},
        border_bottom=f"1px solid {GOLD_BOR}",
        height="64px",
        display="flex",
        align="center",
        width="100%",
    )


# ─────────────────────────────────────────────────────────────────────────────
#  PÁGINA COMPLETA
# ─────────────────────────────────────────────────────────────────────────────

def hero_reservas() -> rx.Component:
    return rx.box(
        rx.box(
            position="absolute",
            inset="0",
            background="linear-gradient(90deg, rgba(43,36,26,0.62), rgba(43,36,26,0.18))",
            z_index="1",
        ),
        rx.vstack(
            rx.text(
                "✦ Experiencias familiares premium ✦",
                color=GOLD_LT,
                font_size="0.8rem",
                text_transform="uppercase",
                letter_spacing="3px",
                font_weight="800",
            ),
            rx.heading(
                "Reserva el viaje perfecto para tu familia",
                color="white",
                font_size="clamp(2rem, 5vw, 4.2rem)",
                font_family="'Playfair Display', serif",
                font_weight="900",
                max_width="700px",
                line_height="0.95",
            ),
            rx.text(
                "Hoteles, resorts, Disney, playas y aventuras inolvidables en un solo lugar.",
                color="rgba(255,255,255,0.9)",
                font_size="1.05rem",
                max_width="620px",
            ),
            spacing="3",
            align="start",
            position="relative",
            z_index="2",
            padding="5rem 4rem",
        ),
        style={
            "backgroundImage": "url('/images/familia_viajando.jpg')",
            "backgroundSize": "cover",
            "backgroundPosition": "center",
        },
        min_height="380px",
        position="relative",
        width="100%",
    )









def reservas() -> rx.Component:
    return rx.box(
        rx.html(f"<style>{CHECKOUT_CSS}</style>"),
        checkout_navbar(),
        hero_reservas(),

        rx.cond(
            CheckoutState.paso == 6,
            paso6_success(),
            rx.box(
                rx.box(
                    rx.vstack(
                        rx.text(
                            "✦  Checkout Premium  ✦",
                            color=GOLD,
                            font_size="0.72rem",
                            text_transform="uppercase",
                            letter_spacing="3px",
                            font_weight="700",
                        ),
                        rx.heading(
                            "Reserva tu aventura",
                            style={
                                "fontFamily": "'Playfair Display', serif",
                                "fontSize": "clamp(1.5rem, 3vw, 2.2rem)",
                                "fontWeight": "900",
                                "color": TEXT_DARK,
                            },
                        ),
                        progress_bar(),
                        spacing="4",
                        align="center",
                        max_width="1300px",
                        margin="0 auto",
                        padding="0 2rem",
                        width="100%",
                    ),
                    padding="2.5rem 0",
                    border_bottom="1px solid rgba(139,106,46,0.12)",
                    width="100%",
                ),

                rx.hstack(
                    rx.box(
                        rx.cond(CheckoutState.paso == 1, paso1(), rx.box()),
                        rx.cond(CheckoutState.paso == 2, paso2(), rx.box()),
                        rx.cond(CheckoutState.paso == 3, paso3(), rx.box()),
                        rx.cond(CheckoutState.paso == 4, paso4(), rx.box()),
                        rx.cond(CheckoutState.paso == 5, paso5(), rx.box()),
                        flex="1",
                        min_width="0",
                    ),
                    rx.box(
                        summary_panel(),
                        width="360px",
                        flex_shrink="0",
                        display=["none", "none", "block"],
                    ),
                    spacing="8",
                    align="start",
                    width="100%",
                    max_width="1300px",
                    margin="0 auto",
                    padding="3rem 2rem",
                ),
                width="100%",
            ),
        ),

        background=DARK,
        min_height="100vh",
        width="100%",
    )