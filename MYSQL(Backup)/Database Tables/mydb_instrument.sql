-- MySQL dump 10.13  Distrib 8.0.15, for Win64 (x86_64)
--
-- Host: localhost    Database: mydb
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
-- Table structure for table `instrument`
--

DROP TABLE IF EXISTS `instrument`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `instrument` (
  `InstrumentID` int(11) NOT NULL,
  `InstrumentName` varchar(45) NOT NULL,
  `InstrumentLost` varchar(1) NOT NULL,
  `InstrumentCheckedOut` varchar(1) NOT NULL,
  `CheckOutDate` date NOT NULL,
  `ReturnDate` date NOT NULL,
  PRIMARY KEY (`InstrumentID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `instrument`
--

LOCK TABLES `instrument` WRITE;
/*!40000 ALTER TABLE `instrument` DISABLE KEYS */;
INSERT INTO `instrument` VALUES (1,'Trumpet','0','1','2019-03-18','2019-05-18'),(2,'Trumpet','0','1','2019-03-18','2019-05-18'),(3,'Piano','0','1','2019-03-18','2019-05-18'),(4,'Piano','0','1','2019-03-18','2019-05-18'),(5,'Violine','0','1','2019-03-18','2019-05-18'),(6,'Guitar','0','1','2019-04-03','2019-06-03'),(7,'Guitar ','0','0','0000-00-00','0000-00-00'),(8,'Flute','0','0','0000-00-00','0000-00-00'),(9,'Flute','0','0','0000-00-00','0000-00-00'),(10,'Drum','0','0','0000-00-00','0000-00-00'),(11,'Drum','0','0','0000-00-00','0000-00-00'),(12,'Recorder','0','0','0000-00-00','0000-00-00'),(13,'Recorder','0','0','0000-00-00','0000-00-00'),(14,'Recorder','0','0','0000-00-00','0000-00-00'),(15,'Recorder','0','0','0000-00-00','0000-00-00'),(16,'Recorder','0','0','0000-00-00','0000-00-00'),(17,'Recorder','0','0','0000-00-00','0000-00-00'),(18,'Recorder','0','0','0000-00-00','0000-00-00'),(19,'Recorder','0','0','0000-00-00','0000-00-00'),(20,'Recorder','0','0','0000-00-00','0000-00-00'),(21,'Recorder','0','0','0000-00-00','0000-00-00'),(22,'Recorder','0','0','0000-00-00','0000-00-00'),(23,'Recorder','0','0','0000-00-00','0000-00-00'),(24,'Recorder','0','0','0000-00-00','0000-00-00'),(25,'Recorder','0','0','0000-00-00','0000-00-00'),(26,'Recorder','0','0','0000-00-00','0000-00-00'),(27,'Recorder','0','0','0000-00-00','0000-00-00'),(28,'Recorder','0','0','0000-00-00','0000-00-00'),(29,'Recorder','0','0','0000-00-00','0000-00-00'),(30,'Recorder','0','0','0000-00-00','0000-00-00'),(31,'Recorder','0','0','0000-00-00','0000-00-00'),(32,'Bass','0','0','0000-00-00','0000-00-00'),(33,'Bass','0','0','0000-00-00','0000-00-00');
/*!40000 ALTER TABLE `instrument` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-20 11:02:01
