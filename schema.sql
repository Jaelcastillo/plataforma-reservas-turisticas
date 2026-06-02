-- ═══════════════════════════════════════════════════════════════
--  TravelWorld — Schema MySQL completo
--  Ejecutar en MySQL Workbench o: mysql -u root -p turismo_reservas_db < schema.sql
-- ═══════════════════════════════════════════════════════════════

USE turismo_reservas_db;

-- ─── Tabla usuarios ──────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS usuarios (
    id            INT AUTO_INCREMENT PRIMARY KEY,
    nombre        VARCHAR(120)  NOT NULL,
    email         VARCHAR(180)  NOT NULL UNIQUE,
    password_hash VARCHAR(255)  NOT NULL,
    rol           ENUM('cliente','admin') NOT NULL DEFAULT 'cliente',
    activo        TINYINT(1)    NOT NULL DEFAULT 1,
    creado_en     DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_email (email),
    INDEX idx_rol   (rol)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Admin por defecto  (password: Admin2024!)
-- El hash se regenera al iniciar la app; esto es solo para bootstrap.
INSERT IGNORE INTO usuarios (nombre, email, password_hash, rol)
VALUES (
    'Administrador',
    'admin@travelworld.com',
    '$2b$12$placeholderHashReemplazadoAlIniciar',
    'admin'
);

-- ─── Tabla destinos ──────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS destinos (
    id     INT AUTO_INCREMENT PRIMARY KEY,
    codigo VARCHAR(10)  NOT NULL UNIQUE,   -- 'rd','pr','co','mx','us'
    nombre VARCHAR(100) NOT NULL,
    activo TINYINT(1)   NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT IGNORE INTO destinos (codigo, nombre) VALUES
    ('rd','República Dominicana'),
    ('pr','Puerto Rico'),
    ('co','Colombia'),
    ('mx','México'),
    ('us','Estados Unidos');

-- ─── Tabla ofertas ───────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS ofertas (
    id              INT AUTO_INCREMENT PRIMARY KEY,
    destino_id      INT           NOT NULL,
    nombre          VARCHAR(200)  NOT NULL,
    descripcion     TEXT,
    precio          DECIMAL(10,2) NOT NULL,
    precio_original DECIMAL(10,2) NOT NULL,
    duracion        VARCHAR(60),
    categoria       VARCHAR(60),
    imagen          VARCHAR(255),
    icono           VARCHAR(10)   DEFAULT '🌴',
    estrellas       TINYINT       DEFAULT 5,
    reviews         INT           DEFAULT 0,
    activo          TINYINT(1)    NOT NULL DEFAULT 1,
    creado_en       DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (destino_id) REFERENCES destinos(id) ON DELETE CASCADE,
    INDEX idx_destino (destino_id),
    INDEX idx_activo  (activo)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Ofertas de ejemplo
INSERT IGNORE INTO ofertas
    (destino_id,nombre,descripcion,precio,precio_original,duracion,categoria,imagen,icono,estrellas,reviews)
VALUES
    (1,'Safari Buggy Punta Cana','8 horas todo incluido, guía bilingüe',89,150,'8 horas','Aventura','/images/offer_buggy.jpg','🏎',5,984),
    (1,'Resort Todo Incluido Bávaro','7 noches All-Inclusive, playa privada',899,1399,'7 noches','Resort','/images/resort_cap_cana.jpg','🏨',5,2341),
    (1,'Buggy Night Tour','4 horas nocturnas, cena incluida',79,120,'4 horas','Nocturno','/images/offer_punta_cana.jpg','🌙',5,512),
    (2,'San Juan Premium Escape','4 noches hotel boutique, desayuno',950,1250,'4 noches','City Escape','/images/offer_pr.jpg','🌺',5,1502),
    (2,'Dorado Beach Ritz-Carlton','5 noches ultra premium, Golf + Spa',3200,4500,'5 noches','Ultra Luxury','/images/resort_ritz.jpg','👑',5,876),
    (3,'Islas del Rosario Premium','1 día, lancha privada, snorkeling',120,180,'1 día','Excursión','/images/offer_cartagena.jpg','🏝',5,1204),
    (3,'Cartagena Old City Stay','3 noches hotel histórico, tour incluido',580,800,'3 noches','Cultural','/images/cartagena.jpg','🏛',5,634),
    (4,'VIP Coco Bongo Experience','Open bar, VIP lounge',199,320,'1 noche','Entretenimiento','/images/offer_cancun.jpg','🎭',5,5842),
    (4,'Marriott Cancún Resort','5 noches vista al mar, All-Inclusive',1199,1650,'5 noches','Resort','/images/resort_hardrock.jpg','🌊',5,1890),
    (5,'Disney World Paquete Premium','6 noches, 4 parques, hotel resort',2499,3099,'6 noches','Magia Disney','/images/offer_disney.jpg','✨',5,8721),
    (5,'Disney VIP After Hours','Acceso After Hours, 2 parques, guía privado',1450,1800,'3 días','VIP Experience','/images/disney.jpg','🏰',5,1243);

-- ─── Tabla reservas (actualizada) ────────────────────────────────
-- Si ya tienes la tabla, ALTER TABLE agrega las columnas faltantes:
ALTER TABLE reservas
    ADD COLUMN IF NOT EXISTS usuario_id    INT           DEFAULT NULL,
    ADD COLUMN IF NOT EXISTS total         DECIMAL(10,2) DEFAULT 0,
    ADD COLUMN IF NOT EXISTS codigo_reserva VARCHAR(20)  DEFAULT NULL,
    ADD COLUMN IF NOT EXISTS pdf_url       VARCHAR(255)  DEFAULT NULL,
    ADD COLUMN IF NOT EXISTS creado_en     DATETIME      DEFAULT CURRENT_TIMESTAMP;

-- Si prefieres crear desde cero (DROP primero si existe):
-- DROP TABLE IF EXISTS reservas;
CREATE TABLE IF NOT EXISTS reservas (
    id              INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id      INT           DEFAULT NULL,
    nombre          VARCHAR(120)  NOT NULL,
    email           VARCHAR(180)  NOT NULL,
    telefono        VARCHAR(30),
    pais_destino    VARCHAR(100),
    oferta          VARCHAR(200),
    fecha_viaje     DATE,
    personas        INT           DEFAULT 1,
    metodo_pago     VARCHAR(40),
    comentarios     TEXT,
    total           DECIMAL(10,2) DEFAULT 0,
    codigo_reserva  VARCHAR(20)   UNIQUE,
    pdf_url         VARCHAR(255),
    creado_en       DATETIME      DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE SET NULL,
    INDEX idx_usuario   (usuario_id),
    INDEX idx_codigo    (codigo_reserva),
    INDEX idx_creado    (creado_en)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;