"# Plataforma de Reservas Turisticas" 
# TravelWorld Premium

## Plataforma de Reservas Turísticas

###  Descripción General

TravelWorld Premium es una plataforma web desarrollada para la gestión integral de reservas turísticas nacionales e internacionales. El sistema permite a los usuarios registrarse, iniciar sesión, explorar destinos turísticos, visualizar ofertas exclusivas, realizar reservas y consultar el historial de viajes. Además, incorpora un panel administrativo completo para la gestión de destinos, ofertas, usuarios y reservas.

El proyecto fue desarrollado utilizando Python, Reflex y MySQL, aplicando una arquitectura organizada por módulos para facilitar el mantenimiento y escalabilidad del sistema.

---

# 🎯 Objetivos del Proyecto

* Facilitar la reserva de paquetes turísticos.
* Centralizar la gestión de destinos y ofertas.
* Permitir el control administrativo de clientes y reservas.
* Simular una plataforma profesional de turismo.
* Aplicar conceptos de desarrollo web, bases de datos y programación orientada a objetos.

---

# 🏗 Arquitectura del Sistema

El proyecto está organizado siguiendo una estructura modular para separar responsabilidades.

```text
turismo_reservas/
│
├── api/
├── database/
├── styles/
├── turismo_reservas/
│   ├── pages/
│   ├── states/
│   └── turismo_reservas.py
│
├── utils/
├── .env
├── rxconfig.py
├── pyproject.toml
└── README.md
```

---

# 📂 Descripción de Carpetas

## api/

Contiene los servicios encargados de la comunicación entre la aplicación y la base de datos.

Funciones principales:

* Creación de reservas.
* Consulta de reservas.
* Procesamiento de información turística.
* Gestión de operaciones administrativas.

---

## database/

Contiene toda la configuración de acceso a MySQL.

Archivos principales:

### connection.py

Gestiona la conexión con la base de datos utilizando SQLAlchemy y PyMySQL.

### models.py

Define las estructuras utilizadas por el sistema para interactuar con la información almacenada.

---

## turismo_reservas/pages/

Contiene todas las páginas visuales del sistema.

### index.py

Página principal del sistema.

Incluye:

* Destinos destacados.
* Ofertas del momento.
* Información corporativa.
* Acceso rápido a reservas.

### login.py

Permite a los usuarios autenticarse dentro del sistema.

### registro.py

Permite la creación de nuevas cuentas de usuario.

### reservas.py

Módulo principal para realizar reservas turísticas.

Incluye:

* Selección de destino.
* Selección de oferta.
* Información del viajero.
* Método de pago.
* Confirmación de reserva.

### mis_reservas.py

Permite visualizar todas las reservas realizadas por el usuario.

### ofertas.py

Muestra las ofertas disponibles para cada destino.

### sobre_nosotros.py

Página corporativa desarrollada para presentar la empresa.

Incluye:

* Historia de TravelWorld Premium.
* Misión.
* Visión.
* Valores.
* Información de contacto.
* Ubicación corporativa en BlueMall Santo Domingo.
* Información de los socios fundadores:

  * Jael Castillo
  * Alissa Marie
  * José Luis Mañón

---

# 🔐 Panel Administrativo

El sistema incorpora un panel administrativo completo.

---

## dashboard.py

Muestra indicadores generales:

* Total de reservas.
* Total de clientes.
* Total de ofertas.
* Ingresos generados.

---

## admin_destinos.py

Permite:

* Crear destinos.
* Editar destinos.
* Activar o desactivar destinos.
* Marcar destinos destacados.
* Gestionar imágenes de destinos.

---

## admin_ofertas.py

Permite:

* Crear nuevas ofertas.
* Editar ofertas existentes.
* Calcular descuentos automáticamente.
* Activar o desactivar ofertas.
* Eliminar ofertas.

---

## admin_reservas.py

Permite:

* Visualizar todas las reservas.
* Confirmar reservas.
* Cancelar reservas.
* Eliminar reservas.
* Gestionar estados de viaje.

---

## admin_usuarios.py

Permite:

* Visualizar usuarios registrados.
* Cambiar roles.
* Activar o desactivar cuentas.
* Eliminar usuarios.

---

# ⚙ Gestión de Estados

## auth_state.py

Es el núcleo de la aplicación.

Controla:

* Registro de usuarios.
* Inicio de sesión.
* Cierre de sesión.
* Gestión de destinos.
* Gestión de ofertas.
* Gestión de reservas.
* Gestión administrativa.
* Estadísticas del dashboard.

---

## reservation_state.py

Administra los datos relacionados con las reservas y el proceso de compra.

---

# 🗄 Base de Datos

Motor utilizado:

**MySQL 8.0**

Base de datos:

```sql
turismo_reservas_db
```

Tablas principales:

* usuarios
* admins
* destinos
* ofertas
* reservas

---

#  Destinos Implementados

* Punta Cana
* Puerto Rico
* Cartagena
* Cancún
* Orlando

---

#  Ofertas Implementadas

* Tours en buggy.
* Resorts todo incluido.
* Excursiones culturales.
* Paquetes Disney.
* Resorts premium.
* Ofertas especiales con descuentos automáticos.

---

# Tecnologías Utilizadas

### Backend

* Python 3.12
* Reflex
* SQLAlchemy
* PyMySQL
* Bcrypt
* Python Dotenv

### Base de Datos

* MySQL 8.0

### Frontend

* Reflex UI
* Componentes Radix
* Diseño responsivo

---

#  Seguridad Implementada

* Contraseñas cifradas con Bcrypt.
* Gestión de sesiones.
* Control de acceso por roles.
* Validación de formularios.
* Restricción de funciones administrativas.

---

#  Funcionalidades Completadas

✅ Registro de usuarios

✅ Inicio de sesión

✅ Gestión de perfiles

✅ Reservas turísticas

✅ Consulta de reservas

✅ Gestión de destinos

✅ Gestión de ofertas

✅ Gestión de usuarios

✅ Dashboard administrativo

✅ Carga dinámica desde MySQL

✅ Sistema de descuentos

✅ Generación de comprobantes

✅ Página corporativa profesional

✅ Integración completa con MySQL

---

👨‍💻 Autores

### TravelWorld Premium

Socios Fundadores:

* Jael Castillo
* Alissa Marie


Año: 2026

Desarrollado como proyecto académico aplicando programación web, bases de datos, diseño de interfaces y administración de sistemas de información.
