CREATE SCHEMA Cinema;
USE Cinema;

CREATE TABLE salas (
  idsala INT(11) NOT NULL AUTO_INCREMENT,
  num_asientos VARCHAR(10) NOT NULL,
  numero_sala VARCHAR(10) NOT NULL,
  tipo_sala VARCHAR(10) NOT NULL,
  PRIMARY KEY (idsala)
);

CREATE TABLE asientos (
  idasiento INT(11) NOT NULL AUTO_INCREMENT,
  asiento VARCHAR(10) NOT NULL,
  fila VARCHAR(10) NOT NULL,
  salas_idsala INT(11) NOT NULL,
  PRIMARY KEY (idasiento),
  INDEX fk_asientos_salas1_idx (salas_idsala ASC),
  CONSTRAINT fk_asientos_salas1
    FOREIGN KEY (salas_idsala)
    REFERENCES salas(idsala)
);

CREATE TABLE clientes (
  idcliente INT(11) NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(20) NOT NULL,
  apellido_p VARCHAR(20) NOT NULL,
  apellido_m VARCHAR(20) NOT NULL,
  edad VARCHAR(30) NOT NULL,
  correo VARCHAR(20) NOT NULL,
  tel VARCHAR(20) NOT NULL,
  usuario VARCHAR(30) NULL DEFAULT NULL,
  contrasena VARCHAR(30) NULL DEFAULT NULL,
  admin TINYINT(4) NOT NULL,
  PRIMARY KEY (idcliente)
);

CREATE TABLE generos (
  idgenero INT(11) NOT NULL AUTO_INCREMENT,
  genero VARCHAR(20) NOT NULL,
  PRIMARY KEY (`idgenero`)
);

CREATE TABLE peliculas (
  idpelicula INT(11) NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(20) NOT NULL,
  duracion VARCHAR(20) NOT NULL,
  sinopsis VARCHAR(20) NOT NULL,
  clasificacion VARCHAR(10) NOT NULL,
  generos_idgenero INT(11) NOT NULL,
  PRIMARY KEY (idpelicula),
  INDEX fk_peliculas_generos1_idx (generos_idgenero ASC),
  CONSTRAINT fk_peliculas_generos1
    FOREIGN KEY (generos_idgenero)
    REFERENCES generos(idgenero)
);

CREATE TABLE funciones (
  id_funciones INT(11) NOT NULL AUTO_INCREMENT,
  idpelicula INT(11) NULL DEFAULT NULL,
  fecha DATE NOT NULL,
  hora VARCHAR(20) NOT NULL,
  salas_idsala INT(11) NOT NULL,
  precio VARCHAR(30) NULL DEFAULT NULL,
  PRIMARY KEY (id_funciones),
  INDEX fk_peli_horario_idpelicula (idpelicula ASC),
  INDEX fk_funciones_salas1_idx (salas_idsala ASC),
  CONSTRAINT fk_funciones_salas1
    FOREIGN KEY (salas_idsala)
    REFERENCES salas (idsala),
  CONSTRAINT fk_peli_horario_idpelicula
    FOREIGN KEY (idpelicula)
    REFERENCES peliculas (idpelicula)
);

CREATE TABLE boletos (
  idboleto INT(11) NOT NULL AUTO_INCREMENT,
  id_funciones INT(11) NULL DEFAULT NULL,
  id_salas_asientos INT(11) NULL DEFAULT NULL,
  clientes_idcliente INT(11) NOT NULL,
  asientos_idasiento INT(11) NOT NULL,
  PRIMARY KEY (idboleto),
  INDEX fk_pelihorario (id_funciones ASC),
  INDEX fk_boletos_clientes1_idx (clientes_idcliente ASC),
  INDEX fk_boletos_asientos1_idx (asientos_idasiento ASC),
  CONSTRAINT fk_boletos_asientos1
    FOREIGN KEY (asientos_idasiento)
    REFERENCES asientos (idasiento),
  CONSTRAINT fk_boletos_clientes1
    FOREIGN KEY (clientes_idcliente)
    REFERENCES clientes (idcliente),
  CONSTRAINT fk_pelihorario
    FOREIGN KEY (id_funciones)
    REFERENCES funciones (id_funciones)
);
