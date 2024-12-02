CREATE DATABASE  IF NOT EXISTS `HotelDB` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `HotelDB`;
-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: localhost    Database: HotelDB
-- ------------------------------------------------------
-- Server version	8.0.40-0ubuntu0.24.04.1

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
  `Piso` int NOT NULL,
  `NumHabitacion` int NOT NULL,
  `TipoID` int NOT NULL,
  PRIMARY KEY (`HabitacionID`,`TipoID`),
  KEY `TipoID` (`TipoID`),
  CONSTRAINT `Habitaciones_ibfk_1` FOREIGN KEY (`TipoID`) REFERENCES `TiposDeHabitacion` (`TipoID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=122 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Habitaciones`
--

LOCK TABLES `Habitaciones` WRITE;
/*!40000 ALTER TABLE `Habitaciones` DISABLE KEYS */;
INSERT INTO `Habitaciones` VALUES (1,1,123,1),(2,1,115,1),(3,2,212,1),(4,2,207,1),(5,1,109,2),(6,2,201,2),(7,2,209,2),(8,3,304,2),(9,3,302,3),(10,3,307,3),(11,4,402,3),(12,1,122,4),(13,1,106,4),(14,2,211,4),(15,3,321,4),(16,3,313,4),(17,1,109,5),(18,1,104,5),(19,3,312,6),(20,3,319,6),(21,4,417,6),(22,4,402,6),(23,4,405,6),(24,4,414,6),(25,1,127,7),(26,3,323,7),(27,3,330,7),(28,3,318,7),(29,3,300,8),(30,4,406,8),(31,4,417,8),(32,5,512,8),(33,5,507,8),(34,5,501,8),(35,5,505,9),(36,5,502,9),(37,6,617,9),(38,6,603,9),(39,6,614,9),(40,6,610,9),(41,6,620,10),(42,6,623,10),(43,0,12,11),(44,0,4,11),(45,0,5,11),(46,1,102,11),(47,1,105,11),(48,0,15,12),(49,1,101,12),(50,1,109,12),(51,0,2,13),(52,1,107,13),(53,1,111,13),(54,1,113,13),(55,1,119,13),(56,0,1,14),(57,0,5,14),(58,0,6,14),(59,1,104,14),(60,0,9,15),(61,0,12,15),(62,1,105,15),(63,1,101,15),(64,1,116,16),(65,1,110,16),(66,0,18,17),(67,0,21,17),(68,0,4,17),(69,1,118,17),(70,1,111,17),(71,0,7,18),(72,1,115,18),(73,1,102,18),(74,1,120,18),(75,2,205,19),(76,2,201,19),(77,2,213,19),(78,0,12,20),(79,0,14,20),(80,0,10,20),(81,0,6,20),(82,1,109,20),(83,1,125,20),(84,1,131,20),(85,0,3,21),(86,1,126,21),(87,1,118,21),(88,2,222,21),(89,2,224,21),(90,2,211,21),(91,2,217,21),(92,2,202,22),(93,2,210,22),(94,2,216,22),(95,3,310,22),(96,3,301,23),(97,3,305,23),(98,3,317,23),(99,0,3,24),(100,0,2,24),(101,0,4,24),(102,0,1,25),(103,0,5,25),(104,0,9,26),(105,0,10,26),(106,0,12,27),(107,0,2,27),(108,0,5,27),(109,0,7,27),(110,0,17,27),(111,0,20,28),(112,0,12,28),(113,0,14,28),(114,0,19,29),(115,0,17,29),(116,0,22,29),(117,0,25,29),(118,1,102,29),(119,1,110,29),(120,1,116,30),(121,1,118,30);
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
  `Nombre` varchar(45) NOT NULL,
  `Descripcion` varchar(1000) NOT NULL,
  `Provincia` varchar(45) NOT NULL,
  `Direccion` varchar(45) NOT NULL,
  `CodigoPostal` int NOT NULL,
  `Localidad` varchar(45) DEFAULT NULL,
  `Longitud` varchar(45) NOT NULL,
  `Latitud` varchar(45) NOT NULL,
  PRIMARY KEY (`HotelID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Hoteles`
--

LOCK TABLES `Hoteles` WRITE;
/*!40000 ALTER TABLE `Hoteles` DISABLE KEYS */;
INSERT INTO `Hoteles` VALUES (1,'Gran Hotel Argentino','El Gran Hotel Argentino está situado a pocos metros de la avenida 9 de Julio y a 300 metros del Obelisco, y ofrece habitaciones cómodas y fácil acceso al transporte público de Buenos Aires. Hay WiFi gratuita. La plaza de Mayo y la Casa Rosada se hallan a 500 metros. \n Las encantadoras habitaciones del Gran Hotel Argentino cuentan con instalaciones modernas, como aire acondicionado, TV por cable y caja fuerte. Algunas habitaciones tienen vistas de la ciudad. \n Se proporciona servicio de habitaciones las 24 horas. El establecimiento puede organizar un servicio de enlace con el aeropuerto.','CABA','Carlos Pellegrini 37',1009,'Monserrat','-34.60781396176777','-58.380493774532816'),(2,'Hampton by Hilton Bariloche','El establecimiento Hampton By Hilton Bariloche alberga un bar y se encuentra en San Carlos de Bariloche, en la región de Río Negro, a 200 metros de la playa del Centro y a 1,6 km de la playa del Centenario. El establecimiento cuenta con restaurante, recepción 24 horas, salón común, WiFi gratuita en todas las instalaciones y guardaesquíes. \nLas habitaciones de este hotel disponen de TV de pantalla plana con canales por cable, hervidor de agua, escritorio, armario y baño privado con bidet y secador de pelo. \nEl Hampton By Hilton Bariloche sirve un desayuno buffet diario. \nHay servicio de alquiler de coches y bicicletas, y la zona es ideal para practicar esquí y ciclismo.','Rio Negro','Libertad 290',8400,'San Carlos de Bariloche','-41.13400569681666','-71.31254116071949'),(3,'Hotel InterContinental Buenos Aires','','CABA','Moreno 809',1091,'Montserrat','-34.61117676041572','-58.37801688802422'),(4,'Hotel Santa Catalina','El Hotel Santa Catalina ofrece un restaurante y habitaciones con WiFi gratuita y TV en Río Cuarto. Hay aparcamiento gratuito. El centro de la ciudad está a 10 minutos en coche.\nLos huéspedes tienen acceso gratuito a la piscina al aire libre, la bañera de hidromasaje y el solárium. En verano, el bar al aire libre sirve cerveza artesanal. \nLas habitaciones del Santa Catalina están decoradas con suelo de parqué, techos a dos aguas y muebles elegantes. TV LED, aire acondicionado y balcón privado. \nTodos los días se sirve un desayuno a la carta. El restaurante del establecimiento sirve platos internacionales y el bar ofrece bebidas y aperitivos en el jardín.','Córdoba','Ruta Nacional Número 8, km 614',5800,'Rio Cuarto','-33.201898609099466','-64.43087118994117'),(5,'Aguará Hotel & Spa','El Aguará Hotel & Spa ofrece alojamiento en Lobos y cuenta con una piscina al aire libre rodeada por un jardín fragante. Ofrece habitaciones con conexión WiFi gratuita y desayuno diario. \nLas habitaciones del Aguará Hotel & Spa son cómodas y disponen de balcón con vistas al jardín y a la piscina. TV de pantalla plana, escritorio, calefacción y caja fuerte. El baño privado incluye artículos de aseo gratuitos, secador de pelo y bañera. Algunos alojamientos están adaptados para silla de ruedas. Se proporciona ropa de cama. \nEl Aguará Hotel & Spa cuenta con un gimnasio y un solárium. El centro de spa incluye bañera de hidromasaje, sauna y solárium. Los huéspedes pueden utilizar el salón común y una sala de juegos con juegos de mesa. En los alrededores se pueden practicar numerosas actividades, como golf, ciclismo y pesca.','Buenos Aires','Los Eucaliptus 296',7240,'Lobos','-35.193185276142756','-59.114965454281986'),(6,'Howard Johnson Hotel & Casino','El Howard Johnson Hotel & Casino se encuentra en Formosa, a 4 km de la zona comercial. Cuenta con jardín con piscina, gimnasio, restaurante, aparcamiento gratuito y habitaciones con conexión Wi-Fi gratuita y TV de plasma. \nLas habitaciones del Howard Johnson Hotel tienen el suelo de moqueta y están equipadas con aire acondicionado, calefacción y baño privado (algunos con bañera de hidromasaje). \nTodas las mañanas se sirve un desayuno bufé por un suplemento.','Formosa','Gutnisky 3748',3600,'Formosa','-26.195999980752273','-58.203659012364'),(7,'Böden Hotel & Spa by AKEN Soul','Böden Hotel & Spa by AKEN Soul está en Villa General Belgrano, a 18 min a pie de Brewer Park Villa General Belgrano, y dispone de alojamiento con piscina de temporada al aire libre, parking privado gratis, centro de fitness y jardín. Este alojamiento ofrece restaurante, servicio de habitaciones y recepción 24 horas, además de wifi gratis en todo el alojamiento. Hay un centro de spa y bienestar con piscina cubierta, sauna, bañera de hidromasaje y salón de uso común. \nEl hotel ofrece habitaciones con aire acondicionado, escritorio, hervidor, minibar, caja fuerte, TV de pantalla plana, balcón y baño privado con bidet. En Böden Hotel & Spa by AKEN Soul, las habitaciones tienen ropa de cama y toallas. \nEl alojamiento ofrece terraza.','Córdoba','Avenida San Martín 1070',5194,'Villa General Belgrano','-31.95903433464375','-64.55365180349467'),(8,'Benitez Hostería','El Benitez Hostería ofrece un restaurante regional a la carta, conexión Wi-Fi gratuita y desayuno continental en Calilegua. También dispone de instalaciones para reuniones y mostrador de información turística. \nLas habitaciones tienen vistas al jardín, aire acondicionado y TV por cable. \nSe ofrece un servicio de consigna de equipaje.','Jujuy','19 de Abril s/n',4514,'Calilegua','-23.775190039036755','-64.77089909031285'),(9,'Amerian Chacras de Coria','Amerian Chacras de Coria está en Luján de Cuyo, a 16 km de Estadio Malvinas Argentinas, y dispone de alojamiento con piscina de temporada al aire libre, parking privado gratis, jardín y terraza. Este hotel de 4 estrellas ofrece restaurante y tiene habitaciones con aire acondicionado, wifi gratis y baño privado. El alojamiento ofrece recepción 24 horas. \nTodas las habitaciones de este alojamiento están equipadas con TV de pantalla plana y caja fuerte. En el hotel, las habitaciones incluyen ropa de cama y toallas. \nEn Amerian Chacras de Coria se sirve cada mañana un desayuno a la carta.','Mendoza','Almirante Brown 2403',5505,'Luján de Cuyo','-33.004891950178425','-68.89331794762224'),(10,'Hotel y Casino Del Río - General Roca','Hotel y Casino Del Río - General Roca tiene jardín, restaurante, casino y centro de spa y bienestar en General Roca. Este hotel de 4 estrellas ofrece centro de fitness y tiene habitaciones con aire acondicionado, wifi gratis y baño privado. El alojamiento dispone de sauna, ocio nocturno y servicio de habitaciones. \nTodas las habitaciones de este alojamiento están equipadas con TV de pantalla plana con canales por cable y caja fuerte. Todas las unidades tienen escritorio. \nLa clientela puede usar el centro de negocios o relajarse en la cafetería El personal de la recepción 24 horas habla inglés y español.','Rio Negro','Tronador 350',8332,'General Roca','-39.04507221597962','-67.57334731664623');
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
  `ImgHabitacion` varchar(200) NOT NULL,
  `TipoID` int NOT NULL,
  PRIMARY KEY (`ImgHabitacionID`,`TipoID`),
  KEY `TipoID` (`TipoID`),
  CONSTRAINT `ImgHabitaciones_ibfk_1` FOREIGN KEY (`TipoID`) REFERENCES `TiposDeHabitacion` (`TipoID`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ImgHabitaciones`
--

LOCK TABLES `ImgHabitaciones` WRITE;
/*!40000 ALTER TABLE `ImgHabitaciones` DISABLE KEYS */;
INSERT INTO `ImgHabitaciones` VALUES (1,'Hotel1/Tipo1/Img1.jpg',1),(2,'Hotel1/Tipo1/Img2.jpg',1),(3,'Hotel1/Tipo1/Img3.jpg',1),(4,'Hotel1/Tipo1/Img4.jpg',1),(5,'Hotel1/Tipo2/Img1.jpg',2),(6,'Hotel1/Tipo2/Img2.jpg',2),(7,'Hotel1/Tipo2/Img3.jpg',2),(8,'Hotel1/Tipo2/Img4.jpg',2),(9,'Hotel1/Tipo2/Img5.jpg',2),(10,'Hotel1/Tipo3/Img1.jpg',3),(11,'Hotel1/Tipo3/Img2.jpg',3),(12,'Hotel1/Tipo3/Img3.jpg',3),(13,'Hotel1/Tipo3/Img4.jpg',3),(14,'Hotel2/Tipo1/Img1.jpg',4),(15,'Hotel2/Tipo1/Img2.jpg',4),(16,'Hotel2/Tipo1/Img3.jpg',4),(17,'Hotel2/Tipo1/Img4.jpg',4),(18,'Hotel2/Tipo2/Img1.jpg',5),(19,'Hotel2/Tipo2/Img2.jpg',5),(20,'Hotel2/Tipo2/Img3.jpg',5),(21,'Hotel2/Tipo2/Img4.jpg',5),(22,'Hotel2/Tipo3/Img1.jpg',6),(23,'Hotel2/Tipo3/Img2.jpg',6),(24,'Hotel2/Tipo3/Img3.jpg',6),(25,'Hotel3/Tipo1/Img1.jpg',7),(26,'Hotel3/Tipo1/Img2.jpg',7),(27,'Hotel3/Tipo1/Img3.jpg',7),(28,'Hotel3/Tipo2/Img1.jpg',8),(29,'Hotel3/Tipo2/Img2.jpg',8),(30,'Hotel3/Tipo2/Img3.jpg',8),(31,'Hotel3/Tipo3/Img1.jpg',9),(32,'Hotel3/Tipo3/Img2.jpg',9),(33,'Hotel3/Tipo3/Img3.jpg',9),(34,'Hotel3/Tipo4/Img1.jpg',10),(35,'Hotel3/Tipo4/Img2.jpg',10),(36,'Hotel3/Tipo4/Img3.jpg',10),(37,'Hotel3/Tipo4/Img4.jpg',10),(38,'Hotel3/Tipo4/Img5.jpg',10),(39,'Hotel3/Tipo4/Img6.jpg',10),(40,'Hotel4/Tipo1/Img1.jpg',11),(41,'Hotel4/Tipo1/Img2.jpg',11),(42,'Hotel4/Tipo1/Img3.jpg',11),(43,'Hotel4/Tipo1/Img4.jpg',11),(44,'Hotel4/Tipo2/Img1.jpg',12),(45,'Hotel4/Tipo2/Img2.jpg',12),(46,'Hotel4/Tipo2/Img3.jpg',12),(47,'Hotel4/Tipo2/Img4.jpg',12),(48,'Hotel4/Tipo2/Img5.jpg',12),(49,'Hotel4/Tipo3/Img1.jpg',13),(50,'Hotel4/Tipo3/Img2.jpg',13),(51,'Hotel4/Tipo3/Img3.jpg',13),(52,'Hotel4/Tipo3/Img4.jpg',13),(53,'Hotel5/Tipo1/Img1.jpg',14),(54,'Hotel5/Tipo1/Img2.jpg',14),(55,'Hotel5/Tipo1/Img3.jpg',14),(56,'Hotel5/Tipo2/Img1.jpg',15),(57,'Hotel5/Tipo2/Img2.jpg',15),(58,'Hotel5/Tipo2/Img3.jpg',15),(59,'Hotel5/Tipo3/Img1.jpg',16),(60,'Hotel5/Tipo3/Img2.jpg',16),(61,'Hotel5/Tipo3/Img3.jpg',16),(62,'Hotel6/Tipo1/Img1.jpg',17),(63,'Hotel6/Tipo1/Img2.jpg',17),(64,'Hotel6/Tipo1/Img3.jpg',17),(65,'Hotel6/Tipo2/Img1.jpg',18),(66,'Hotel6/Tipo2/Img2.jpg',18),(67,'Hotel6/Tipo2/Img3.jpg',18),(68,'Hotel6/Tipo3/Img1.jpg',19),(69,'Hotel7/Tipo1/Img1.jpg',20),(70,'Hotel7/Tipo1/Img2.jpg',20),(71,'Hotel7/Tipo1/Img3.jpg',20),(72,'Hotel7/Tipo1/Img4.jpg',20),(73,'Hotel7/Tipo2/Img1.jpg',21),(74,'Hotel7/Tipo2/Img2.jpg',21),(75,'Hotel7/Tipo2/Img3.jpg',21),(76,'Hotel7/Tipo2/Img4.jpg',21),(77,'Hotel7/Tipo3/Img1.jpg',22),(78,'Hotel7/Tipo3/Img2.jpg',22),(79,'Hotel7/Tipo3/Img3.jpg',22),(80,'Hotel7/Tipo4/Img1.jpg',23),(81,'Hotel7/Tipo4/Img2.jpg',23),(82,'Hotel7/Tipo4/Img3.jpg',23),(83,'Hotel8/Tipo1/Img1.jpg',24),(84,'Hotel8/Tipo1/Img2.jpg',24),(85,'Hotel8/Tipo2/Img1.jpg',25),(86,'Hotel8/Tipo2/Img2.jpg',25),(87,'Hotel8/Tipo3/Img1.jpg',26),(88,'Hotel8/Tipo3/Img2.jpg',26),(89,'Hotel9/Tipo1/Img1.jpg',27),(90,'Hotel9/Tipo1/Img2.jpg',27),(91,'Hotel9/Tipo1/Img3.jpg',27),(92,'Hotel9/Tipo2/Img1.jpg',28),(93,'Hotel9/Tipo2/Img2.jpg',28),(94,'Hotel9/Tipo2/Img3.jpg',28),(95,'Hotel10/Tipo1/Img1.jpg',29),(96,'Hotel10/Tipo1/Img2.jpg',29),(97,'Hotel10/Tipo1/Img3.jpg',29),(98,'Hotel10/Tipo2/Img1.jpg',30),(99,'Hotel10/Tipo2/Img2.jpg',30),(100,'Hotel10/Tipo2/Img3.jpg',30);
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
  `ImgHotel` varchar(200) NOT NULL,
  `HotelID` int NOT NULL,
  PRIMARY KEY (`ImgHotelID`,`HotelID`),
  KEY `HotelID` (`HotelID`),
  CONSTRAINT `ImgHoteles_ibfk_1` FOREIGN KEY (`HotelID`) REFERENCES `Hoteles` (`HotelID`)
) ENGINE=InnoDB AUTO_INCREMENT=75 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ImgHoteles`
--

LOCK TABLES `ImgHoteles` WRITE;
/*!40000 ALTER TABLE `ImgHoteles` DISABLE KEYS */;
INSERT INTO `ImgHoteles` VALUES (1,'Hotel1/Img1.jpg',1),(2,'Hotel1/Img2.jpg',1),(3,'Hotel1/Img3.jpg',1),(4,'Hotel1/Img4.jpg',1),(5,'Hotel1/Img5.jpg',1),(6,'Hotel2/Img1.jpg',2),(7,'Hotel2/Img2.jpg',2),(8,'Hotel2/Img3.jpg',2),(9,'Hotel2/Img4.jpg',2),(10,'Hotel2/Img5.jpg',2),(11,'Hotel2/Img6.jpg',2),(12,'Hotel2/Img7.jpg',2),(13,'Hotel3/Img1.jpg',3),(14,'Hotel3/Img2.jpg',3),(15,'Hotel3/Img3.jpg',3),(16,'Hotel3/Img4.jpg',3),(17,'Hotel3/Img5.jpg',3),(18,'Hotel3/Img6.jpg',3),(19,'Hotel3/Img7.jpg',3),(20,'Hotel3/Img8.jpg',3),(21,'Hotel4/Img1.jpg',4),(22,'Hotel4/Img2.jpg',4),(23,'Hotel4/Img3.jpg',4),(24,'Hotel4/Img4.jpg',4),(25,'Hotel4/Img5.jpg',4),(26,'Hotel4/Img6.jpg',4),(27,'Hotel4/Img7.jpg',4),(28,'Hotel4/Img8.jpg',4),(29,'Hotel4/Img9.jpg',4),(30,'Hotel5/Img1.jpg',5),(31,'Hotel5/Img2.jpg',5),(32,'Hotel5/Img3.jpg',5),(33,'Hotel5/Img4.jpg',5),(34,'Hotel5/Img5.jpg',5),(35,'Hotel5/Img6.jpg',5),(36,'Hotel5/Img7.jpg',5),(37,'Hotel5/Img8.jpg',5),(38,'Hotel6/Img1.jpg',6),(39,'Hotel6/Img2.jpg',6),(40,'Hotel6/Img3.jpg',6),(41,'Hotel6/Img4.jpg',6),(42,'Hotel6/Img5.jpg',6),(43,'Hotel6/Img6.jpg',6),(44,'Hotel7/Img1.jpg',7),(45,'Hotel7/Img2.jpg',7),(46,'Hotel7/Img3.jpg',7),(47,'Hotel7/Img4.jpg',7),(48,'Hotel7/Img5.jpg',7),(49,'Hotel7/Img6.jpg',7),(50,'Hotel7/Img7.jpg',7),(51,'Hotel7/Img8.jpg',7),(52,'Hotel7/Img9.jpg',7),(53,'Hotel7/Img10.jpg',7),(54,'Hotel8/Img1.jpg',8),(55,'Hotel8/Img2.jpg',8),(56,'Hotel8/Img3.jpg',8),(57,'Hotel8/Img4.jpg',8),(58,'Hotel8/Img5.jpg',8),(59,'Hotel8/Img6.jpg',8),(60,'Hotel8/Img7.jpg',8),(61,'Hotel9/Img1.jpg',9),(62,'Hotel9/Img2.jpg',9),(63,'Hotel9/Img3.jpg',9),(64,'Hotel9/Img4.jpg',9),(65,'Hotel9/Img5.jpg',9),(66,'Hotel9/Img6.jpg',9),(67,'Hotel9/Img7.jpg',9),(68,'Hotel10/Img1.jpg',10),(69,'Hotel10/Img2.jpg',10),(70,'Hotel10/Img3.jpg',10),(71,'Hotel10/Img4.jpg',10),(72,'Hotel10/Img5.jpg',10),(73,'Hotel10/Img6.jpg',10),(74,'Hotel10/Img7.jpg',10);
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
  `Creacion` datetime NOT NULL,
  `Desde` datetime NOT NULL,
  `Hasta` datetime NOT NULL,
  `CantNiños` int DEFAULT NULL,
  `CantAdultos` int NOT NULL,
  `PrecioTotal` int NOT NULL,
  `HabitacionID` int NOT NULL,
  `UsuarioID` int NOT NULL,
  PRIMARY KEY (`ReservaID`,`HabitacionID`,`UsuarioID`),
  KEY `HabitacionID` (`HabitacionID`),
  KEY `UsuarioID` (`UsuarioID`),
  CONSTRAINT `Reservas_ibfk_1` FOREIGN KEY (`HabitacionID`) REFERENCES `Habitaciones` (`HabitacionID`),
  CONSTRAINT `Reservas_ibfk_2` FOREIGN KEY (`UsuarioID`) REFERENCES `Usuarios` (`UsuarioID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Reservas`
--

LOCK TABLES `Reservas` WRITE;
/*!40000 ALTER TABLE `Reservas` DISABLE KEYS */;
INSERT INTO `Reservas` VALUES (1,'2024-11-15 20:05:21','2025-01-14 00:00:00','2025-01-29 00:00:00',0,2,88650,6,3);
/*!40000 ALTER TABLE `Reservas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ServiciosContratados`
--

DROP TABLE IF EXISTS `ServiciosContratados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ServiciosContratados` (
  `ServicioContratadoID` int NOT NULL AUTO_INCREMENT,
  `Creacion` datetime NOT NULL,
  `PrecioTotal` int NOT NULL,
  `ServicioID` int NOT NULL,
  `ReservaID` int NOT NULL,
  PRIMARY KEY (`ServicioContratadoID`,`ServicioID`,`ReservaID`),
  KEY `ServicioID` (`ServicioID`),
  KEY `ReservaID` (`ReservaID`),
  CONSTRAINT `ServiciosContratados_ibfk_1` FOREIGN KEY (`ServicioID`) REFERENCES `Servicios` (`ServicioID`),
  CONSTRAINT `ServiciosContratados_ibfk_2` FOREIGN KEY (`ReservaID`) REFERENCES `Reservas` (`ReservaID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ServiciosContratados`
--

LOCK TABLES `ServiciosContratados` WRITE;
/*!40000 ALTER TABLE `ServiciosContratados` DISABLE KEYS */;
/*!40000 ALTER TABLE `ServiciosContratados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Servicios`
--

DROP TABLE IF EXISTS `Servicios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Servicios` (
  `ServicioID` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(45) NOT NULL,
  `Descripcion` varchar(200) DEFAULT NULL,
  `Precio` int NOT NULL,
  `ImgServicio` varchar(200) DEFAULT NULL,
  `HotelID` int NOT NULL,
  `TipoDePago` varchar(45) NOT NULL,
  PRIMARY KEY (`ServicioID`,`HotelID`),
  KEY `HotelID` (`HotelID`),
  CONSTRAINT `Servicios_ibfk_1` FOREIGN KEY (`HotelID`) REFERENCES `Hoteles` (`HotelID`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Servicios`
--

LOCK TABLES `Servicios` WRITE;
/*!40000 ALTER TABLE `Servicios` DISABLE KEYS */;
INSERT INTO `Servicios` VALUES (1,'Enlace con el aeropuerto','Traslados privados cómodos y puntuales entre el aeropuerto y el hotel, con vehículos modernos y aire acondicionado.',70000,'Hotel1/Servicios/Img1.jpg',1,'Único'),(2,'Servicio a la habitación','Disfruta de platos a la carta, refrescos, snacks y artículos de primera necesidad desde la comodidad de tu habitación las 24 horas. El precio solo incluye la disposición del personal',50000,'Hotel2/Servicios/Img1.jpg',2,'Por día'),(3,'Traslado aeropuerto-hotel','Olvidate del estrés al llegar. Ofrecemos traslados 24/7, asegurando que tu llegada y salida sean siempre puntuales y sin contratiempos.',100000,'Hotel2/Servicios/Img2.jpg',2,'Único'),(4,'Masajes','Relajate con masajes terapéuticos, desde sueco hasta descontracturante, para aliviar tensiones y mejorar tu bienestar físico y mental.',100000,'Hotel3/Servicios/Img1.jpg',3,'Por persona'),(5,'Gimnasio','Gimnasio totalmente equipado con máquinas de cardio, pesas y zona de estiramientos, además de entrenadores personales a tu disposición.',140000,'Hotel3/Servicios/Img2.jpg',3,'Por persona'),(6,'Desayuno buffet','Desayuno buffet: cereales, frutas frescas, jugos naturales, panes, croissants, yogures, quesos, embutidos, y opciones calientes como huevos y tocino.',100000,'Hotel4/Servicios/Img1.jpg',4,'Por persona'),(7,'Gimnasio','Mantente activo durante tu estancia en nuestro gimnasio, que cuenta con equipos para ejercitarte a cualquier hora del día.',100000,'Hotel5/Servicios/Img1.jpg',5,'Por persona'),(8,'Spa','Relájate en nuestro spa con sauna, bañera de hidromasaje y solárium, diseñados para restaurar tu energía y bienestar.',120000,'Hotel5/Servicios/Img2.jpg',5,'Por persona'),(9,'Desayuno a la habitación','Comienza el día con un delicioso desayuno a la habitación, que incluye opciones como panadería fresca, frutas, café, jugos y platos calientes, todo servido directamente en tu puerta.',130000,'Hotel6/Servicios/Img1.jpg',6,'Por persona'),(10,'Servicio a la Habitación','Disfruta de la comodidad de nuestro servicio a la habitación. Amplia variedad de platos y bebidas, disponibles las 24 horas.',50000,'Hotel7/Servicios/Img1.jpg',7,'Por día'),(11,'Gimnasio','Mantené tu rutina en forma mientras viajás. Nuestro gimnasio te ofrece todo lo que necesitás: máquinas de cardio, pesas libres y más. Perfecto para recargar energías',160000,'Hotel7/Servicios/Img2.jpg',7,'Por persona'),(12,'Zona de Spa','Nuestra zona de spa incluye sauna y bañera de hidromasaje, diseñados para ofrecerte comodidad y relajación en un entorno privado y exclusivo.',180000,'Hotel7/Servicios/Img3.jpg',7,'Por persona'),(13,'Parking Privado','Nuestro parking privado ofrece seguridad y comodidad, con plazas exclusivas para huéspedes. Acceso controlado y ubicado cerca del hotel para tu mayor tranquilidad y facilidad.',20000,'Hotel7/Servicios/Img4.jpg',7,'Por día'),(14,'Traslado aeropuerto','Traslado para ir o volver del aeropuerto',60000,'Hotel8/Servicios/Img1.jpg',8,'Único'),(15,'Desayuno buffet','Disfruta de un desayuno buffet con una amplia variedad de opciones para todos los gustos.',120000,'Hotel9/Servicios/Img1.jpg',9,'Por persona'),(16,'Conexión con el aeropuerto','El hotel ofrece servicio de traslado entre el aeropuerto y el hotel, disponible bajo solicitud previa.',80000,'Hotel9/Servicios/Img2.jpg',9,'Único'),(17,'Servicio a la habitación','Disfruta de la comodidad de recibir tu comida, bebida o artículos en la habitación las 24 horas. El servicio incluye solo el trabajo del personal, y los productos solicitados se cobran aparte.',35000,'Hotel10/Servicios/Img1.jpg',10,'Por día'),(18,'Spa','Disfruta de nuestro spa con sauna y baños de vapor, ideales para relajarte y revitalizarte en un ambiente tranquilo y acogedor.',130000,'Hotel10/Servicios/Img2.jpg',10,'Por persona'),(19,'Gimnasio','Accede a nuestro gimnasio con equipos de cardio y pesas para mantenerte en forma durante tu estancia. Un espacio cómodo y funcional, disponible para ti en cualquier momento del día.',110000,'Hotel10/Servicios/Img3.jpg',10,'Por persona');
/*!40000 ALTER TABLE `Servicios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TiposDeHabitacion`
--

DROP TABLE IF EXISTS `TiposDeHabitacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TiposDeHabitacion` (
  `TipoID` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(100) NOT NULL,
  `CantHuespedes` int NOT NULL,
  `Descripcion` varchar(500) NOT NULL,
  `Superficie` int NOT NULL,
  `PrecioAdulto` int NOT NULL,
  `PrecioNiño` int DEFAULT NULL,
  `HotelID` int NOT NULL,
  PRIMARY KEY (`TipoID`,`HotelID`),
  KEY `HotelID` (`HotelID`),
  CONSTRAINT `TiposDeHabitacion_ibfk_1` FOREIGN KEY (`HotelID`) REFERENCES `Hoteles` (`HotelID`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TiposDeHabitacion`
--

LOCK TABLES `TiposDeHabitacion` WRITE;
/*!40000 ALTER TABLE `TiposDeHabitacion` DISABLE KEYS */;
INSERT INTO `TiposDeHabitacion` VALUES (1,'Habitacion individual económica',1,'Habitación interior con aire acondicionado, caja fuerte y TV de pantalla plana por cable. Incluye baño privado con ducha.',12,38717,NULL,1),(2,'Habitación doble',2,'Habitación interior con escritorio cómodo, aire acondicionado, caja fuerte y TV de pantalla plana por cable. Incluye baño privado con ducha.',15,44325,37535,1),(3,'Suite',3,'Suite amplia de 2 habitaciones comunicadas con baño, escritorio y TV por cable. Tiene vistas a la avenida 9 de Julio.',30,68574,55768,1),(4,'Habitación con cama extragrande y vistas a la ciudad',2,'Esta habitación doble cuenta con aire acondicionado, TV de pantalla plana con canales por cable, tetera/cafetera, caja fuerte y calefacción. Incluye 1 cama.',23,143949,117534,2),(5,'Habitación Doble Estándar con vistas al lago - 2 camas',2,'La habitación doble cuenta con aire acondicionado, tetera/cafetera, caja fuerte, calefacción y TV de pantalla plana con canales por cable. El alojamiento dispone de 2 camas.',23,177703,148452,2),(6,'Habitación Doble con 2 camas dobles y vistas al lago',4,'La habitación cuádruple cuenta con aire acondicionado, TV de pantalla plana con canales por cable, tetera/cafetera, caja fuerte y calefacción. El alojamiento dispone de 2 camas.',23,307753,256379,2),(7,'Habitación Clásica',2,'Cuenta con 1 cama doble grande o 2 camas individuales, TV de pantalla plana, minibar, aire acondicionado y baño privado.',28,341506,273956,3),(8,'Habitación Premium con 2 camas extragrandes',4,'Esta habitación doble cuenta con artículos de aseo gratuitos y baño privado con ducha, bidet y secador de pelo. La amplia habitación doble cuenta con aire acondicionado, TV de pantalla plana con canales por cable, minibar, cafetera y armario. La unidad tiene 2 camas.',32,509926,413196,3),(9,'Suite Junior con cama extragrande',2,'La Junior Suite ofrece una sala de estar independiente con sofá y minibar.',56,564874,440904,3),(10,'Suite Presidencial',2,'Esta suite incluye bañera de hidromasaje. Esta suite tiene baño privado con artículos de aseo gratuitos, ducha, bidet y secador de pelo. La cocina de la suite tiene nevera, microondas y espacio para guardar comida. La suite es amplia y tiene aire acondicionado, TV de pantalla plana con canales por cable, minibar, tetera, cafetera y acceso al salón executive.',192,965447,727531,3),(11,'Habitación Doble',2,'Esta habitación doble tiene piscina con vistas. Esta habitación doble ofrece aire acondicionado, TV de pantalla plana con servicio de streaming, baño privado y balcón con vistas al jardín.',25,80413,61532,4),(12,'Suite con bañera de hidromasaje - Cama extragrande',4,'Esta suite cuenta con piscina con vistas y bañera de hidromasaje. Esta suite cuenta con sala de estar, 1 dormitorio independiente y baño con bañera y artículos de aseo gratuitos. La suite dispone de aire acondicionado, paredes insonorizadas, minibar, tetera/cafetera, TV de pantalla plana con servicio de streaming y vistas al jardín. El alojamiento incluye 3 camas.',40,109897,83180,4),(13,'Habitación Triple',3,'La habitación está equipada con 3 camas individuales, aire acondicionado, TV LCD por cable y balcón privado.',25,91134,69691,4),(14,'Habitación Doble Deluxe',2,'Esta habitación dispone de aire acondicionado, balcón con vistas al jardín y a la piscina, Hay TV de pantalla plana, escritorio, calefacción y caja fuerte. El baño privado cuenta con artículos de aseo gratuitos, secador de pelo y ducha. Se facilita ropa de cama.',22,127072,103153,5),(15,'Apartamento',3,'Este apartamento con aire acondicionado dispone de balcón con vistas al jardín y a la piscina. Hay TV de pantalla plana, escritorio, calefacción y caja fuerte. También tiene baño privado con bañera, secador de pelo y artículos de aseo gratuitos. Se facilita ropa de cama.',30,171249,152916,5),(16,'Suite Master',2,'Esta suite con aire acondicionado dispone de balcón con vistas al jardín y a la piscina. Hay TV de pantalla plana, escritorio, calefacción y caja fuerte. También tiene baño privado con bañera, secador de pelo y artículos de aseo gratuitos. Se facilita ropa de cama.',50,154869,119823,5),(17,'Doble Superior',2,'No se pueden añadir camas supletorias en esta habitación.',33,114166,88812,6),(18,'Habitación Doble Executive - 1 o 2 camas',2,'Hay zona de estar con sofá.',41,119130,91574,6),(19,'Suite Deluxe',2,'Incluye zonas de estar y de comedor.',61,124094,99047,6),(20,'Habitación Deluxe',2,'Habitación doble amplia con aire acondicionado, minibar, balcón con vistas a una calle tranquila y baño privado con ducha. El alojamiento incluye 1 cama.',32,191065,141794,7),(21,'Habitación Doble con vistas a la montaña',2,'Esta habitación doble es amplia y dispone de aire acondicionado, minibar, balcón con vistas al jardín y baño privado con ducha. Tiene 1 cama.',32,229275,180063,7),(22,'Suite Junior con vistas a la montaña',2,'Esta suite tiene aire acondicionado, dormitorio y baño con ducha y bidet. La suite dispone de balcón con vistas al jardín, minibar y TV de pantalla plana por cable. El alojamiento cuenta con 1 cama.',32,248376,192301,7),(23,'Suite con bañera de hidromasaje - Cama extragrande',2,'Esta suite cuenta con bañera de hidromasaje. Esta suite tiene zona de estar, dormitorio independiente y baño con ducha y artículos de aseo gratuitos. La suite ofrece vistas al jardín y dispone de aire acondicionado, TV de pantalla plana por cable, minibar, cafetera y zona de estar. El alojamiento cuenta con 2 camas.',50,324808,256459,7),(24,'Habitación Doble',2,'Esta habitación cuenta con baño privado.',17,59565,44239,8),(25,'Habitación Triple',3,'Esta habitación cuenta con baño privado.',20,74456,58824,8),(26,'Habitación Cuádruple Clásica',4,'Tiene 3 camas.',22,99275,76709,8),(27,'Habitación Doble',2,'Esta habitación doble incluye baño privado con ducha. La habitación doble cuenta con aire acondicionado, TV de pantalla plana, zona de comedor, armario, caja fuerte y vistas al jardín. La unidad dispone de 1 cama.',22,160825,121533,9),(28,'Habitación Doble - 2 camas',2,'Esta habitación doble incluye artículos de aseo gratuitos con baño privado con ducha. La habitación doble con aire acondicionado, TV de pantalla plana, zona de comedor, armario, caja fuerte y vistas al jardín. La unidad tiene 2 camas.',22,178695,133929,9),(29,'Habitación Doble Superior - 2 camas',2,'Habitación insonorizada y equipada con 2 camas individuales, minibar y aire acondicionado.',34,112409,73104,10),(30,'Suite Junior',2,'Los huéspedes tendrán una experiencia especial ya que esta suite ofrece una bañera de hidromasaje y un baño de spa. La suite cuenta con aire acondicionado, 1 dormitorio y 1 baño con ducha y bidet. La suite cuenta con suelos de moquetas, zona de estar con TV de pantalla plana con canales por cable, paredes insonorizadas, minibar, así como armario. La unidad dispone de 1 cama.',43,125632,79646,10);
/*!40000 ALTER TABLE `TiposDeHabitacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Usuarios`
--

DROP TABLE IF EXISTS `Usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Usuarios` (
  `UsuarioID` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(45) NOT NULL,
  `Apellido` varchar(45) NOT NULL,
  `Nacimiento` date NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Contraseña` varchar(45) NOT NULL,
  `Telefono` varchar(45) NOT NULL,
  `DNI` varchar(45) NOT NULL,
  `Pais` varchar(45) NOT NULL,
  PRIMARY KEY (`UsuarioID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Usuarios`
--

LOCK TABLES `Usuarios` WRITE;
/*!40000 ALTER TABLE `Usuarios` DISABLE KEYS */;
INSERT INTO `Usuarios` VALUES (1,'Mariano','Alvarez','2000-10-21','marianoalvarez@gmail.com','mariano2024','+54 11 2342-5398','41294180','Argentina'),(2,'Carlos','Alvarez','1989-05-23','alvarez099@gmail.com','carloscarlos099','+54 11 9384-1627','33738193','Argentina'),(3,'Gustavo','Perez','1992-02-21','gusti1992@gmail.com','gusti1992','+54 11 1539-9390','36902746','Argentina'),(4,'Alberto','Martinez','1970-10-23','alberto@gmail.com','albertoma123','+54 11 6542-5165','21133859','Argentina');
/*!40000 ALTER TABLE `Usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-27 21:56:15
