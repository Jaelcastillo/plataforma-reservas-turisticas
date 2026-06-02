import reflex as rx
from turismo_reservas.states.auth_state import AuthState

GOLD = "#C9A84C"
GOLD_LT = "#E8C96A"
TEXT_D = "#2A1F14"
TEXT_S = "#6B5A45"

LOGIN_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500;600&display=swap');

* { box-sizing: border-box; }

.auth-wrap {
    display: grid;
    grid-template-columns: 1fr 0.72fr;
    min-height: 100vh;
    font-family: 'DM Sans', sans-serif;
}

.auth-left {
    position: relative;
    padding: 4rem;
    display: flex;
    align-items: flex-end;
    overflow: hidden;
    background:
        linear-gradient(90deg, rgba(5,15,25,.86), rgba(5,15,25,.55)),
        url('/images/resort_bg.jpg') center/cover no-repeat;
}

.auth-left-content {
    position: relative;
    z-index: 2;
    max-width: 560px;
}

.auth-logo {
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    font-weight: 900;
    letter-spacing: 2px;
    color: white;
    margin-bottom: 2rem;
}

.auth-logo span { color: #C9A84C; }

.auth-quote {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2rem, 4vw, 3.4rem);
    font-weight: 900;
    color: #fff8ec;
    line-height: 1.12;
    margin-bottom: 1rem;
}

.auth-quote-sub {
    color: rgba(255,255,255,.72);
    font-size: 1rem;
}

.auth-badges {
    display: flex;
    gap: .8rem;
    margin-top: 2rem;
    flex-wrap: wrap;
}

.auth-badge {
    color: #E8C96A;
    border: 1px solid rgba(201,168,76,.45);
    background: rgba(201,168,76,.12);
    padding: .45rem .95rem;
    border-radius: 999px;
    font-size: .72rem;
    font-weight: 800;
    letter-spacing: 1px;
}

.auth-right {
    background:
        radial-gradient(circle at top right, rgba(201,168,76,.16), transparent 35%),
        linear-gradient(180deg, #FAF9F6, #F4F1EA);
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 2.5rem;
}

.auth-card {
    width: 100%;
    max-width: 450px;
    background: rgba(255,255,255,.86);
    border: 1px solid rgba(201,168,76,.30);
    border-radius: 30px;
    padding: 2.8rem 2.4rem;
    box-shadow: 0 28px 80px rgba(43,36,26,.16);
}

.tw-field {
    position: relative;
    width: 100%;
}

.tw-field-icon {
    position: absolute;
    left: 16px;
    top: 50%;
    transform: translateY(-50%);
    z-index: 2;
}

.tw-input-styled {
    width: 100% !important;
    height: 56px !important;
    padding: 0 1rem 0 3rem !important;
    background: white !important;
    border: 1.5px solid #E1D2BE !important;
    border-radius: 16px !important;
    color: #2A1F14 !important;
    font-size: 1rem !important;
    font-weight: 600 !important;
}

.tw-input-styled::placeholder {
    color: #A99882 !important;
}

.tw-input-styled:focus {
    border-color: #C9A84C !important;
    box-shadow: 0 0 0 4px rgba(201,168,76,.13) !important;
}

.btn-gold {
    width: 100%;
    height: 56px;
    background: linear-gradient(135deg, #8B6A2E, #C9A84C, #E8C96A);
    color: white;
    border: none;
    border-radius: 16px;
    font-weight: 900;
    font-size: 1rem;
    cursor: pointer;
    box-shadow: 0 14px 35px rgba(201,168,76,.38);
}

.btn-back {
    background: transparent;
    border: 1.5px solid #D8C7B0;
    border-radius: 14px;
    color: #6B5A45;
    padding: .7rem 1.5rem;
    font-weight: 700;
    cursor: pointer;
}

.auth-divider {
    display: flex;
    align-items: center;
    gap: .8rem;
    width: 100%;
}

.auth-divider-line {
    flex: 1;
    height: 1px;
    background: #E1D2BE;
}

.msg-ok {
    background: rgba(26,122,110,.08);
    border: 1px solid rgba(26,122,110,.22);
    color: #1A7A6E;
    padding: .8rem 1rem;
    border-radius: 12px;
    text-align: center;
    font-weight: 700;
}

@media (max-width: 850px) {
    .auth-wrap { grid-template-columns: 1fr; }
    .auth-left { min-height: 360px; padding: 2rem; }
}
"""


def _field(icon: str, placeholder: str, value, on_change, type_: str = "text") -> rx.Component:
    return rx.box(
        rx.html(f'<span class="tw-field-icon">{icon}</span>'),
        rx.input(
            placeholder=placeholder,
            value=value,
            on_change=on_change,
            type=type_,
            class_name="tw-input-styled",
        ),
        class_name="tw-field",
    )


def login() -> rx.Component:
    return rx.box(
        rx.html(f"<style>{LOGIN_CSS}</style>"),
        rx.box(
            rx.box(
                rx.box(
                    rx.html('<div class="auth-logo">Travel<span>World</span></div>'),
                    rx.html(
                        '<p class="auth-quote">"El mundo es un libro,<br>'
                        'y quienes no viajan<br>solo leen una página."</p>'
                        '<p class="auth-quote-sub">— San Agustín</p>'
                        '<div class="auth-badges">'
                        '<span class="auth-badge">🏝 Caribe</span>'
                        '<span class="auth-badge">✨ Disney</span>'
                        '<span class="auth-badge">🌊 Resorts</span>'
                        '<span class="auth-badge">🏎 Tours</span>'
                        '</div>'
                    ),
                    class_name="auth-left-content",
                ),
                class_name="auth-left",
            ),
            rx.box(
                rx.vstack(
                    rx.vstack(
                       rx.box(
    rx.text( font_size="1.35rem", line_height="1"),
    width="62px",
    height="62px",
    border_radius="50%",
    background="rgba(201,168,76,0.12)",
    border=f"1px solid {GOLD}",
    display="flex",
    align="center",
    justify="center",
    
),
                        rx.heading(
                            "Bienvenido de nuevo",
                            style={
                                "fontFamily": "'Playfair Display', serif",
                                "fontSize": "2.45rem",
                                "fontWeight": "900",
                                "color": "#1F160F",
                                "textAlign": "center",
                                "lineHeight": "1.05",
                            },
                        ),
                        rx.box(
                            width="120px",
                            height="2px",
                            background=f"linear-gradient(90deg, transparent, {GOLD}, transparent)",
                        ),
                        rx.text(
                            "Accede a tu cuenta TravelWorld",
                            font_size="1rem",
                            color="#5C4E3A",
                            text_align="center",
                        ),
                        spacing="3",
                        align="center",
                        width="100%",
                    ),
                    rx.vstack(
                        _field("📧", "Correo electrónico", AuthState.email, AuthState.set_email, "email"),
                        _field("🔒", "Contraseña", AuthState.password, AuthState.set_password, "password"),
                        spacing="4",
                        width="100%",
                    ),
                    rx.cond(
                        AuthState.mensaje != "",
                        rx.box(rx.text(AuthState.mensaje), class_name="msg-ok"),
                        rx.box(),
                    ),
                    rx.button(
                        "🗝 Iniciar sesión",
                        on_click=AuthState.login,
                        class_name="btn-gold",
                        width="100%",
                    ),
                    rx.html(
                        '<div class="auth-divider">'
                        '<div class="auth-divider-line"></div>'
                        '<span style="font-size:.78rem;color:#A99882;">¿Nuevo aquí?</span>'
                        '<div class="auth-divider-line"></div>'
                        '</div>'
                    ),
                    rx.link(
                        rx.text(
                            "¿No tienes cuenta? ",
                            rx.text.span("Regístrate", color=GOLD, font_weight="900", text_decoration="underline"),
                            color=TEXT_S,
                            text_align="center",
                        ),
                        href="/registro",
                    ),
                    rx.link(
                        rx.html('<button class="btn-back">← Volver al inicio</button>'),
                        href="/",
                    ),
                    spacing="5",
                    width="100%",
                    class_name="auth-card",
                ),
                class_name="auth-right",
            ),
            class_name="auth-wrap",
        ),
        width="100%",
        min_height="100vh",
    )