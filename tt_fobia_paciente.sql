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
-- Table structure for table `paciente`
--

DROP TABLE IF EXISTS `paciente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `paciente` (
  `IdPaciente` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(45) COLLATE utf8_spanish_ci NOT NULL,
  `ApPaterno` varchar(45) COLLATE utf8_spanish_ci NOT NULL,
  `ApMaterno` varchar(45) COLLATE utf8_spanish_ci NOT NULL,
  `Domicilio` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `Edad` int(11) NOT NULL,
  `Telefono` varchar(45) COLLATE utf8_spanish_ci DEFAULT NULL,
  `Correo` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `Sexo` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `Comentario` text COLLATE utf8_spanish_ci,
  `IdUser` int(11) NOT NULL,
  `Imagen` varchar(250) COLLATE utf8_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`IdPaciente`),
  KEY `fk_IdUser_idx` (`IdUser`),
  CONSTRAINT `fk_IdUser` FOREIGN KEY (`IdUser`) REFERENCES `user` (`IdUser`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paciente`
--

LOCK TABLES `paciente` WRITE;
/*!40000 ALTER TABLE `paciente` DISABLE KEYS */;
INSERT INTO `paciente` VALUES (6,'asf','asdf','asdf','asdf',1234,'123','a@l.v','Masculino','asdfasdf',1,NULL),(7,'NAMEs','paterno','materno','calle calle',20,'222222222','algo@algo.com','Masculino','',1,NULL),(8,'repainter','repaint','repaint','repaint',1,'1','repaint@repaint.com','Masculino','repaintrepaintrepaint',1,NULL),(9,'re','r','r','r',1,'1','r@r.r','Masculino','qewr',1,NULL),(10,'nombrecambio','w','w','wr',1,'1','w1@l.s','Masculino','ss',1,NULL),(12,'asdfasdf','asdfasdf','asdfasdf','asdfasdf',1,'1234','as@l.c','Masculino','asdfsadf',1,'C:UsersBoomerangDesktopInterfazDesktopProfilePicturesimage.jpg'),(13,'qwer','qwer','qwer','qwer',2,'2','qw1@l.w','Masculino','qwer',1,'C:\\Users\\Boomerang\\Desktop\\Interfaz\\Desktop\\ProfilePictures\\image.jpg'),(14,'rutyu','rtuy','rtuy','rrtyu',34,'4','f@l.f','Masculino','asdf',1,'C:\\Users\\Boomerang\\Desktop\\Interfaz\\Desktop\\ProfilePictures\\image.jpg'),(15,'ui','ui','ui','ui',6,'56','ui@sd.d','Masculino','uiu',1,'C:\\Users\\Boomerang\\Desktop\\Interfaz\\Desktop\\ProfilePictures\\image.jpg132810'),(16,'Vamo','A','Calmarno','Agua',1,'56','vamoacalmarno@gmail.com','Masculino','g',1,'C:\\Users\\Boomerang\\Desktop\\Interfaz\\Desktop\\ProfilePictures\\13380image.jpg'),(18,'r','r','r','r',3,'2','r@r','Masculino','3',1,'C:\\Users\\Boomerang\\Desktop\\Interfaz\\Desktop\\ProfilePictures\\C:\\Users\\Boomerang\\Desktop\\Interfaz\\Desktop\\ProfilePictures'),(21,'vamo','a','calmarno','pokemon',2,'12','vamo@calmarno.com','Masculino','',21,'C:\\Users\\Boomerang\\Desktop\\Interfaz\\Desktop\\ProfilePictures\\95456MR.jpg'),(22,'vamo','vamo','vamo','vamo',2,'2','sl@k.d','Masculino','asdfa',17,'');
/*!40000 ALTER TABLE `paciente` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-12 13:03:59
