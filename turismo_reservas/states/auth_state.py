import reflex as rx
import pymysql
import bcrypt
import os
from dotenv import load_dotenv

load_dotenv()


def get_conn():
    return pymysql.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "turismo_reservas_db"),
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True,
    )


class AuthState(rx.State):
    usuario_id: int = 0
    nombre: str = ""
    email: str = ""
    password: str = ""
    confirmar_password: str = ""
    rol: str = ""
    mensaje: str = ""

    admin_total_reservas: int = 0
    admin_total_clientes: int = 0
    admin_total_ofertas: int = 0
    admin_total_ingresos: float = 0.0

    mis_reservas: list[dict] = []
    admin_reservas: list[dict] = []
    admin_ofertas: list[dict] = []
    ofertas_publicas: list[dict] = []

    editando_oferta: bool = False
    edit_oferta_id: int = 0
    edit_titulo_oferta: str = ""
    edit_categoria_oferta: str = ""
    edit_precio_oferta: str = ""
    edit_descuento_oferta: str = ""

    @rx.var
    def esta_logueado(self) -> bool:
        return self.usuario_id != 0

    @rx.var
    def es_admin(self) -> bool:
        return self.rol == "admin"

    def set_nombre(self, v):
        self.nombre = v

    def set_email(self, v):
        self.email = v

    def set_password(self, v):
        self.password = v

    def set_confirmar_password(self, v):
        self.confirmar_password = v

    def registrar(self):
        if not self.nombre or not self.email or not self.password:
            self.mensaje = "Completa todos los campos."
            return

        if self.password != self.confirmar_password:
            self.mensaje = "Las contraseñas no coinciden."
            return

        password_hash = bcrypt.hashpw(self.password.encode(), bcrypt.gensalt()).decode()

        try:
            conn = get_conn()
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO usuarios (nombre, email, password_hash, rol)
                    VALUES (%s, %s, %s, 'cliente')
                    """,
                    (self.nombre, self.email, password_hash),
                )
                self.usuario_id = cur.lastrowid
                self.rol = "cliente"
                self.mensaje = "Cuenta creada correctamente."

            conn.close()
            return rx.redirect("/")

        except pymysql.err.IntegrityError:
            self.mensaje = "Ese correo ya está registrado."

        except Exception as e:
            self.mensaje = f"Error: {str(e)}"

    def login(self):
        if not self.email or not self.password:
            self.mensaje = "Escribe tu correo y contraseña."
            return

        try:
            conn = get_conn()
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT id, nombre, email, password_hash, rol
                    FROM usuarios
                    WHERE email=%s AND activo=1
                    LIMIT 1
                    """,
                    (self.email,),
                )
                user = cur.fetchone()

            conn.close()

            if not user:
                self.mensaje = "Usuario no encontrado."
                return

            if not bcrypt.checkpw(self.password.encode(), user["password_hash"].encode()):
                self.mensaje = "Contraseña incorrecta."
                return

            self.usuario_id = user["id"]
            self.nombre = user["nombre"]
            self.email = user["email"]
            self.rol = user["rol"]
            self.mensaje = ""

            if self.rol == "admin":
                self.cargar_dashboard_admin()
                return rx.redirect("/admin/dashboard")

            self.cargar_mis_reservas()
            return rx.redirect("/")

        except Exception as e:
            self.mensaje = f"Error: {str(e)}"

    def cargar_dashboard_admin(self):
        try:
            conn = get_conn()
            with conn.cursor() as cur:
                cur.execute("SELECT COUNT(*) AS total FROM reservas")
                self.admin_total_reservas = cur.fetchone()["total"]

                cur.execute("SELECT COUNT(*) AS total FROM usuarios WHERE rol='cliente'")
                self.admin_total_clientes = cur.fetchone()["total"]

                cur.execute("SELECT COUNT(*) AS total FROM ofertas WHERE activo=1")
                self.admin_total_ofertas = cur.fetchone()["total"]

                cur.execute("SELECT COALESCE(SUM(total),0) AS total FROM reservas")
                self.admin_total_ingresos = float(cur.fetchone()["total"])

            conn.close()

        except Exception as e:
            self.mensaje = f"Error dashboard: {str(e)}"

    def cargar_ofertas_publicas(self):
        try:
            conn = get_conn()
            with conn.cursor() as cur:
                cur.execute(
    """
    SELECT
        id,
        titulo,
        categoria,
        descripcion,
        precio,
        precio_anterior,
        descuento,
        duracion,
        rating,
        CONCAT('/images/', imagen) AS imagen
    FROM ofertas
    WHERE activo=1
    ORDER BY id DESC
    """
)
                self.ofertas_publicas = cur.fetchall()

            conn.close()

        except Exception as e:
            self.mensaje = str(e)

    def cargar_mis_reservas(self):
        try:
            conn = get_conn()
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT id, pais_destino, oferta, fecha_viaje, personas,
                           metodo_pago, estado, total, created_at,
                           codigo_reserva, pdf_url, oferta_imagen
                    FROM reservas
                    WHERE email = %s
                    ORDER BY id DESC
                    """,
                    (self.email,),
                )
                self.mis_reservas = cur.fetchall()

            conn.close()

        except Exception as e:
            self.mensaje = f"Error cargando reservas: {str(e)}"

    def cargar_todas_reservas(self):
        try:
            conn = get_conn()
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT id, nombre, oferta, fecha_viaje, total, estado
                    FROM reservas
                    ORDER BY id DESC
                    """
                )
                self.admin_reservas = cur.fetchall()

            conn.close()

        except Exception as e:
            self.mensaje = str(e)

    def confirmar_reserva_admin(self, reserva_id: int):
        try:
            conn = get_conn()
            with conn.cursor() as cur:
                cur.execute("UPDATE reservas SET estado='Confirmada' WHERE id=%s", (reserva_id,))
            conn.close()
            self.cargar_todas_reservas()
            self.cargar_dashboard_admin()
        except Exception as e:
            self.mensaje = str(e)

    def cancelar_reserva_admin(self, reserva_id: int):
        try:
            conn = get_conn()
            with conn.cursor() as cur:
                cur.execute("UPDATE reservas SET estado='Cancelada' WHERE id=%s", (reserva_id,))
            conn.close()
            self.cargar_todas_reservas()
            self.cargar_dashboard_admin()
        except Exception as e:
            self.mensaje = str(e)

    def eliminar_reserva_admin(self, reserva_id: int):
        try:
            conn = get_conn()
            with conn.cursor() as cur:
                cur.execute("DELETE FROM reservas WHERE id=%s", (reserva_id,))
            conn.close()
            self.cargar_todas_reservas()
            self.cargar_dashboard_admin()
        except Exception as e:
            self.mensaje = str(e)

    def cargar_ofertas_admin(self):
        try:
            conn = get_conn()
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT id, titulo, categoria, precio, descuento, activo
                    FROM ofertas
                    ORDER BY id DESC
                    """
                )
                self.admin_ofertas = cur.fetchall()

            conn.close()

        except Exception as e:
            self.mensaje = str(e)

    def toggle_oferta_admin(self, oferta_id: int):
        try:
            conn = get_conn()
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE ofertas SET activo = NOT activo WHERE id = %s",
                    (oferta_id,),
                )

            conn.close()
            self.cargar_ofertas_admin()
            self.cargar_dashboard_admin()
            self.cargar_ofertas_publicas()

        except Exception as e:
            self.mensaje = str(e)

    def set_edit_titulo_oferta(self, v):
        self.edit_titulo_oferta = v

    def set_edit_categoria_oferta(self, v):
        self.edit_categoria_oferta = v

    def set_edit_precio_oferta(self, v):
        self.edit_precio_oferta = v

    def set_edit_descuento_oferta(self, v):
        self.edit_descuento_oferta = v

    def cargar_oferta_para_editar(self, oferta_id: int):
        try:
            conn = get_conn()
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT id, titulo, categoria, precio, descuento
                    FROM ofertas
                    WHERE id=%s
                    LIMIT 1
                    """,
                    (oferta_id,),
                )
                oferta = cur.fetchone()

            conn.close()

            if oferta:
                self.editando_oferta = True
                self.edit_oferta_id = oferta["id"]
                self.edit_titulo_oferta = oferta["titulo"]
                self.edit_categoria_oferta = oferta["categoria"]
                self.edit_precio_oferta = str(oferta["precio"])
                self.edit_descuento_oferta = str(oferta["descuento"])

        except Exception as e:
            self.mensaje = str(e)

    def cancelar_edicion_oferta(self):
        self.editando_oferta = False
        self.edit_oferta_id = 0
        self.edit_titulo_oferta = ""
        self.edit_categoria_oferta = ""
        self.edit_precio_oferta = ""
        self.edit_descuento_oferta = ""

    def actualizar_oferta_admin(self):
        try:
            conn = get_conn()
            with conn.cursor() as cur:
                cur.execute(
                    """
                    UPDATE ofertas
                    SET titulo=%s,
                        categoria=%s,
                        precio=%s,
                        descuento=%s
                    WHERE id=%s
                    """,
                    (
                        self.edit_titulo_oferta,
                        self.edit_categoria_oferta,
                        float(self.edit_precio_oferta),
                        int(self.edit_descuento_oferta),
                        self.edit_oferta_id,
                    ),
                )

            conn.close()
            self.cancelar_edicion_oferta()
            self.cargar_ofertas_admin()
            self.cargar_dashboard_admin()
            self.cargar_ofertas_publicas()
            return rx.redirect("/")

        except Exception as e:
            self.mensaje = str(e)

    def eliminar_oferta_admin(self, oferta_id: int):
        try:
            conn = get_conn()
            with conn.cursor() as cur:
                cur.execute("DELETE FROM ofertas WHERE id=%s", (oferta_id,))

            conn.close()
            self.cargar_ofertas_admin()
            self.cargar_dashboard_admin()
            self.cargar_ofertas_publicas()

        except Exception as e:
            self.mensaje = str(e)

    def logout(self):
        self.usuario_id = 0
        self.nombre = ""
        self.email = ""
        self.password = ""
        self.confirmar_password = ""
        self.rol = ""
        self.mensaje = ""

        self.admin_total_reservas = 0
        self.admin_total_clientes = 0
        self.admin_total_ofertas = 0
        self.admin_total_ingresos = 0.0

        self.mis_reservas = []
        self.admin_reservas = []
        self.admin_ofertas = []
        self.ofertas_publicas = []

        self.cancelar_edicion_oferta()

        return rx.redirect("/")