from database.connection import get_db_connection
from database.models import Destino

db = get_db_connection()

destinos = db.query(Destino).all()

for destino in destinos:
    print(destino.pais, "-", destino.ciudad)

db.close()