
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
) ENGINE=MyISAM AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cfd_case`
--

LOCK TABLES `cfd_case` WRITE;
/*!40000 ALTER TABLE `cfd_case` DISABLE KEYS */;
INSERT INTO `cfd_case` VALUES (1,'stq','T','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(2,'dun','T','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(3,'Ames_All_Body13','L','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(4,'Blunt_Cone14','L','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(5,'Compression_Corner24_6','T','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(6,'Cone_Cylinder_Flare7','T','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(7,'Corner_Flow4','L','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(8,'D1_Shu_Osher1','L','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(9,'D2_Circular_Cylinder27','L','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(10,'D2_Double_Ellipsoid_heat31','L','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(11,'Double_Blunt_Cone15','L','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(12,'Double_Cone12','L','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(13,'Double_Ellipsoid11','L','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(14,'Double_Mach_Reflection3','L','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(15,'Folding_Wedge19','T','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(16,'Forward_Facing_Step2','L','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(17,'HBS26','T','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(18,'Hypersonic_Inlet16','T','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(19,'Sharp_Flared_Cone_Model23','T','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(20,'Single_Wedge20','T','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(21,'SupExpCompression_Corner5','T','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(22,'Type_4_Shock_Wave_Interaction22','L','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(23,'Wing_Pylon_Finned_Store30','U','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(24,'Wing_Pylon_Finned_Store_zidan29','U','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(25,'DoubleCone','T','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat'),(26,'stq48','T','bhcfd.cgns','bhcfd.bc','bhcfd.grd','inplot.dat','result.dat','experiment.dat');
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
) ENGINE=MyISAM AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cfd_sts`
--

LOCK TABLES `cfd_sts` WRITE;
/*!40000 ALTER TABLE `cfd_sts` DISABLE KEYS */;
INSERT INTO `cfd_sts` VALUES (1,1,'stq',12,0.001,1,1,1,0.5,0,158,3,1,1,2,-1,7.8,0,0,300,2174.5,0.101744,74.42,1.4,0.72,0.9,0,90000,0.75,100,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(2,2,'dun',12,0.001,1,1,1,0.5,0,158,3,1,1,2,-1,7.8,0,0,300,2174.5,0.101744,74.42,1.4,0.72,0.9,0,90000,0.75,100,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(3,3,'Ames_All_Body13',12,0.001,1,1,1,0.5,0,158,1,3,1,2,-1,7.4,0,0,300,945,0.0531,62,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(4,4,'Blunt_Cone14',12,0.001,1,1,1,0.5,0,158,1,3,1,2,-1,10.6,0,0,294.44,110,0.0081,47.3,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(5,5,'Compression_Corner24_6',12,0.001,1,1,1,0.5,0,158,1,3,1,2,-1,2.84,0,0,300,23921.66,0.8313,100.2633,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(6,6,'Cone_Cylinder_Flare7',12,0.001,1,1,1,0.5,0,158,1,3,1,2,-1,7.05,0,0,311,576,0.0252,81.2,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(7,7,'Corner_Flow4',12,0.001,1,1,1,0.5,0,158,1,3,1,2,-1,3,0,0,300,101325,1.1768,300,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,2,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(8,8,'D1_Shu_Osher1',12,0.001,1,1,1,0.5,0,158,1,3,1,5,-1,3,0,0,300,101325,1.229,288.15,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,2,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(9,9,'D2_Circular_Cylinder27',12,0.001,1,1,1,0.5,0,158,3,3,1,2,-1,0.1,0,0,300,9.5,8.51e-05,389,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(10,10,'D2_Double_Ellipsoid_heat31',12,0.001,1,1,1,0.5,0,158,3,3,1,2,-1,7.8,0,0,296,2172.6,0.10173,74.41,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(11,11,'Double_Blunt_Cone15',12,0.001,1,1,1,0.5,0,158,1,3,1,2,-1,3,0,0,300,101325,1.229,288.15,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(12,12,'Double_Cone12',12,0.001,1,1,1,0.5,0,158,1,3,1,2,-1,12.49,0,0,296.1,18.55,0.000632,102.22,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(13,13,'Double_Ellipsoid11',12,0.001,1,1,1,0.5,0,158,1,3,1,2,-1,7.79,0,0,300,11027.89,0.2611,147.1457,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(14,14,'Double_Mach_Reflection3',12,0.001,1,1,1,0.5,0,158,1,3,1,2,-1,3,0,0,300,101325,1.229,288.15,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(15,15,'Folding_Wedge19',12,0.001,1,1,1,0.5,0,158,1,3,1,2,-1,4.9,0,0,300,101325,1.229,288.15,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(16,16,'Forward_Facing_Step2',12,0.001,1,1,1,0.5,0,158,1,3,1,2,-1,3,0,0,300,1,1.4,0.00249,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(17,17,'HBS26',12,0.001,1,1,1,0.5,0,158,3,3,1,2,-1,6.85,0,0,300,461.51,0.00555,290,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,1,1e-05,10000,99999999,0.75,30,0.01,20,0,10000000),(18,18,'Hypersonic_Inlet16',12,0.001,1,1,1,0.5,0,158,5,3,1,2,-1,7,0,0,300,169.1,0.0127,46.3,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(19,19,'Sharp_Flared_Cone_Model23',12,0.001,1,1,1,0.5,0,158,3,3,1,2,-1,5.91,0,0,300,1190,0.0496,83.63,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(20,20,'Single_Wedge20',12,0.001,1,1,1,0.5,0,158,4,3,1,2,-1,3.98,0,0,300,12000,0.523,80,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(21,21,'SupExpCompression_Corner5',12,0.001,1,1,1,0.5,0,158,3,3,1,2,-1,2.9,0,0,300,101325,0.7675,460,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(22,22,'Type_4_Shock_Wave_Interaction22',12,0.001,1,1,1,0.5,0,158,1,3,1,2,-1,8.03,0,0,122.11,101325,1.229,288.15,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(23,23,'Wing_Pylon_Finned_Store30',12,0.001,1,1,1,0.5,0,158,3,3,1,2,-1,7.8,0,0,296,2172.6,0.10173,74.41,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(24,24,'Wing_Pylon_Finned_Store_zidan29',12,0.001,1,1,1,0.5,0,158,3,3,1,2,-1,3,0,0,300,101325,1.229,288.15,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(25,25,'DoubleCone',37,0.001,1,1,1,0.5,0,158,3,1,1,2,-1,8,0,0,575,363.623,0.0221,57.246,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000);
/*!40000 ALTER TABLE `cfd_sts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cfd_sts19`
--

DROP TABLE IF EXISTS `cfd_sts19`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cfd_sts19` (
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
  KEY `cfd_sts19_72319564` (`case_id`)
) ENGINE=MyISAM AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cfd_sts19`
--

LOCK TABLES `cfd_sts19` WRITE;
/*!40000 ALTER TABLE `cfd_sts19` DISABLE KEYS */;
INSERT INTO `cfd_sts19` VALUES (1,1,'stq',12,0.001,1,1,1,0.5,0,158,3,3,1,2,-1,7.8,0,0,300,2174.5,0.101744,74.42,1.4,0.72,0.9,0,90000,0.75,100,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(2,2,'dun',12,0.001,1,1,1,0.5,0,158,3,3,1,2,-1,7.8,0,0,300,2174.5,0.101744,74.42,1.4,0.72,0.9,0,90000,0.75,100,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(3,3,'Ames_All_Body13',12,0.001,1,1,1,0.5,0,158,1,3,1,2,-1,7.4,0,0,300,945,0.0531,62,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(4,4,'Blunt_Cone14',12,0.001,1,1,1,0.5,0,158,1,3,1,2,-1,10.6,0,0,294.44,110,0.0081,47.3,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(5,5,'Compression_Corner24_6',12,0.001,1,1,1,0.5,0,158,1,3,1,2,-1,2.84,0,0,300,23921.66,0.8313,100.2633,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(6,6,'Cone_Cylinder_Flare7',12,0.001,1,1,1,0.5,0,158,1,3,1,2,-1,7.05,0,0,311,576,0.0252,81.2,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(7,7,'Corner_Flow4',12,0.001,1,1,1,0.5,0,158,1,3,1,2,-1,3,0,0,300,101325,1.1768,300,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,2,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(8,8,'D1_Shu_Osher1',12,0.001,1,1,1,0.5,0,158,1,3,1,5,-1,3,0,0,300,101325,1.229,288.15,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,2,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(9,9,'D2_Circular_Cylinder27',12,0.001,1,1,1,0.5,0,158,3,3,1,2,-1,0.1,0,0,300,9.5,8.51e-05,389,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(10,10,'D2_Double_Ellipsoid_heat31',12,0.001,1,1,1,0.5,0,158,3,3,1,2,-1,7.8,0,0,296,2172.6,0.10173,74.41,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(11,11,'Double_Blunt_Cone15',12,0.001,1,1,1,0.5,0,158,1,3,1,2,-1,3,0,0,300,101325,1.229,288.15,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(12,12,'Double_Cone12',12,0.001,1,1,1,0.5,0,158,1,3,1,2,-1,12.49,0,0,296.1,18.55,0.000632,102.22,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(13,13,'Double_Ellipsoid11',12,0.001,1,1,1,0.5,0,158,1,3,1,2,-1,7.79,0,0,300,11027.89,0.2611,147.1457,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(14,14,'Double_Mach_Reflection3',12,0.001,1,1,1,0.5,0,158,1,3,1,2,-1,3,0,0,300,101325,1.229,288.15,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(15,15,'Folding_Wedge19',12,0.001,1,1,1,0.5,0,158,1,3,1,2,-1,4.9,0,0,300,101325,1.229,288.15,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(16,16,'Forward_Facing_Step2',12,0.001,1,1,1,0.5,0,158,1,3,1,2,-1,3,0,0,300,1,1.4,0.00249,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(17,17,'HBS26',12,0.001,1,1,1,0.5,0,158,3,3,1,2,-1,6.85,0,0,300,461.51,0.00555,290,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,1,1e-05,10000,99999999,0.75,30,0.01,20,0,10000000),(18,18,'Hypersonic_Inlet16',12,0.001,1,1,1,0.5,0,158,5,3,1,2,-1,7,0,0,300,169.1,0.0127,46.3,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(19,19,'Sharp_Flared_Cone_Model23',12,0.001,1,1,1,0.5,0,158,3,3,1,2,-1,5.91,0,0,300,1190,0.0496,83.63,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(20,20,'Single_Wedge20',12,0.001,1,1,1,0.5,0,158,4,1,1,2,-1,3.98,0,0,300,12000,0.523,80,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(21,21,'SupExpCompression_Corner5',12,0.001,1,1,1,0.5,0,158,3,3,1,2,-1,2.9,0,0,300,101325,0.7675,460,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(22,22,'Type_4_Shock_Wave_Interaction22',12,0.001,1,1,1,0.5,0,158,1,3,1,2,-1,8.03,0,0,122.11,101325,1.229,288.15,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(23,23,'Wing_Pylon_Finned_Store30',12,0.001,1,1,1,0.5,0,158,3,3,1,2,-1,7.8,0,0,296,2172.6,0.10173,74.41,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(24,24,'Wing_Pylon_Finned_Store_zidan29',12,0.001,1,1,1,0.5,0,158,3,3,1,2,-1,3,0,0,300,101325,1.229,288.15,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000),(25,25,'DoubleCone',12,0.001,1,1,1,0.5,0,158,1,3,1,2,-1,8,0,0,575,363.623,0.0221,57.246,1.4,0.72,0.9,0,100000,0.75,400,1e-08,400,1,1,0,0,0,0,0,3,3,2,3,1.05,2,0.3,0.45,0,0,0,0,0,0,0,0,2000,4,2.5,30,0.01,20,0,1000000);
/*!40000 ALTER TABLE `cfd_sts19` ENABLE KEYS */;
UNLOCK TABLES;


