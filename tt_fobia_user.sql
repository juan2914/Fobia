CREATE DATABASE  IF NOT EXISTS `tt_fobia` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_spanish_ci */;
USE `tt_fobia`;
-- MySQL dump 10.13  Distrib 8.0.15, for Win64 (x86_64)
--
-- Host: localhost    Database: tt_fobia
-- ------------------------------------------------------
-- Server version	8.0.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `user` (
  `IdUser` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(45) COLLATE utf8_spanish_ci DEFAULT NULL,
  `ApPaterno` varchar(45) COLLATE utf8_spanish_ci DEFAULT NULL,
  `ApMaterno` varchar(45) COLLATE utf8_spanish_ci DEFAULT NULL,
  `Domicilio` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `Edad` int(11) DEFAULT NULL,
  `Telefono` varchar(45) COLLATE utf8_spanish_ci DEFAULT NULL,
  `Especialidad` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `Correo` varchar(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `Usuario` varchar(45) COLLATE utf8_spanish_ci NOT NULL,
  `Password` varchar(45) COLLATE utf8_spanish_ci NOT NULL,
  `Tipo` int(11) NOT NULL,
  `Imagen` varchar(250) COLLATE utf8_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`IdUser`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'PurebaPsico','PurebaPsico','PurebaPsico','dom',10,'789456123','esp','corr@mail.com','user','user',2,NULL),(17,'Gabriela','Enriquez','Cervantes','calle numero colonia  delegacion cp ciudad',25,'5567409232','TAS','juan.glez2914@gmail.com','gbs2019','gbs2019',2,NULL),(19,'admin','admin','admin','admin',0,'0','admin','admin@l.c','admin','admin',1,NULL),(21,'VamoA','Calmarno','llll','asdfa',1,'1','asdfa','vamo@calmarno.com','vamo','vamo',2,'C:\\Users\\Boomerang\\Desktop\\Interfaz\\Desktop\\ProfilePictures\\13740image.jpg');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-12 13:04:02
