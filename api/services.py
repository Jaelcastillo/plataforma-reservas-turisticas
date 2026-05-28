from database.connection import get_db_connection
from database.models import Destino, Oferta, Reserva, Admin


def obtener_destinos():
    db = get_db_connection()
    try:
        return db.query(Destino).filter(Destino.activo == True).all()
    finally:
        db.close()


def obtener_ofertas():
    db = get_db_connection()
    try:
        return db.query(Oferta).filter(Oferta.activo == True).all()
    finally:
        db.close()


def obtener_ofertas_momento():
    db = get_db_connection()
    try:
        return db.query(Oferta).filter(
            Oferta.activo == True,
            Oferta.es_oferta_momento == True
        ).all()
    finally:
        db.close()


def crear_reserva(nombre, email, telefono, pais_destino, oferta, fecha_viaje, personas, metodo_pago, comentarios):
    db = get_db_connection()
    try:
        nueva_reserva = Reserva(
            nombre=nombre,
            email=email,
            telefono=telefono,
            pais_destino=pais_destino,
            oferta=oferta,
            fecha_viaje=fecha_viaje,
            personas=personas,
            metodo_pago=metodo_pago,
            comentarios=comentarios,
        )
        db.add(nueva_reserva)
        db.commit()
        db.refresh(nueva_reserva)
        return nueva_reserva
    finally:
        db.close()


def obtener_reservas():
    db = get_db_connection()
    try:
        return db.query(Reserva).all()
    finally:
        db.close()