import io
import qrcode
from pathlib import Path
from datetime import datetime

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    HRFlowable,
    Image,
)


CREMA = colors.HexColor("#F5EFE6")
DORADO = colors.HexColor("#C9A84C")
TEXTO_OSC = colors.HexColor("#2B241A")
TEXTO_MED = colors.HexColor("#5C4E3A")
GRIS_SUAVE = colors.HexColor("#EDE6DA")
GRIS_LINEA = colors.HexColor("#D4C9B5")
VERDE_OK = colors.HexColor("#2E7D52")
BLANCO = colors.white


def generar_qr(codigo: str) -> io.BytesIO:
    qr = qrcode.QRCode(version=2, box_size=6, border=2)
    qr.add_data(f"https://travelworld.com/reserva/{codigo}")
    qr.make(fit=True)

    img = qr.make_image(fill_color="#2B241A", back_color="#F5EFE6")
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return buf


def local_image_path(url_imagen: str | None) -> str | None:
    if not url_imagen:
        return None

    clean = url_imagen.lstrip("/")

    if clean.startswith("images/"):
        path = Path("assets") / clean
    else:
        path = Path(clean)

    if path.exists():
        return str(path)

    return None


def generar_pdf_reserva(datos: dict, output_path: str | None = None) -> str:
    d = {
        "codigo_reserva": f"TW-{datetime.now().strftime('%Y%m%d%H%M%S')}",
        "fecha_emision": datetime.now().strftime("%d/%m/%Y"),
        "nombre_paquete": "Reserva TravelWorld",
        "destino": "Destino",
        "duracion": "N/A",
        "categoria": "Reserva TravelWorld",
        "url_imagen": None,
        "cliente_nombre": "",
        "cliente_email": "",
        "cliente_telefono": "",
        "viajeros": 1,
        "fecha_viaje": "",
        "metodo_pago": "",
        "comentarios": "",
        "precio_base": 0.0,
        "descuento": 0.0,
        "impuestos": 0.0,
        "total_pagado": 0.0,
        "moneda": "USD",
    }

    d.update(datos)

    carpeta = Path(".web/public//comprobantes")
    carpeta.mkdir(parents=True, exist_ok=True)

    if output_path is None:
       output_path = str(carpeta / f"{d['codigo_reserva']}.pdf")

    W, H = A4
    margen = 1.8 * cm
    ancho = W - 2 * margen

    def style(
        name,
        size=10,
        color=TEXTO_OSC,
        bold=False,
        align=TA_LEFT,
        leading=None,
    ):
        return ParagraphStyle(
            name,
            fontName="Helvetica-Bold" if bold else "Helvetica",
            fontSize=size,
            textColor=color,
            alignment=align,
            leading=leading or size * 1.35,
        )

    styles = {
        "brand": style("brand", 22, DORADO, True),
        "small": style("small", 8, TEXTO_MED),
        "right": style("right", 9, TEXTO_MED, False, TA_RIGHT),
        "code": style("code", 16, DORADO, True, TA_RIGHT),
        "title": style("title", 20, TEXTO_OSC, True),
        "section": style("section", 11, DORADO, True),
        "label": style("label", 8, TEXTO_MED, True),
        "value": style("value", 10, TEXTO_OSC, True),
        "white": style("white", 12, BLANCO, True),
        "total": style("total", 22, DORADO, True, TA_RIGHT),
        "center": style("center", 9, TEXTO_MED, False, TA_CENTER),
    }

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=margen,
        rightMargin=margen,
        topMargin=margen,
        bottomMargin=1.4 * cm,
        title=f"Confirmación TravelWorld {d['codigo_reserva']}",
        author="TravelWorld",
    )

    story = []

    header = Table(
        [
            [
                Paragraph("TravelWorld", styles["brand"]),
                Table(
                    [
                        [Paragraph("Reserva Confirmada", styles["right"])],
                        [Paragraph(d["codigo_reserva"], styles["code"])],
                        [Paragraph(f"Emitido: {d['fecha_emision']}", styles["right"])],
                    ],
                    colWidths=[ancho * 0.45],
                ),
            ]
        ],
        colWidths=[ancho * 0.55, ancho * 0.45],
    )

    header.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )

    story.append(header)
    story.append(Paragraph("Tu agencia de viajes premium de confianza", styles["small"]))
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width=ancho, thickness=2, color=DORADO))
    story.append(Spacer(1, 14))

    img_path = local_image_path(d.get("url_imagen"))

    if img_path:
        story.append(Image(img_path, width=ancho, height=5.4 * cm))
    else:
        placeholder = Table(
            [[Paragraph(d["destino"].upper(), style("ph", 20, DORADO, True, TA_CENTER))]],
            colWidths=[ancho],
            rowHeights=[5.4 * cm],
        )
        placeholder.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, -1), TEXTO_OSC),
                    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ]
            )
        )
        story.append(placeholder)

    banner = Table(
        [
            [
                Paragraph(d["nombre_paquete"], styles["white"]),
                Paragraph("CONFIRMADO", style("ok", 10, BLANCO, True, TA_CENTER)),
            ],
            [
                Paragraph(f"{d['destino']} - {d['duracion']} - {d['categoria']}", style("bd", 9, DORADO)),
                "",
            ],
        ],
        colWidths=[ancho * 0.72, ancho * 0.28],
    )

    banner.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), TEXTO_OSC),
                ("BACKGROUND", (1, 0), (1, 0), VERDE_OK),
                ("SPAN", (1, 0), (1, 1)),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("TOPPADDING", (0, 0), (-1, -1), 9),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
                ("LEFTPADDING", (0, 0), (-1, -1), 12),
                ("RIGHTPADDING", (0, 0), (-1, -1), 12),
            ]
        )
    )

    story.append(banner)
    story.append(Spacer(1, 16))

    story.append(Paragraph("INFORMACIÓN DEL CLIENTE", styles["section"]))
    story.append(HRFlowable(width=ancho, thickness=1, color=DORADO))
    story.append(Spacer(1, 8))

    cliente = Table(
        [
            [
                Paragraph("Nombre", styles["label"]),
                Paragraph(d["cliente_nombre"], styles["value"]),
                Paragraph("Email", styles["label"]),
                Paragraph(d["cliente_email"], styles["value"]),
            ],
            [
                Paragraph("Teléfono", styles["label"]),
                Paragraph(d["cliente_telefono"], styles["value"]),
                Paragraph("Viajeros", styles["label"]),
                Paragraph(str(d["viajeros"]), styles["value"]),
            ],
        ],
        colWidths=[ancho * 0.18, ancho * 0.32, ancho * 0.18, ancho * 0.32],
    )

    cliente.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), GRIS_SUAVE),
                ("GRID", (0, 0), (-1, -1), 0.5, GRIS_LINEA),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )

    story.append(cliente)
    story.append(Spacer(1, 16))

    story.append(Paragraph("DETALLE DE LA RESERVA", styles["section"]))
    story.append(HRFlowable(width=ancho, thickness=1, color=DORADO))
    story.append(Spacer(1, 8))

    detalle = Table(
        [
            [Paragraph("Destino", styles["label"]), Paragraph(d["destino"], styles["value"])],
            [Paragraph("Paquete", styles["label"]), Paragraph(d["nombre_paquete"], styles["value"])],
            [Paragraph("Fecha del viaje", styles["label"]), Paragraph(d["fecha_viaje"], styles["value"])],
            [Paragraph("Duración", styles["label"]), Paragraph(d["duracion"], styles["value"])],
            [Paragraph("Método de pago", styles["label"]), Paragraph(d["metodo_pago"], styles["value"])],
            [Paragraph("Comentarios", styles["label"]), Paragraph(d.get("comentarios") or "Sin comentarios", styles["value"])],
        ],
        colWidths=[ancho * 0.30, ancho * 0.70],
    )

    detalle.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (0, -1), GRIS_SUAVE),
                ("GRID", (0, 0), (-1, -1), 0.5, GRIS_LINEA),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
            ]
        )
    )

    story.append(detalle)
    story.append(Spacer(1, 38))

    story.append(Paragraph("RESUMEN FINANCIERO", styles["section"]))
    story.append(HRFlowable(width=ancho, thickness=1, color=DORADO))
    story.append(Spacer(1, 14))

    moneda = d["moneda"]

    financiero = Table(
        [
            ["Precio base", f"{moneda} {float(d['precio_base']):,.2f}"],
            ["Descuento", f"{moneda} {float(d['descuento']):,.2f}"],
            ["Impuestos", f"{moneda} {float(d['impuestos']):,.2f}"],
        ],
        colWidths=[ancho * 0.55, ancho * 0.45],
    )

    financiero.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), GRIS_SUAVE),
            ("GRID", (0, 0), (-1, -1), 0.5, GRIS_LINEA),
            ("ALIGN", (1, 0), (1, -1), "RIGHT"),
            ("TOPPADDING", (0, 0), (-1, -1), 9),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
            ("LEFTPADDING", (0, 0), (-1, -1), 12),
            ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ])
    )

    total = Table(
        [[
            Paragraph("TOTAL PAGADO", style("tl", 11, BLANCO, True)),
            Paragraph(f"{moneda} {float(d['total_pagado']):,.2f}", styles["total"]),
        ]],
        colWidths=[ancho * 0.45, ancho * 0.55],
    )

    total.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), TEXTO_OSC),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("ALIGN", (1, 0), (1, 0), "RIGHT"),
            ("TOPPADDING", (0, 0), (-1, -1), 14),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 14),
            ("LEFTPADDING", (0, 0), (-1, -1), 14),
            ("RIGHTPADDING", (0, 0), (-1, -1), 14),
        ])
    )

    story.append(financiero)
    story.append(total)
    story.append(Spacer(1, 18))

    qr_img = Image(
        generar_qr(d["codigo_reserva"]),
        width=2.8 * cm,
        height=2.8 * cm,
    )

    qr_box = Table(
        [
            [qr_img],
            [Paragraph(d["codigo_reserva"], style("qr", 8, TEXTO_OSC, True, TA_CENTER))],
            [Paragraph("Verificar reserva", styles["center"])],
        ],
        colWidths=[5 * cm],
    )

    qr_box.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), GRIS_SUAVE),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ])
    )

    story.append(qr_box)
    story.append(Spacer(1, 24))

    story.append(Paragraph("BENEFICIOS INCLUIDOS", styles["section"]))
    story.append(HRFlowable(width=ancho, thickness=1, color=DORADO))
    story.append(Spacer(1, 8))

    beneficios = Table(
        [
            ["Reserva confirmada", "Tu reserva está garantizada y asegurada."],
            ["Pago seguro", "Transacción protegida."],
            ["Cancelación flexible", "Hasta 48h antes del viaje."],
            ["Soporte en español", "Atención 24/7."],
        ],
        colWidths=[ancho * 0.35, ancho * 0.65],
    )

    beneficios.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), GRIS_SUAVE),
                ("GRID", (0, 0), (-1, -1), 0.5, GRIS_LINEA),
                ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
            ]
        )
    )

    story.append(beneficios)
    story.append(Spacer(1, 18))

    footer = Table(
        [
            [
                Paragraph("TravelWorld", styles["brand"]),
                Paragraph(
                    "www.travelworld.com<br/>reservas@travelworld.com | +1 (809) 555-5555<br/>© 2026 TravelWorld",
                    styles["right"],
                ),
            ]
        ],
        colWidths=[ancho * 0.45, ancho * 0.55],
    )

    footer.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), GRIS_SUAVE),
                ("LINEABOVE", (0, 0), (-1, 0), 2, DORADO),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("TOPPADDING", (0, 0), (-1, -1), 12),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
                ("LEFTPADDING", (0, 0), (-1, -1), 12),
                ("RIGHTPADDING", (0, 0), (-1, -1), 12),
            ]
        )
    )

    story.append(footer)

    doc.build(story)

    print(f"PDF generado: {output_path}")

    return f"/comprobantes/{Path(output_path).name}"