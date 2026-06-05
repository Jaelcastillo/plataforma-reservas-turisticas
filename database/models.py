from sqlalchemy import Column, Integer, String, Text, DECIMAL, Boolean, Date, TIMESTAMP, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Destino(Base):
    __tablename__ = "destinos"

    id = Column(Integer, primary_key=True, index=True)
    pais = Column(String(100), nullable=False)
    ciudad = Column(String(100), nullable=False)
    titulo = Column(String(150), nullable=False)
    descripcion = Column(Text, nullable=False)
    imagen = Column(String(255))
    destacado = Column(Boolean, default=False)
    activo = Column(Boolean, default=True)


class Oferta(Base):
    __tablename__ = "ofertas"

    id = Column(Integer, primary_key=True, index=True)
    destino_id = Column(Integer, ForeignKey("destinos.id"))
    titulo = Column(String(150), nullable=False)
    categoria = Column(String(50), nullable=False)
    descripcion = Column(Text, nullable=False)
    precio = Column(DECIMAL(10, 2), nullable=False)
    precio_anterior = Column(DECIMAL(10, 2))
    descuento = Column(Integer, default=0)
    es_oferta_momento = Column(Boolean, default=False)
    duracion = Column(String(80))
    rating = Column(DECIMAL(2, 1), default=5.0)
    imagen = Column(String(255))
    activo = Column(Boolean, default=True)


class Reserva(Base):
    __tablename__ = "reservas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    telefono = Column(String(30))
    pais_destino = Column(String(100), nullable=False)
    oferta = Column(String(150), nullable=False)
    fecha_viaje = Column(Date, nullable=False)
    personas = Column(Integer, nullable=False)
    metodo_pago = Column(String(50))
    estado = Column(String(50), default="Pendiente")
    comentarios = Column(Text)

    usuario_id = Column(Integer)
    total = Column(DECIMAL(10, 2), default=0)
    codigo_reserva = Column(String(50))
    pdf_url = Column(String(255))
    oferta_imagen = Column(String(255))

    created_at = Column(TIMESTAMP)

class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP)