from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from pathlib import Path
from datetime import datetime


def generar_pdf_reserva(data: dict) -> str:
    carpeta = Path("assets/comprobantes")
    carpeta.mkdir(parents=True, exist_ok=True)

    codigo = f"TW-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    archivo = carpeta / f"{codigo}.pdf"

    doc = SimpleDocTemplate(str(archivo), pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    title = Paragraph("<b>TravelWorld</b>", styles["Title"])
    story.append(title)
    story.append(Spacer(1, 0.2 * inch))

    story.append(Paragraph("<b>¡Tu reserva está confirmada!</b>", styles["Heading1"]))
    story.append(Paragraph(f"Número de confirmación: <b>{codigo}</b>", styles["Normal"]))
    story.append(Spacer(1, 0.3 * inch))

    imagen = data.get("imagen")
    if imagen:
        img_path = imagen.replace("/images/", "assets/images/")
        if Path(img_path).exists():
            img = Image(img_path, width=6.3 * inch, height=2.8 * inch)
            story.append(img)
            story.append(Spacer(1, 0.3 * inch))

    tabla = [
        ["Nombre", data.get("nombre", "")],
        ["Email", data.get("email", "")],
        ["Teléfono", data.get("telefono", "")],
        ["Destino", data.get("destino", "")],
        ["Paquete", data.get("paquete", "")],
        ["Fecha de viaje", data.get("fecha", "")],
        ["Personas", data.get("personas", "")],
        ["Método de pago", data.get("metodo_pago", "")],
        ["Total", f"${data.get('total', '')} USD"],
        ["Comentarios", data.get("comentarios", "")],
    ]

    table = Table(tabla, colWidths=[2.2 * inch, 4.1 * inch])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#F5EFE6")),
        ("TEXTCOLOR", (0, 0), (-1, -1), colors.HexColor("#2B241A")),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#D8CBB6")),
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
        ("PADDING", (0, 0), (-1, -1), 10),
    ]))

    story.append(table)
    story.append(Spacer(1, 0.4 * inch))

    story.append(Paragraph("Gracias por elegir TravelWorld.", styles["Heading3"]))
    story.append(Paragraph("Este comprobante confirma que tu reserva fue registrada correctamente.", styles["Normal"]))

    doc.build(story)

    return f"/comprobantes/{archivo.name}"