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

        password_hash = bcrypt.hashpw(
            self.password.encode(),
            bcrypt.gensalt()
        ).decode()

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

            if not user:
                self.mensaje = "Usuario no encontrado."
                return

            if not bcrypt.checkpw(
                self.password.encode(),
                user["password_hash"].encode()
            ):
                self.mensaje = "Contraseña incorrecta."
                return

            self.usuario_id = user["id"]
            self.nombre = user["nombre"]
            self.email = user["email"]
            self.rol = user["rol"]
            self.mensaje = ""

            if self.rol == "admin":
                return rx.redirect("/admin/dashboard")

            return rx.redirect("/")

        except Exception as e:
            self.mensaje = f"Error: {str(e)}"

    def logout(self):
        self.usuario_id = 0
        self.nombre = ""
        self.email = ""
        self.password = ""
        self.confirmar_password = ""
        self.rol = ""
        self.mensaje = ""
        return rx.redirect("/")