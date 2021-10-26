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
  `id` varchar(60) NOT NULL,
  `All_tickets` int DEFAULT NULL,
  `Pendings` int DEFAULT NULL,
  `Assigned` int DEFAULT NULL,
  `Solved` int DEFAULT NULL,
  `User_id` varchar(60) DEFAULT NULL,
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
  `id` varchar(60) NOT NULL,
  `Text` varchar(1000) DEFAULT NULL,
  `Ticket_id` varchar(60) DEFAULT NULL,
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
  `id` varchar(60) NOT NULL,
  `Agent_ID` varchar(60) DEFAULT NULL,
  `User_ID` varchar(60) DEFAULT NULL,
  `Subject` varchar(100) DEFAULT NULL,
  `Description` varchar(1000) DEFAULT NULL,
  `Problem_Type` varchar(100) DEFAULT NULL,
  `Company_Area` varchar(45) DEFAULT NULL,
  `Service_Score` int DEFAULT NULL,
  `Status` int DEFAULT NULL,
  `DateTime` datetime DEFAULT NULL,
  `UpdateTime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tickets`
--


--
-- Table structure for table `tickets__summary`
--

DROP TABLE IF EXISTS `tickets__summary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tickets__summary` (
  `id` varchar(60) NOT NULL,
  `All_tickets` int DEFAULT NULL,
  `Pendings` int DEFAULT NULL,
  `Assigned` int DEFAULT NULL,
  `Solved` int DEFAULT NULL,
  `DateTime` datetime DEFAULT NULL,
  `UpdateTime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tickets__summary`
--



--
-- Table structure for table `chathistory`
--

DROP TABLE IF EXISTS `chathistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chathistory` (
  `id` varchar(60) NOT NULL,
  `Ticket_id` varchar(60) DEFAULT NULL,
  `Agent_ID` varchar(60) DEFAULT NULL,
  `User_ID` varchar(60) DEFAULT NULL,
  `message` text DEFAULT NULL,
  `DateTime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `time__access`
--

DROP TABLE IF EXISTS `time__access`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `time__access` (
  `id` varchar(60) NOT NULL,
  `User_id` varchar(60) DEFAULT NULL,
  `From` datetime NOT NULL,
  `To` datetime NOT NULL,
  `Last_activity` datetime NOT NULL,
  `Last_login` datetime NOT NULL,
  `DateTime` datetime NOT NULL,
  `UpdateTime` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `User_id` (`User_id`),
  CONSTRAINT `time__access_ibfk_1` FOREIGN KEY (`User_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `time__access`
--

LOCK TABLES `time__access` WRITE;
/*!40000 ALTER TABLE `time__access` DISABLE KEYS */;
INSERT INTO `time__access` VALUES ('45a77e20-f44f-413c-b6e6-943cc2b703a7','29729e77-05e1-4356-b48a-ae3ec4a44f47','2021-10-14 00:00:00','2022-12-31 00:00:00', '2021-10-14 20:59:16', '2021-10-14 20:59:16','2021-10-14 20:51:36','2021-10-14 20:51:36');
/*!40000 ALTER TABLE `time__access` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user__tickets__summary`
--

DROP TABLE IF EXISTS `user__tickets__summary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user__tickets__summary` (
  `id` varchar(60) NOT NULL,
  `All_tickets` int DEFAULT NULL,
  `Pendings` int DEFAULT NULL,
  `Assigned` int DEFAULT NULL,
  `Solved` int DEFAULT NULL,
  `User_id` varchar(60) DEFAULT NULL,
  `DateTime` datetime DEFAULT NULL,
  `UpdateTime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `User_id` (`User_id`),
  CONSTRAINT `user__tickets__summary_ibfk_1` FOREIGN KEY (`User_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user__tickets__summary`
--


--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` varchar(60) NOT NULL,
  `Username` varchar(30) DEFAULT NULL,
  `Nombre` varchar(30) DEFAULT NULL,
  `Apellido` varchar(30) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `Password` varchar(300) DEFAULT NULL,
  `Rol` varchar(20) DEFAULT NULL,
  `Area` varchar(30) DEFAULT NULL,
  `Estado` varchar(30) DEFAULT NULL,
  `User_id` varchar(60) DEFAULT NULL,
  `DateTime` datetime NOT NULL,
  `UpdateTime` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Username` (`Username`),
  UNIQUE KEY `Email` (`Email`),
  UNIQUE KEY `User_id` (`User_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('29729e77-05e1-4356-b48a-ae3ec4a44f47','Admin','Admin','Admin','tmrfack@gmail.com','sha256$7dvrKr3kKi7R3CTO$cf28d6a26fc2536e3bf23956f31803891ff212cd96327adf44012b9b06b26491','Administrador','Sistemas','Activo',NULL,'2021-10-14 20:51:36','2021-10-14 20:51:36');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `workers_ids`
--

DROP TABLE IF EXISTS `workers_ids`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `workers_ids` (
  `id` varchar(60) NOT NULL,
  `User_id` varchar(60) DEFAULT NULL,
  `Used` varchar(15) DEFAULT NULL,
  `Admin` varchar(15) DEFAULT NULL,
  `DateTime` datetime DEFAULT NULL,
  `UpdateTime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `User_id` (`User_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `workers_ids`
--

LOCK TABLES `workers_ids` WRITE;
/*!40000 ALTER TABLE `workers_ids` DISABLE KEYS */;
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

-- Dump completed on 2021-10-14 19:27:48
