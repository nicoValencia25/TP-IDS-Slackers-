CREATE DATABASE  IF NOT EXISTS `HotelBD` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `HotelBD`;
-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: HotelBD
-- ------------------------------------------------------
-- Server version	8.0.39-0ubuntu0.24.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Habitaciones`
--

DROP TABLE IF EXISTS `Habitaciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Habitaciones` (
  `HabitacionID` int NOT NULL AUTO_INCREMENT,
  `HotelID` int NOT NULL,
  `NumHabitacion` tinyint NOT NULL,
  `Piso` tinyint NOT NULL,
  `TipoDeHabitacion` varchar(50) NOT NULL,
  `CantHuespedes` tinyint NOT NULL,
  `Descripcion` varchar(500) NOT NULL,
  `Superficie` tinyint NOT NULL,
  `PrecioAdulto` int NOT NULL,
  `PrecioNiño` int NOT NULL,
  PRIMARY KEY (`HabitacionID`),
  KEY `FK_1` (`HotelID`),
  CONSTRAINT `FK_1` FOREIGN KEY (`HotelID`) REFERENCES `Hoteles` (`HotelID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Habitaciones`
--

LOCK TABLES `Habitaciones` WRITE;
/*!40000 ALTER TABLE `Habitaciones` DISABLE KEYS */;
/*!40000 ALTER TABLE `Habitaciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Hoteles`
--

DROP TABLE IF EXISTS `Hoteles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Hoteles` (
  `HotelID` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) NOT NULL,
  `Ubicacion` point NOT NULL,
  `Descripcion` varchar(1000) NOT NULL,
  PRIMARY KEY (`HotelID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Hoteles`
--

LOCK TABLES `Hoteles` WRITE;
/*!40000 ALTER TABLE `Hoteles` DISABLE KEYS */;
/*!40000 ALTER TABLE `Hoteles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ImgHabitaciones`
--

DROP TABLE IF EXISTS `ImgHabitaciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ImgHabitaciones` (
  `ImgHabitacionID` int NOT NULL AUTO_INCREMENT,
  `HabitacionID` int NOT NULL,
  `ImgHabitacion` varchar(50) NOT NULL,
  PRIMARY KEY (`ImgHabitacionID`),
  KEY `FK_4` (`HabitacionID`),
  CONSTRAINT `FK_4` FOREIGN KEY (`HabitacionID`) REFERENCES `Habitaciones` (`HabitacionID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ImgHabitaciones`
--

LOCK TABLES `ImgHabitaciones` WRITE;
/*!40000 ALTER TABLE `ImgHabitaciones` DISABLE KEYS */;
/*!40000 ALTER TABLE `ImgHabitaciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ImgHoteles`
--

DROP TABLE IF EXISTS `ImgHoteles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ImgHoteles` (
  `ImgHotelID` int NOT NULL AUTO_INCREMENT,
  `HotelID` int NOT NULL,
  `imgHotel` varchar(50) NOT NULL,
  PRIMARY KEY (`ImgHotelID`),
  KEY `FK_5` (`HotelID`),
  CONSTRAINT `FK_5` FOREIGN KEY (`HotelID`) REFERENCES `Hoteles` (`HotelID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ImgHoteles`
--

LOCK TABLES `ImgHoteles` WRITE;
/*!40000 ALTER TABLE `ImgHoteles` DISABLE KEYS */;
/*!40000 ALTER TABLE `ImgHoteles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Reservas`
--

DROP TABLE IF EXISTS `Reservas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Reservas` (
  `ReservaID` int NOT NULL AUTO_INCREMENT,
  `UsuarioID` int NOT NULL,
  `HabitacionID` int NOT NULL,
  `ReservaCreacion` datetime NOT NULL,
  `Desde` datetime NOT NULL,
  `Hasta` datetime NOT NULL,
  `CantAdultos` tinyint NOT NULL,
  `CantNiños` tinyint NOT NULL,
  `PrecioTotal` int NOT NULL,
  PRIMARY KEY (`ReservaID`),
  KEY `FK_3` (`UsuarioID`),
  KEY `FK_3_1` (`HabitacionID`),
  CONSTRAINT `FK_3` FOREIGN KEY (`UsuarioID`) REFERENCES `Usuarios` (`UsuarioID`),
  CONSTRAINT `FK_3_1` FOREIGN KEY (`HabitacionID`) REFERENCES `Habitaciones` (`HabitacionID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Reservas`
--

LOCK TABLES `Reservas` WRITE;
/*!40000 ALTER TABLE `Reservas` DISABLE KEYS */;
/*!40000 ALTER TABLE `Reservas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Usuarios`
--

DROP TABLE IF EXISTS `Usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Usuarios` (
  `UsuarioID` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) NOT NULL,
  `Apellido` varchar(50) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Contraseña` varchar(40) NOT NULL,
  `Telefono` varchar(20) NOT NULL,
  `DNI` varchar(15) NOT NULL,
  PRIMARY KEY (`UsuarioID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Usuarios`
--

LOCK TABLES `Usuarios` WRITE;
/*!40000 ALTER TABLE `Usuarios` DISABLE KEYS */;
/*!40000 ALTER TABLE `Usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'HotelBD'
--

--
-- Dumping routines for database 'HotelBD'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-01 21:26:27
