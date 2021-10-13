-- MySQL dump 10.13  Distrib 8.0.26, for Linux (x86_64)
--
-- Host: localhost    Database: HelpDesk
-- ------------------------------------------------------
-- Server version	8.0.26-0ubuntu0.20.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `agent__tickets__summary`
--

DROP TABLE IF EXISTS `agent__tickets__summary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `agent__tickets__summary` (
  `id` int NOT NULL AUTO_INCREMENT,
  `All_tickets` int DEFAULT NULL,
  `Pendings` int DEFAULT NULL,
  `Solved` int DEFAULT NULL,
  `User_id` int DEFAULT NULL,
  `DateTime` datetime DEFAULT NULL,
  `UpdateTime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `User_id` (`User_id`),
  CONSTRAINT `agent__tickets__summary_ibfk_1` FOREIGN KEY (`User_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `agent__tickets__summary`
--

LOCK TABLES `agent__tickets__summary` WRITE;
/*!40000 ALTER TABLE `agent__tickets__summary` DISABLE KEYS */;
/*!40000 ALTER TABLE `agent__tickets__summary` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reviews` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Text` varchar(1000) DEFAULT NULL,
  `Ticket_id` int DEFAULT NULL,
  `DateTime` datetime DEFAULT NULL,
  `UpdateTime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Ticket_id` (`Ticket_id`),
  CONSTRAINT `reviews_ibfk_1` FOREIGN KEY (`Ticket_id`) REFERENCES `tickets` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tickets`
--

DROP TABLE IF EXISTS `tickets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tickets` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Agent_ID` varchar(15) DEFAULT NULL,
  `User_ID` varchar(15) DEFAULT NULL,
  `Subject` varchar(100) DEFAULT NULL,
  `Description` varchar(1000) DEFAULT NULL,
  `Problem_Type` varchar(100) DEFAULT NULL,
  `Company_Area` varchar(45) DEFAULT NULL,
  `Service_Score` int DEFAULT NULL,
  `Status` int DEFAULT NULL,
  `DateTime` datetime DEFAULT NULL,
  `UpdateTime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tickets`
--

LOCK TABLES `tickets` WRITE;
/*!40000 ALTER TABLE `tickets` DISABLE KEYS */;
INSERT INTO `tickets` VALUES (1,NULL,'2','testing','we123','Hardware','Recursos Humanos',NULL,NULL,'2021-10-13 05:20:35','2021-10-13 05:20:35'),(2,NULL,'2','testing','we123','Hardware','Recursos Humanos',NULL,NULL,'2021-10-13 05:38:08','2021-10-13 05:38:08'),(3,NULL,'2','testing','we123','Hardware','Recursos Humanos',NULL,NULL,'2021-10-13 05:38:59','2021-10-13 05:38:59'),(4,NULL,'2','testing','we123','Hardware','Recursos Humanos',NULL,NULL,'2021-10-13 05:40:46','2021-10-13 05:40:46'),(5,NULL,'2','testing','we123','Hardware','Recursos Humanos',NULL,NULL,'2021-10-13 05:41:39','2021-10-13 05:41:39'),(6,NULL,'2','testing','we123','Hardware','Recursos Humanos',NULL,NULL,'2021-10-13 05:41:41','2021-10-13 05:41:41'),(7,NULL,'2','testing','we123','Hardware','Recursos Humanos',NULL,NULL,'2021-10-13 05:42:56','2021-10-13 05:42:56'),(8,NULL,'2','testing','we123','Hardware','Recursos Humanos',NULL,NULL,'2021-10-13 05:49:40','2021-10-13 05:49:40'),(9,NULL,'2','testing','we123','Hardware','Recursos Humanos',NULL,NULL,'2021-10-13 05:51:42','2021-10-13 05:51:42'),(10,NULL,'2','testing','we123','Hardware','Recursos Humanos',NULL,NULL,'2021-10-13 05:51:42','2021-10-13 05:51:42'),(11,NULL,'2','testing','we123','Hardware','Recursos Humanos',NULL,NULL,'2021-10-13 05:52:00','2021-10-13 05:52:00'),(12,NULL,'2','testing','we123','Hardware','Recursos Humanos',NULL,NULL,'2021-10-13 06:00:35','2021-10-13 06:00:35'),(13,NULL,'2','testing','we123','Hardware','Recursos Humanos',NULL,NULL,'2021-10-13 06:01:13','2021-10-13 06:01:13'),(14,NULL,'2','testing','we123','Hardware','Recursos Humanos',NULL,NULL,'2021-10-13 06:01:45','2021-10-13 06:01:45'),(15,NULL,'2','testing','we123','Hardware','Recursos Humanos',NULL,NULL,'2021-10-13 06:10:12','2021-10-13 06:10:12'),(16,NULL,'2','testing','we123','Hardware','Recursos Humanos',NULL,NULL,'2021-10-13 06:11:22','2021-10-13 06:11:22'),(17,NULL,'2','testing','we123','Hardware','Recursos Humanos',NULL,NULL,'2021-10-13 06:16:25','2021-10-13 06:16:25'),(18,NULL,'2','testing','we123','Hardware','Recursos Humanos',NULL,NULL,'2021-10-13 08:58:28','2021-10-13 08:58:28'),(19,NULL,'2','testing','asawe','Software','Recursos Humanos',NULL,NULL,'2021-10-13 09:02:10','2021-10-13 09:02:10'),(20,NULL,'3','testing','123123','Hardware','Recursos Humanos',NULL,NULL,'2021-10-13 14:21:05','2021-10-13 14:21:05');
/*!40000 ALTER TABLE `tickets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tickets__summary`
--

DROP TABLE IF EXISTS `tickets__summary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tickets__summary` (
  `id` int NOT NULL AUTO_INCREMENT,
  `All_tickets` int DEFAULT NULL,
  `Pendings` int DEFAULT NULL,
  `Assigned` int DEFAULT NULL,
  `Solved` int DEFAULT NULL,
  `DateTime` datetime DEFAULT NULL,
  `UpdateTime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tickets__summary`
--

LOCK TABLES `tickets__summary` WRITE;
/*!40000 ALTER TABLE `tickets__summary` DISABLE KEYS */;
INSERT INTO `tickets__summary` VALUES (1,13,13,0,0,'2021-10-13 05:20:35','2021-10-13 09:21:05'),(2,0,0,0,0,'2021-10-13 05:38:08','2021-10-13 05:38:08'),(3,0,0,0,0,'2021-10-13 05:38:59','2021-10-13 05:38:59');
/*!40000 ALTER TABLE `tickets__summary` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user__tickets__summary`
--

DROP TABLE IF EXISTS `user__tickets__summary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user__tickets__summary` (
  `id` int NOT NULL AUTO_INCREMENT,
  `All_tickets` int DEFAULT NULL,
  `Pendings` int DEFAULT NULL,
  `Assigned` int DEFAULT NULL,
  `Solved` int DEFAULT NULL,
  `User_id` int DEFAULT NULL,
  `DateTime` datetime DEFAULT NULL,
  `UpdateTime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `User_id` (`User_id`),
  CONSTRAINT `user__tickets__summary_ibfk_1` FOREIGN KEY (`User_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user__tickets__summary`
--

LOCK TABLES `user__tickets__summary` WRITE;
/*!40000 ALTER TABLE `user__tickets__summary` DISABLE KEYS */;
INSERT INTO `user__tickets__summary` VALUES (1,16,16,0,0,2,'2021-10-13 05:20:35','2021-10-13 04:02:10'),(2,1,1,0,0,3,'2021-10-13 14:21:05','2021-10-13 14:21:05');
/*!40000 ALTER TABLE `user__tickets__summary` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Username` varchar(15) DEFAULT NULL,
  `Nombre` varchar(30) DEFAULT NULL,
  `Apellido` varchar(30) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `Password` varchar(300) DEFAULT NULL,
  `Admin` varchar(20) DEFAULT NULL,
  `Confirmed_mail` varchar(10) DEFAULT NULL,
  `User_id` varchar(15) DEFAULT NULL,
  `DateTime` datetime NOT NULL,
  `UpdateTime` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Username` (`Username`),
  UNIQUE KEY `Email` (`Email`),
  UNIQUE KEY `User_id` (`User_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Admin','Admin','Admin','tmrfack@gmail.com','sha256$niL5I2NzBgAWp6Xn$ee2c6c2430317ceb5e159f24b70a961d638036234ef446a47e8ea42f744816fa','yes','yes','123','2021-10-13 05:17:20','2021-10-13 05:17:20'),(2,'user','user','user','mameco4541@specialistblog.com','sha256$mXcZE0tF7n3N08It$0fdfb9d399e6280edd8b845c2d16ea100c8bc655cc5271c250776ddd86b47228','nop','yes','444','2021-10-13 05:20:14','2021-10-13 05:20:14'),(3,'user2','user2','user2','jibome3847@specialistblog.com','sha256$1RKLrfHjWC5ZG4wB$1cab8836cebc052f177d7e4506d76a2ea9f661ad6587490dae2650f0b9c04bc6','nop','yes','333','2021-10-13 14:20:23','2021-10-13 14:20:23');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `workers_ids`
--

DROP TABLE IF EXISTS `workers_ids`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `workers_ids` (
  `id` int NOT NULL AUTO_INCREMENT,
  `User_id` varchar(15) DEFAULT NULL,
  `Used` varchar(15) DEFAULT NULL,
  `Admin` varchar(15) DEFAULT NULL,
  `DateTime` datetime DEFAULT NULL,
  `UpdateTime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `User_id` (`User_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `workers_ids`
--

LOCK TABLES `workers_ids` WRITE;
/*!40000 ALTER TABLE `workers_ids` DISABLE KEYS */;
INSERT INTO `workers_ids` VALUES (1,'123','used','yes',NULL,NULL),(2,'444','used','nop','2021-10-13 05:19:27','2021-10-13 05:19:27'),(3,'333','used','nop','2021-10-13 14:19:10','2021-10-13 14:19:10');
/*!40000 ALTER TABLE `workers_ids` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-13 11:24:50
