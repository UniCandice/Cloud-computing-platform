-- MySQL dump 10.13  Distrib 5.1.66, for redhat-linux-gnu (x86_64)
--
-- Host: localhost    Database: fuck
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
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-08-27 10:12:27
