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
-- Table structure for table `parent`
--

DROP TABLE IF EXISTS `parent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `parent` (
  `ParentID` int(11) NOT NULL,
  `ParentFname` varchar(45) DEFAULT NULL,
  `parentLname` varchar(45) DEFAULT NULL,
  `parentEmail` varchar(45) DEFAULT NULL,
  `Parentusername` varchar(45) DEFAULT NULL,
  `ParentPassword` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`ParentID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parent`
--

LOCK TABLES `parent` WRITE;
/*!40000 ALTER TABLE `parent` DISABLE KEYS */;
INSERT INTO `parent` VALUES (1,'jay','james','jj@gmail.com','jj','$5$rounds=535000$7DHPNBXcGi8Va14R$y1yqTRK0N/cA90QDfZudBlXg66ED90nDfcCbpTfOhPD'),(2,'mark','mark','mm@gmail.com','mm','$5$rounds=535000$7DHPNBXcGi8Va14R$y1yqTRK0N/cA90QDfZudBlXg66ED90nDfcCbpTfOhPD'),(3,'Sarah','Sarah','SS@gmail.com','ss','$5$rounds=535000$7DHPNBXcGi8Va14R$y1yqTRK0N/cA90QDfZudBlXg66ED90nDfcCbpTfOhPD'),(4,'Terra','Terra','tt@gmail.com','tt','$5$rounds=535000$7DHPNBXcGi8Va14R$y1yqTRK0N/cA90QDfZudBlXg66ED90nDfcCbpTfOhPD'),(5,'Stacey','Sell','Sst@gmail.com','sst','$5$rounds=535000$7DHPNBXcGi8Va14R$y1yqTRK0N/cA90QDfZudBlXg66ED90nDfcCbpTfOhPD'),(6,'Monty','mon','mmm@gmail.com','mmt','$5$rounds=535000$7DHPNBXcGi8Va14R$y1yqTRK0N/cA90QDfZudBlXg66ED90nDfcCbpTfOhPD'),(7,'Ashley','teacher','atech@gmai.com','atech','$5$rounds=535000$7DHPNBXcGi8Va14R$y1yqTRK0N/cA90QDfZudBlXg66ED90nDfcCbpTfOhPD'),(8,'Patrick','Star','Pstar@gmail.com','Pstar','$5$rounds=535000$PI0L8BhWzgUoXyAt$7nDwH/lzlUDKeT1nLRNAbVsgQbeLoVrzWJr94vxaB12'),(9,'Spongebob','Squarepants','Ssquarepants@gmail.com','Ssquarepants','$5$rounds=535000$9DJjvgMVala0qoEp$iEOSx9SAbE1DlGUxqcIz2xZMHYL6CvSsw2g40JeYYPC');
/*!40000 ALTER TABLE `parent` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-20 11:02:00
