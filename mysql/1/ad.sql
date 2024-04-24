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
INSERT INTO `auth_user` VALUES (1,'ssheng','','','822657545@qq.com','pbkdf2_sha256$10000$lpzPH9ZW3f1M$CdD3BFsegE990FtUpwiHr6eSG2WD3OSVqOxEhvyJHbk=',1,1,1,'2015-08-31 11:23:19','2015-08-16 02:30:59');
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
) ENGINE=MyISAM AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cfd_case`
--

LOCK TABLES `cfd_case` WRITE;
/*!40000 ALTER TABLE `cfd_case` DISABLE KEYS */;
INSERT INTO `cfd_case` VALUES (1,'stq','T','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(2,'dun','T','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(3,'Ames_All_Body13','L','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(4,'Blunt_Cone14','L','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(5,'Compression_Corner24_6','T','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(6,'Cone_Cylinder_Flare7','T','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(7,'Corner_Flow4','L','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(8,'D1_Shu_Osher1','L','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(9,'D2_Circular_Cylinder27','L','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(10,'D2_Double_Ellipsoid_heat31','L','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(11,'Double_Blunt_Cone15','L','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(12,'Double_Cone12','L','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(13,'Double_Ellipsoid11','L','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(14,'Double_Mach_Reflection3','L','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(15,'Folding_Wedge19','T','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(16,'Forward_Facing_Step2','L','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(17,'HBS26','T','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(18,'Hypersonic_Inlet16','T','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(19,'Sharp_Flared_Cone_Model23','T','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(20,'Single_Wedge20','T','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(21,'SupExpCompression_Corner5','T','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(22,'Type_4_Shock_Wave_Interaction22','L','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(23,'Wing_Pylon_Finned_Store30','U','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(24,'Wing_Pylon_Finned_Store_zidan29','U','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat');
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
) ENGINE=MyISAM AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cfd_sts`
--

LOCK TABLES `cfd_sts` WRITE;
/*!40000 ALTER TABLE `cfd_sts` DISABLE KEYS */;
INSERT INTO `cfd_sts` VALUES (1,1,'stq',12,0.001,1,1,1,0.5,0,158,3,1,1,2,-1,7.8,0,0,300,2174.5,0.101744,74.42,1.4,0.72,0.9,0,90000,0.75,100,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(2,2,'dun',12,0.001,1,1,1,0.5,0,158,3,3,1,2,-1,7.8,0,0,300,2174.5,0.101744,74.42,1.4,0.72,0.9,0,90000,0.75,100,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(3,3,'Ames_All_Body13',12,0.001,1,1,1,0.5,0,158,1,3,1,2,-1,7.4,0,0,300,945,0.0531,62,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(4,4,'Blunt_Cone14',12,0.001,1,1,1,0.5,0,158,1,3,1,2,-1,10.6,0,0,294.44,110,0.0081,47.3,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(5,5,'Compression_Corner24_6',12,0.001,1,1,1,0.5,0,158,1,3,1,2,-1,2.84,0,0,300,23921.66,0.8313,100.2633,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(6,6,'Cone_Cylinder_Flare7',12,0.001,1,1,1,0.5,0,158,1,3,1,2,-1,7.05,0,0,311,576,0.0252,81.2,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(7,7,'Corner_Flow4',12,0.001,1,1,1,0.5,0,158,1,3,1,2,-1,3,0,0,300,101325,1.1768,300,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,2,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(8,8,'D1_Shu_Osher1',12,0.001,1,1,1,0.5,0,158,1,3,1,5,-1,3,0,0,300,101325,1.229,288.15,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,2,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(9,9,'D2_Circular_Cylinder27',12,0.001,1,1,1,0.5,0,158,3,3,1,2,-1,0.1,0,0,300,9.5,8.51e-05,389,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(10,10,'D2_Double_Ellipsoid_heat31',12,0.001,1,1,1,0.5,0,158,3,3,1,2,-1,7.8,0,0,296,2172.6,0.10173,74.41,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(11,11,'Double_Blunt_Cone15',12,0.001,1,1,1,0.5,0,158,1,3,1,2,-1,3,0,0,300,101325,1.229,288.15,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(12,12,'Double_Cone12',12,0.001,1,1,1,0.5,0,158,1,3,1,2,-1,12.49,0,0,296.1,18.55,0.000632,102.22,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(13,13,'Double_Ellipsoid11',12,0.001,1,1,1,0.5,0,158,1,3,1,2,-1,7.79,0,0,300,11027.89,0.2611,147.1457,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(14,14,'Double_Mach_Reflection3',12,0.001,1,1,1,0.5,0,158,1,3,1,2,-1,3,0,0,300,101325,1.229,288.15,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(15,15,'Folding_Wedge19',12,0.001,1,1,1,0.5,0,158,1,3,1,2,-1,4.9,0,0,300,101325,1.229,288.15,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(16,16,'Forward_Facing_Step2',12,0.001,1,1,1,0.5,0,158,1,3,1,2,-1,3,0,0,300,1,1.4,0.00249,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(17,17,'HBS26',12,0.001,1,1,1,0.5,0,158,3,3,1,2,-1,6.85,0,0,300,461.51,0.00555,290,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,1,1e-05,10000,99999999,0.75,30,0.01,20,0,10000000),(18,18,'Hypersonic_Inlet16',12,0.001,1,1,1,0.5,0,158,5,3,1,2,-1,7,0,0,300,169.1,0.0127,46.3,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(19,19,'Sharp_Flared_Cone_Model23',12,0.001,1,1,1,0.5,0,158,3,3,1,2,-1,5.91,0,0,300,1190,0.0496,83.63,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(20,20,'Single_Wedge20',12,0.001,1,1,1,0.5,0,158,4,3,1,2,-1,3.98,0,0,300,12000,0.523,80,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(21,21,'SupExpCompression_Corner5',12,0.001,1,1,1,0.5,0,158,3,3,1,2,-1,2.9,0,0,300,101325,0.7675,460,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(22,22,'Type_4_Shock_Wave_Interaction22',12,0.001,1,1,1,0.5,0,158,1,3,1,2,-1,8.03,0,0,122.11,101325,1.229,288.15,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(23,23,'Wing_Pylon_Finned_Store30',12,0.001,1,1,1,0.5,0,158,3,3,1,2,-1,7.8,0,0,296,2172.6,0.10173,74.41,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(24,24,'Wing_Pylon_Finned_Store_zidan29',12,0.001,1,1,1,0.5,0,158,3,3,1,2,-1,3,0,0,300,101325,1.229,288.15,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000);
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
) ENGINE=MyISAM AUTO_INCREMENT=65 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2015-08-16 02:37:09',1,9,'1','stq',1,''),(2,'2015-08-16 02:37:18',1,9,'2','dun',1,''),(3,'2015-08-16 02:39:22',1,10,'1','stq',1,''),(4,'2015-08-16 02:39:46',1,10,'2','dun',1,''),(5,'2015-08-19 03:39:35',1,10,'2','dun',2,'Changed TimeScheme.'),(6,'2015-08-19 08:54:22',1,10,'2','dun',2,'Changed TimeScheme.'),(7,'2015-08-20 09:20:03',1,10,'1','stq',2,'Changed IterationNum and IOUT.'),(8,'2015-08-20 09:20:28',1,10,'2','dun',2,'Changed IterationNum and IOUT.'),(9,'2015-08-22 07:28:40',1,10,'1','stq',2,'Changed IOUT.'),(10,'2015-08-22 07:28:52',1,10,'2','dun',2,'Changed IOUT.'),(11,'2015-08-23 08:32:42',1,10,'1','stq',2,'Changed NCPUs.'),(12,'2015-08-23 08:32:51',1,10,'2','dun',2,'Changed NCPUs.'),(13,'2015-08-23 08:50:21',1,10,'1','stq',2,'Changed NCPUs.'),(14,'2015-08-23 08:52:06',1,10,'2','dun',2,'No fields changed.'),(15,'2015-08-23 08:52:14',1,10,'1','stq',2,'No fields changed.'),(16,'2015-08-24 02:01:28',1,10,'2','dun',2,'Changed NCPUs.'),(17,'2015-08-28 07:21:36',1,10,'2','dun',2,'Changed TimeScheme.'),(18,'2015-08-28 12:59:00',1,10,'2','dun',2,'Changed TimeScheme.'),(19,'2015-09-02 00:00:39',1,9,'3','Ames_All_Body13',1,''),(20,'2015-09-02 00:00:42',1,9,'3','Ames_All_Body13',2,'No fields changed.'),(21,'2015-09-02 00:02:30',1,9,'4','Blunt_Cone14',1,''),(22,'2015-09-02 00:04:38',1,9,'5','Compression_Corner24_6',1,''),(23,'2015-09-02 00:05:21',1,9,'6','Cone_Cylinder_Flare7',1,''),(24,'2015-09-02 00:06:25',1,9,'7','Corner_Flow4',1,''),(25,'2015-09-02 00:07:45',1,9,'8','D1_Shu_Osher1',1,''),(26,'2015-09-02 00:08:57',1,9,'9','D2_Circular_Cylinder27',1,''),(27,'2015-09-02 00:10:16',1,9,'10','D2_Double_Ellipsoid_heat31',1,''),(28,'2015-09-02 00:11:05',1,9,'11','Double_Blunt_Cone15',1,''),(29,'2015-09-02 00:12:11',1,9,'12','Double_Cone12',1,''),(30,'2015-09-02 00:13:01',1,9,'13','Double_Ellipsoid11',1,''),(31,'2015-09-02 00:13:44',1,9,'14','Double_Mach_Reflection3',1,''),(32,'2015-09-02 00:14:16',1,9,'15','Folding_Wedge19',1,''),(33,'2015-09-02 00:14:53',1,9,'16','Forward_Facing_Step2',1,''),(34,'2015-09-02 00:16:04',1,9,'17','HBS26',1,''),(35,'2015-09-02 00:17:21',1,9,'18','Hypersonic_Inlet16',1,''),(36,'2015-09-02 00:17:53',1,9,'19','Sharp_Flared_Cone_Model23',1,''),(37,'2015-09-02 00:18:40',1,9,'20','Single_Wedge20',1,''),(38,'2015-09-02 00:20:04',1,9,'21','SupExpCompression_Corner5',1,''),(39,'2015-09-02 00:20:48',1,9,'22','Type_4_Shock_Wave_Interaction22',1,''),(40,'2015-09-02 00:21:27',1,9,'23','Wing_Pylon_Finned_Store30',1,''),(41,'2015-09-02 00:22:00',1,9,'24','Wing_Pylon_Finned_Store_zidan29',1,''),(42,'2015-09-02 00:28:18',1,10,'2','dun',2,'No fields changed.'),(43,'2015-09-02 00:42:56',1,10,'3','Ames_All_Body13',1,''),(44,'2015-09-02 00:59:07',1,10,'4','Blunt_Cone14',1,''),(45,'2015-09-02 01:01:38',1,10,'5','Compression_Corner24_6',1,''),(46,'2015-09-02 01:04:01',1,10,'6','Cone_Cylinder_Flare7',1,''),(47,'2015-09-02 01:07:46',1,10,'7','Corner_Flow4',1,''),(48,'2015-09-02 01:21:17',1,10,'8','D1_Shu_Osher1',1,''),(49,'2015-09-02 01:24:47',1,10,'9','D2_Circular_Cylinder27',1,''),(50,'2015-09-02 01:27:13',1,10,'10','D2_Double_Ellipsoid_heat31',1,''),(51,'2015-09-02 01:30:45',1,10,'11','Double_Blunt_Cone15',1,''),(52,'2015-09-02 01:34:43',1,10,'12','Double_Cone12',1,''),(53,'2015-09-02 01:37:26',1,10,'13','Double_Ellipsoid11',1,''),(54,'2015-09-02 01:40:36',1,10,'14','Double_Mach_Reflection3',1,''),(55,'2015-09-02 01:48:28',1,10,'15','Folding_Wedge19',1,''),(56,'2015-09-02 01:51:24',1,10,'16','Forward_Facing_Step2',1,''),(57,'2015-09-02 01:57:00',1,10,'17','HBS26',1,''),(58,'2015-09-02 02:00:02',1,10,'18','Hypersonic_Inlet16',1,''),(59,'2015-09-02 02:04:21',1,10,'19','Sharp_Flared_Cone_Model23',1,''),(60,'2015-09-02 02:06:50',1,10,'20','Single_Wedge20',1,''),(61,'2015-09-02 02:09:13',1,10,'21','SupExpCompression_Corner5',1,''),(62,'2015-09-02 02:13:16',1,10,'22','Type_4_Shock_Wave_Interaction22',1,''),(63,'2015-09-02 02:17:20',1,10,'23','Wing_Pylon_Finned_Store30',1,''),(64,'2015-09-02 02:20:38',1,10,'24','Wing_Pylon_Finned_Store_zidan29',1,'');
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
INSERT INTO `django_session` VALUES ('b8899e1df70501538a68b6c3dbbb0eb6','NzViMzM0NDRiODgwZmU3M2Q1NmIwMTZkMGM4YzRhNjMzYmNlYmJkYjqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2015-08-30 02:32:16'),('3f123984f7f47a5964717bfe0fece69f','NzViMzM0NDRiODgwZmU3M2Q1NmIwMTZkMGM4YzRhNjMzYmNlYmJkYjqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2015-09-14 11:23:19');
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

-- Dump completed on 2015-09-02 14:42:27
