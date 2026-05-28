from api.services import obtener_destinos, obtener_ofertas_momento

print("DESTINOS:")
for d in obtener_destinos():
    print(d.pais, "-", d.ciudad)

print("\nOFERTAS DEL MOMENTO:")
for o in obtener_ofertas_momento():
    print(o.titulo, "-", o.precio)