-- MySQL dump 10.13  Distrib 5.7.12, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: od_appconf
-- ------------------------------------------------------
-- Server version	5.7.16-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `rediscfg`
--

DROP TABLE IF EXISTS `rediscfg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rediscfg` (
  `Redis_Id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键标志，自增列',
  `DomainName` varchar(45) DEFAULT NULL COMMENT '域名',
  `IPAddress` varchar(45) DEFAULT NULL COMMENT 'IP地址',
  `Username` varchar(45) DEFAULT NULL COMMENT '账号',
  `Password` varchar(100) DEFAULT NULL COMMENT '登录密码--备用',
  `Note` varchar(45) DEFAULT NULL COMMENT '备注',
  `Used` bit(1) DEFAULT b'0' COMMENT '是否已启用',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`Redis_Id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COMMENT='redis 配置主表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rediscfg`
--

LOCK TABLES `rediscfg` WRITE;
/*!40000 ALTER TABLE `rediscfg` DISABLE KEYS */;
INSERT INTO `rediscfg` VALUES (1,'Center','172.16.18.1','admin',NULL,'Admin','\0','2018-02-11 14:24:52','2018-02-11 14:24:52'),(2,'Center','172.16.18.1','Admin',NULL,'admin','\0','2018-02-11 14:26:06','2018-02-11 15:13:19'),(3,NULL,NULL,NULL,NULL,NULL,'\0','2018-02-11 14:29:00','2018-02-11 14:29:00'),(4,NULL,NULL,NULL,NULL,NULL,'\0','2018-02-11 14:50:46','2018-02-11 14:50:46'),(5,NULL,NULL,NULL,NULL,NULL,'\0','2018-02-11 14:52:00','2018-02-11 14:52:00'),(6,NULL,NULL,NULL,NULL,NULL,'\0','2018-02-11 14:53:00','2018-02-11 14:53:00');
/*!40000 ALTER TABLE `rediscfg` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-03-16 16:12:15
