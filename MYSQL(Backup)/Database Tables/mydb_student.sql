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
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `student` (
  `StudentID` int(11) NOT NULL,
  `StudentFname` varchar(45) DEFAULT NULL,
  `StudentLname` varchar(45) DEFAULT NULL,
  `Gradelevel_GradelevelID` int(11) NOT NULL,
  `Teacher_TeacherID` int(11) NOT NULL,
  `Instrument_InstrumentID` int(11) NOT NULL,
  PRIMARY KEY (`StudentID`,`Gradelevel_GradelevelID`,`Teacher_TeacherID`,`Instrument_InstrumentID`),
  KEY `fk_Student_Gradelevel1_idx` (`Gradelevel_GradelevelID`),
  KEY `fk_Student_Teacher1_idx` (`Teacher_TeacherID`),
  KEY `fk_Student_Instrument1_idx` (`Instrument_InstrumentID`),
  CONSTRAINT `fk_Student_Gradelevel1` FOREIGN KEY (`Gradelevel_GradelevelID`) REFERENCES `gradelevel` (`GradelevelID`),
  CONSTRAINT `fk_Student_Instrument1` FOREIGN KEY (`Instrument_InstrumentID`) REFERENCES `instrument` (`InstrumentID`),
  CONSTRAINT `fk_Student_Teacher1` FOREIGN KEY (`Teacher_TeacherID`) REFERENCES `teacher` (`TeacherID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (1,'Isaac','Yocum',1,1,1),(2,'Raidan','Christopherson',2,2,2),(3,'Nik ','Jenson',1,2,3),(4,'Easton','Shurtliff',1,1,4),(5,'Jared','Martin',2,2,5),(6,'patrickJR','Star',3,1,6);
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-20 11:02:02
