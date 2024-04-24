-- MySQL dump 10.13  Distrib 5.1.66, for redhat-linux-gnu (x86_64)
--
-- Host: localhost    Database: mydata
-- ------------------------------------------------------
-- Server version	5.1.66

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_bda51c3c` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_e4470c6e` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add site',6,'add_site'),(17,'Can change site',6,'change_site'),(18,'Can delete site',6,'delete_site'),(19,'Can add log entry',7,'add_logentry'),(20,'Can change log entry',7,'change_logentry'),(21,'Can delete log entry',7,'delete_logentry'),(22,'Can add solver',8,'add_solver'),(23,'Can change solver',8,'change_solver'),(24,'Can delete solver',8,'delete_solver'),(25,'Can add case',9,'add_case'),(26,'Can change case',9,'change_case'),(27,'Can delete case',9,'delete_case'),(28,'Can add sts',10,'add_sts'),(29,'Can change sts',10,'change_sts'),(30,'Can delete sts',10,'delete_sts');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'ssheng','','','822657545@qq.com','pbkdf2_sha256$10000$lpzPH9ZW3f1M$CdD3BFsegE990FtUpwiHr6eSG2WD3OSVqOxEhvyJHbk=',1,1,1,'2015-08-16 02:32:16','2015-08-16 02:30:59');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_fbfc09f1` (`user_id`),
  KEY `auth_user_groups_bda51c3c` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_fbfc09f1` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cfd_case`
--

DROP TABLE IF EXISTS `cfd_case`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cfd_case` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `character` varchar(20) NOT NULL,
  `cgns` varchar(50) NOT NULL,
  `bc` varchar(50) NOT NULL,
  `grd` varchar(50) NOT NULL,
  `inplot` varchar(50) NOT NULL,
  `cfd_result` varchar(50) NOT NULL,
  `experiment` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cfd_case`
--

LOCK TABLES `cfd_case` WRITE;
/*!40000 ALTER TABLE `cfd_case` DISABLE KEYS */;
INSERT INTO `cfd_case` VALUES (1,'stq','T','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(2,'dun','T','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat');
/*!40000 ALTER TABLE `cfd_case` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cfd_solver`
--

DROP TABLE IF EXISTS `cfd_solver`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cfd_solver` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `describe` longtext NOT NULL,
  `ststemplate` varchar(100) NOT NULL,
  `ch` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cfd_solver`
--

LOCK TABLES `cfd_solver` WRITE;
/*!40000 ALTER TABLE `cfd_solver` DISABLE KEYS */;
/*!40000 ALTER TABLE `cfd_solver` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cfd_sts`
--

DROP TABLE IF EXISTS `cfd_sts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cfd_sts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `case_id` int(11) NOT NULL,
  `TaskName` varchar(50) NOT NULL,
  `NCPUs` int(11) NOT NULL,
  `Nondimension_L` double NOT NULL,
  `GridType` int(11) NOT NULL,
  `SolverType` int(11) NOT NULL,
  `Initial_way` int(11) NOT NULL,
  `SG1` double NOT NULL,
  `SG2` int(11) NOT NULL,
  `SG3` int(11) NOT NULL,
  `FlowModel` int(11) NOT NULL,
  `TimeScheme` int(11) NOT NULL,
  `FluxScheme` int(11) NOT NULL,
  `Limiter` int(11) NOT NULL,
  `Height` double NOT NULL,
  `Mach` double NOT NULL,
  `Alpha` double NOT NULL,
  `Beta` double NOT NULL,
  `Twall` double NOT NULL,
  `ATM_Pressure` double NOT NULL,
  `ATM_Density` double NOT NULL,
  `ATM_Temperature` double NOT NULL,
  `Gamma` double NOT NULL,
  `Prandtl_Lam` double NOT NULL,
  `Prandtl_Turb` double NOT NULL,
  `IsRestart` int(11) NOT NULL,
  `IterationNum` int(11) NOT NULL,
  `CFL` double NOT NULL,
  `IOUT` int(11) NOT NULL,
  `ErrorTol` double NOT NULL,
  `InitialStepNum` int(11) NOT NULL,
  `Ref_Area` double NOT NULL,
  `Ref_Length` double NOT NULL,
  `Ref_X` double NOT NULL,
  `Ref_Y` double NOT NULL,
  `Ref_Z` double NOT NULL,
  `InvDiscretMethod` int(11) NOT NULL,
  `VisDiscretMethod` int(11) NOT NULL,
  `SG4` int(11) NOT NULL,
  `VisDirection` int(11) NOT NULL,
  `UnphysicsCorrect` int(11) NOT NULL,
  `TimeSizeMethod` int(11) NOT NULL,
  `RelaxFactor` double NOT NULL,
  `EntropyFix` int(11) NOT NULL,
  `EntropyFixD` double NOT NULL,
  `EntropyFixO` double NOT NULL,
  `JSTCoe2` double NOT NULL,
  `JSTCoe4` double NOT NULL,
  `CompressibilityCorrect` int(11) NOT NULL,
  `DES_Method` int(11) NOT NULL,
  `CDES` int(11) NOT NULL,
  `CDES_SST` int(11) NOT NULL,
  `Unsteady` int(11) NOT NULL,
  `TimeSize` double NOT NULL,
  `MaxTimeSteps` int(11) NOT NULL,
  `EndTime` double NOT NULL,
  `SubCFL` double NOT NULL,
  `SubStepNum` int(11) NOT NULL,
  `SubErrorTOL` double NOT NULL,
  `IPlot` int(11) NOT NULL,
  `QuasiSteadySteps` int(11) NOT NULL,
  `QuasiRestartSteps` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cfd_sts_72319564` (`case_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cfd_sts`
--

LOCK TABLES `cfd_sts` WRITE;
/*!40000 ALTER TABLE `cfd_sts` DISABLE KEYS */;
INSERT INTO `cfd_sts` VALUES (1,1,'stq',12,0.001,1,1,1,0.5,0,158,3,1,1,2,-1,7.8,0,0,300,2174.5,0.101744,74.42,1.4,0.72,0.9,0,90000,0.75,100,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(2,2,'dun',12,0.001,1,1,1,0.5,0,158,3,3,1,2,-1,7.8,0,0,300,2174.5,0.101744,74.42,1.4,0.72,0.9,0,90000,0.75,100,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000);
/*!40000 ALTER TABLE `cfd_sts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_fbfc09f1` (`user_id`),
  KEY `django_admin_log_e4470c6e` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2015-08-16 02:37:09',1,9,'1','stq',1,''),(2,'2015-08-16 02:37:18',1,9,'2','dun',1,''),(3,'2015-08-16 02:39:22',1,10,'1','stq',1,''),(4,'2015-08-16 02:39:46',1,10,'2','dun',1,''),(5,'2015-08-19 03:39:35',1,10,'2','dun',2,'Changed TimeScheme.'),(6,'2015-08-19 08:54:22',1,10,'2','dun',2,'Changed TimeScheme.'),(7,'2015-08-20 09:20:03',1,10,'1','stq',2,'Changed IterationNum and IOUT.'),(8,'2015-08-20 09:20:28',1,10,'2','dun',2,'Changed IterationNum and IOUT.'),(9,'2015-08-22 07:28:40',1,10,'1','stq',2,'Changed IOUT.'),(10,'2015-08-22 07:28:52',1,10,'2','dun',2,'Changed IOUT.'),(11,'2015-08-23 08:32:42',1,10,'1','stq',2,'Changed NCPUs.'),(12,'2015-08-23 08:32:51',1,10,'2','dun',2,'Changed NCPUs.'),(13,'2015-08-23 08:50:21',1,10,'1','stq',2,'Changed NCPUs.'),(14,'2015-08-23 08:52:06',1,10,'2','dun',2,'No fields changed.'),(15,'2015-08-23 08:52:14',1,10,'1','stq',2,'No fields changed.'),(16,'2015-08-24 02:01:28',1,10,'2','dun',2,'Changed NCPUs.');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'permission','auth','permission'),(2,'group','auth','group'),(3,'user','auth','user'),(4,'content type','contenttypes','contenttype'),(5,'session','sessions','session'),(6,'site','sites','site'),(7,'log entry','admin','logentry'),(8,'solver','cfd','solver'),(9,'case','cfd','case'),(10,'sts','cfd','sts');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_c25c2c28` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('b8899e1df70501538a68b6c3dbbb0eb6','NzViMzM0NDRiODgwZmU3M2Q1NmIwMTZkMGM4YzRhNjMzYmNlYmJkYjqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2015-08-30 02:32:16');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-08-27  9:58:02
