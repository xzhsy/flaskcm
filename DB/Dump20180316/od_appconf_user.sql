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
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `userId` varchar(36) NOT NULL COMMENT '序列号',
  `username` varchar(45) NOT NULL COMMENT '登录用户名',
  `email` varchar(45) DEFAULT NULL COMMENT '关联邮箱',
  `password` varchar(32) NOT NULL COMMENT '登录密码',
  `Note` varchar(45) DEFAULT NULL,
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `IsAdmin` int(1) NOT NULL DEFAULT '0' COMMENT '是否为管理员',
  `IsLogin` int(1) DEFAULT '0' COMMENT '是否已经登录',
  `Allowed` int(1) DEFAULT '0' COMMENT '等待管理员审核,是否允许登录',
  PRIMARY KEY (`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户数据表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('102f827a-221f-479d-8237-d3d23ec429a9','miao10','789456','456123',NULL,'2018-03-15 17:10:10','2018-03-15 17:10:10',0,0,0),('1ff879a8-0cb1-11e8-aa03-c03fd55c3733','miao','henu5972@163.com','123456','I have a dream','2018-02-08 17:19:12','2018-02-08 17:19:12',0,0,0),('21fa6342-0cb1-11e8-a814-c03fd55c3733','henu','henu5972@163.com','123456','I have a dream','2018-02-08 17:19:15','2018-02-08 17:19:15',0,0,0),('356db95c-6c11-48a2-b70e-bfc1d0f9a18a','miao11','13543564','123456',NULL,'2018-03-15 17:12:22','2018-03-15 17:12:22',0,0,0),('b0590ed5-8168-4c74-a974-481615323ad5','miao14','henu789','456123',NULL,'2018-03-15 17:14:57','2018-03-15 17:14:57',0,0,0),('b3ce070a-4e29-4f48-9931-b96ead00c00f','miao2','henu5972@163.com','123456',NULL,'2018-03-15 16:33:13','2018-03-15 16:33:13',0,0,0),('c4fa0523-88f0-496a-ad49-93947245cc3f','miao8','asdfasdfa','789456',NULL,'2018-03-15 17:08:06','2018-03-15 17:08:06',0,0,0),('daf58176-0d37-11e8-a1f7-f633955aa4c9','admin','henu5972@163.com','123456','I am Admin','2018-02-09 09:23:41','2018-02-09 16:13:01',1,0,0),('df7ab152-0d37-11e8-a300-f633955aa4c9','jzm','henu5972@163.com','123456','I am Admin','2018-02-09 09:23:46','2018-02-09 09:23:46',0,0,0),('e33e60c9-eaac-4227-9fb0-46f348c5ab3f','miao3','henu5972@163.com','123456',NULL,'2018-03-15 16:42:23','2018-03-15 16:42:23',0,0,0),('e36152fb-cb56-4242-9961-ea50ae6bdad2','miao9','asdfasdfa','789456',NULL,'2018-03-15 17:09:57','2018-03-15 17:09:57',0,0,0),('e3edddac-a8dd-4364-bfe2-e31c2a9c8451','miao7','henu5972@163.com','123456',NULL,'2018-03-15 17:06:12','2018-03-15 17:06:12',0,0,0),('ebdcac36-0cb0-11e8-a1d8-c03fd55c3733','mst','henu5972@163.com','123456','I have a dream','2018-02-08 17:17:48','2018-02-08 17:17:48',0,0,0);
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

-- Dump completed on 2018-03-16 16:12:15
