-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 08, 2025 at 09:04 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dmrp2`
--

DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `createNation` (IN `p_nationName` VARCHAR(100), IN `p_nationCapital` VARCHAR(100), IN `p_nationDesc` TEXT, IN `p_population` BIGINT, IN `p_gdp` DOUBLE, IN `p_popGrowth` DECIMAL(5,2), IN `p_gdpGrowth` DECIMAL(5,2))   BEGIN
    DECLARE latestYear INT;
    DECLARE newNationID INT;

   
    SELECT MAX(year) INTO latestYear FROM nationstats;

   
    IF latestYear IS NULL THEN
        SET latestYear = 2150;
    END IF;

    
    INSERT INTO nation (nationName, nationCapital, nationDesc)
    VALUES (p_nationName, p_nationCapital, p_nationDesc);

    SET newNationID = LAST_INSERT_ID();

   
    INSERT INTO nationstats (nationID, year, population, gdp, gdppercapita)
    VALUES (
        newNationID,
        latestYear,
        p_population,
        p_gdp,
        p_gdp / p_population
    );


    INSERT INTO nationgrowth (nationID, popgrowth, gdpgrowth)
    VALUES (newNationID, p_popGrowth, p_gdpGrowth);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `updateGrowth` (IN `Ingdpgrowth` DECIMAL(5,2), IN `Inpopgrowth` DECIMAL(5,2), IN `InnationID` INT)   UPDATE nationgrowth ng
SET 
    ng.gdpgrowth = inGdpGrowth,
    ng.popgrowth = inPopGrowth
WHERE ng.nationID = inNationID$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `updateNations` ()   BEGIN
 
    DECLARE latestYear INT;
    DECLARE nextYear INT;

  
    SELECT MAX(year) INTO latestYear FROM nationstats;
    SET nextYear = latestYear + 1;

 
    INSERT INTO nationstats (
        nationID, year, gdp, gdppercapita, population
    )
    SELECT
        ns.nationID,
        nextYear,
        ROUND(gdp * (1 + ng.gdpgrowth / 100)),
        ROUND(gdp * (1 + ng.gdpgrowth / 100) / ROUND(population * (1 + ng.popgrowth / 100))),
        ROUND(population * (1 + ng.popgrowth / 100))
    FROM nationstats ns
    join nationgrowth ng ON ns.nationID = ng.nationID
    WHERE year = latestYear;
    
    CALL updateProjects(nextYear);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `updateProjects` (IN `newYear` INT)   update projects 
set projects.complete=1
WHERE projects.completionDate<=newYear$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Stand-in structure for view `atprojects`
-- (See below for the actual view)
--
CREATE TABLE `atprojects` (
`projectName` tinytext
,`projectDesc` mediumtext
,`completionDate` int(11)
,`secrecy` enum('SECRET','CLASSIFIED','PUBLIC')
,`link` text
);

-- --------------------------------------------------------

--
-- Table structure for table `facilities`
--

CREATE TABLE `facilities` (
  `facilityID` int(11) NOT NULL,
  `locationID` int(11) NOT NULL,
  `facilityName` tinytext NOT NULL,
  `facilityDesc` mediumtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `locations`
--

CREATE TABLE `locations` (
  `locationID` int(11) NOT NULL,
  `subsectorID` int(11) NOT NULL,
  `ownerID` int(11) DEFAULT NULL,
  `locationName` tinytext NOT NULL,
  `locationDesc` mediumtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `nation`
--

CREATE TABLE `nation` (
  `nationID` int(11) NOT NULL,
  `nationName` varchar(50) NOT NULL,
  `nationCapital` varchar(50) NOT NULL,
  `nationDesc` longtext DEFAULT NULL COMMENT 'Optional Lore Description'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `nation`
--

INSERT INTO `nation` (`nationID`, `nationName`, `nationCapital`, `nationDesc`) VALUES
(1, 'Utopia Corporation', 'Berlin', 'One of the two greatest superpowers in the entire history of humanity, the Utopia Corporation rules from its seat in Europe all the way to Southern China and Brazil.\r\nUC has forged a paradoxical order built on cold compassion, ruling with an iron fist wrapped in a velvet glove for what they consider the protection of some abstraction of humanity.\r\n\r\nThe Utopia Corporation is a cold, and sometimes cruel state machine that will drag all of its citizens into a bright new future... whether they want it or not'),
(2, 'Atomantia', 'Bhutan', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `nationgrowth`
--

CREATE TABLE `nationgrowth` (
  `nationID` int(11) NOT NULL,
  `popgrowth` decimal(5,2) NOT NULL,
  `gdpgrowth` decimal(5,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `nationgrowth`
--

INSERT INTO `nationgrowth` (`nationID`, `popgrowth`, `gdpgrowth`) VALUES
(1, 4.50, 10.00),
(2, 1.13, 3.00);

-- --------------------------------------------------------

--
-- Table structure for table `nationpolicies`
--

CREATE TABLE `nationpolicies` (
  `nationID` int(11) NOT NULL,
  `PolicyID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `nationprojects`
--

CREATE TABLE `nationprojects` (
  `nationID` int(11) NOT NULL,
  `projectID` int(11) NOT NULL,
  `ownership` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `nationprojects`
--

INSERT INTO `nationprojects` (`nationID`, `projectID`, `ownership`) VALUES
(1, 1, 1),
(2, 2, 1),
(1, 3, 1),
(2, 3, 0);

-- --------------------------------------------------------

--
-- Table structure for table `nationsectors`
--

CREATE TABLE `nationsectors` (
  `nationID` int(11) NOT NULL,
  `sectorID` int(11) NOT NULL,
  `ownershipPercentage` float DEFAULT NULL,
  `ownershipType` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `nationstats`
--

CREATE TABLE `nationstats` (
  `nationID` int(11) NOT NULL,
  `year` int(11) NOT NULL,
  `gdp` double NOT NULL,
  `gdppercapita` float NOT NULL,
  `population` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `nationstats`
--

INSERT INTO `nationstats` (`nationID`, `year`, `gdp`, `gdppercapita`, `population`) VALUES
(1, 2154, 3.82398764747014e15, 1150060, 3325046591),
(2, 2154, 3.3646764874028e15, 650846, 5169699482);

-- --------------------------------------------------------

--
-- Table structure for table `nationsubsectors`
--

CREATE TABLE `nationsubsectors` (
  `nationID` int(11) NOT NULL,
  `subsectorID` int(11) NOT NULL,
  `ownershipPercentage` float DEFAULT NULL,
  `ownershipType` tinytext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `planets`
--

CREATE TABLE `planets` (
  `planetID` int(11) NOT NULL,
  `PlanetName` tinytext NOT NULL,
  `planetDesc` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `planets`
--

INSERT INTO `planets` (`planetID`, `PlanetName`, `planetDesc`) VALUES
(1, 'Earth', 'The original homeworld of humanity, and one of two planets known to harbour life');

-- --------------------------------------------------------

--
-- Table structure for table `policies`
--

CREATE TABLE `policies` (
  `policyID` int(11) NOT NULL,
  `policyCategory` int(11) NOT NULL,
  `policyName` tinytext NOT NULL,
  `policyStatus` tinytext NOT NULL,
  `policyDesc` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `policycategories`
--

CREATE TABLE `policycategories` (
  `categoryID` int(11) NOT NULL,
  `categoryName` varchar(50) NOT NULL,
  `categoryDesc` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `projects`
--

CREATE TABLE `projects` (
  `projectID` int(11) NOT NULL,
  `projectType` tinytext NOT NULL,
  `projectName` tinytext NOT NULL,
  `projectDesc` mediumtext NOT NULL,
  `completionDate` int(11) NOT NULL,
  `complete` tinyint(1) NOT NULL DEFAULT 0,
  `secrecy` enum('SECRET','CLASSIFIED','PUBLIC') DEFAULT 'PUBLIC',
  `global` tinyint(1) NOT NULL DEFAULT 0,
  `link` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `projects`
--

INSERT INTO `projects` (`projectID`, `projectType`, `projectName`, `projectDesc`, `completionDate`, `complete`, `secrecy`, `global`, `link`) VALUES
(1, 'test', 'UCtest', 'testing', 2160, 0, 'PUBLIC', 0, 'http:'),
(2, 'testin2', 'ATtest', 'oh no!', 2153, 1, 'CLASSIFIED', 1, 'https:'),
(3, 'z', 'sharedtest', 'oops! All testing!', 400, 1, 'PUBLIC', 0, 'gttp:');

-- --------------------------------------------------------

--
-- Table structure for table `sectors`
--

CREATE TABLE `sectors` (
  `sectorID` int(11) NOT NULL,
  `planetID` int(11) NOT NULL,
  `sectorName` tinytext NOT NULL,
  `sectorDesc` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Stand-in structure for view `shared_projects`
-- (See below for the actual view)
--
CREATE TABLE `shared_projects` (
`projectName` tinytext
,`projectDesc` mediumtext
,`completionDate` int(11)
,`link` text
);

-- --------------------------------------------------------

--
-- Table structure for table `subsectors`
--

CREATE TABLE `subsectors` (
  `subsectorID` int(11) NOT NULL,
  `sectorID` int(11) NOT NULL,
  `subsectorName` tinytext NOT NULL,
  `subsectorDesc` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Stand-in structure for view `ucprojects`
-- (See below for the actual view)
--
CREATE TABLE `ucprojects` (
`projectName` tinytext
,`projectDesc` mediumtext
,`completionDate` int(11)
,`secrecy` enum('SECRET','CLASSIFIED','PUBLIC')
,`link` text
);

-- --------------------------------------------------------

--
-- Structure for view `atprojects`
--
DROP TABLE IF EXISTS `atprojects`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `atprojects`  AS SELECT `p`.`projectName` AS `projectName`, `p`.`projectDesc` AS `projectDesc`, `p`.`completionDate` AS `completionDate`, `p`.`secrecy` AS `secrecy`, `p`.`link` AS `link` FROM (`projects` `p` join `nationprojects` `np` on(`p`.`projectID` = `np`.`projectID`)) WHERE `np`.`nationID` = 2 AND `np`.`ownership` = 1 AND !exists(select 1 from (`projects` `p2` join `nationprojects` `np2` on(`p2`.`projectID` = `np2`.`projectID`)) where `np2`.`projectID` = `np`.`projectID` AND `np2`.`ownership` = 0 limit 1) ;

-- --------------------------------------------------------

--
-- Structure for view `shared_projects`
--
DROP TABLE IF EXISTS `shared_projects`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `shared_projects`  AS SELECT `p`.`projectName` AS `projectName`, `p`.`projectDesc` AS `projectDesc`, `p`.`completionDate` AS `completionDate`, `p`.`link` AS `link` FROM (`projects` `p` join `nationprojects` `np` on(`p`.`projectID` = `np`.`projectID`)) WHERE `np`.`nationID` = 1 AND exists(select 1 from (`projects` `p2` join `nationprojects` `np2` on(`p2`.`projectID` = `np2`.`projectID`)) where `np2`.`projectID` = `np`.`projectID` AND `np2`.`nationID` = 2 limit 1) ;

-- --------------------------------------------------------

--
-- Structure for view `ucprojects`
--
DROP TABLE IF EXISTS `ucprojects`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `ucprojects`  AS SELECT `p`.`projectName` AS `projectName`, `p`.`projectDesc` AS `projectDesc`, `p`.`completionDate` AS `completionDate`, `p`.`secrecy` AS `secrecy`, `p`.`link` AS `link` FROM (`projects` `p` join `nationprojects` `np` on(`p`.`projectID` = `np`.`projectID`)) WHERE `np`.`nationID` = 1 AND `np`.`ownership` = 1 AND !exists(select 1 from (`projects` `p2` join `nationprojects` `np2` on(`p2`.`projectID` = `np2`.`projectID`)) where `np2`.`projectID` = `np`.`projectID` AND `np2`.`ownership` = 0 limit 1) ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `facilities`
--
ALTER TABLE `facilities`
  ADD PRIMARY KEY (`facilityID`),
  ADD KEY `fkfacilitieslocation` (`locationID`);

--
-- Indexes for table `locations`
--
ALTER TABLE `locations`
  ADD PRIMARY KEY (`locationID`),
  ADD KEY `fklocationsubsector` (`subsectorID`),
  ADD KEY `fklocationowner` (`ownerID`);

--
-- Indexes for table `nation`
--
ALTER TABLE `nation`
  ADD PRIMARY KEY (`nationID`),
  ADD UNIQUE KEY `nameUnique` (`nationName`);

--
-- Indexes for table `nationgrowth`
--
ALTER TABLE `nationgrowth`
  ADD PRIMARY KEY (`nationID`);

--
-- Indexes for table `nationpolicies`
--
ALTER TABLE `nationpolicies`
  ADD KEY `fknationpoliciesnation` (`nationID`),
  ADD KEY `fknationpoliciespolicy` (`PolicyID`);

--
-- Indexes for table `nationprojects`
--
ALTER TABLE `nationprojects`
  ADD KEY `fknationprojectsnation` (`nationID`),
  ADD KEY `fknationprojectsproject` (`projectID`);

--
-- Indexes for table `nationsectors`
--
ALTER TABLE `nationsectors`
  ADD KEY `fknationsectornation` (`nationID`),
  ADD KEY `fknationsectorsector` (`sectorID`);

--
-- Indexes for table `nationstats`
--
ALTER TABLE `nationstats`
  ADD PRIMARY KEY (`nationID`,`year`);

--
-- Indexes for table `nationsubsectors`
--
ALTER TABLE `nationsubsectors`
  ADD KEY `fknationsubsectornation` (`nationID`),
  ADD KEY `fknationsubsectorsubsector` (`subsectorID`);

--
-- Indexes for table `planets`
--
ALTER TABLE `planets`
  ADD PRIMARY KEY (`planetID`);

--
-- Indexes for table `policies`
--
ALTER TABLE `policies`
  ADD PRIMARY KEY (`policyID`),
  ADD KEY `fkpolicyPcategory` (`policyCategory`);

--
-- Indexes for table `policycategories`
--
ALTER TABLE `policycategories`
  ADD PRIMARY KEY (`categoryID`),
  ADD UNIQUE KEY `catnameUnique` (`categoryName`);

--
-- Indexes for table `projects`
--
ALTER TABLE `projects`
  ADD PRIMARY KEY (`projectID`),
  ADD UNIQUE KEY `link` (`link`) USING HASH;

--
-- Indexes for table `sectors`
--
ALTER TABLE `sectors`
  ADD PRIMARY KEY (`sectorID`),
  ADD KEY `fksectorplanet` (`planetID`);

--
-- Indexes for table `subsectors`
--
ALTER TABLE `subsectors`
  ADD PRIMARY KEY (`subsectorID`),
  ADD KEY `fksubsectorsector` (`sectorID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `facilities`
--
ALTER TABLE `facilities`
  MODIFY `facilityID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `locations`
--
ALTER TABLE `locations`
  MODIFY `locationID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `nation`
--
ALTER TABLE `nation`
  MODIFY `nationID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `planets`
--
ALTER TABLE `planets`
  MODIFY `planetID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `policies`
--
ALTER TABLE `policies`
  MODIFY `policyID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `policycategories`
--
ALTER TABLE `policycategories`
  MODIFY `categoryID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `projects`
--
ALTER TABLE `projects`
  MODIFY `projectID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `subsectors`
--
ALTER TABLE `subsectors`
  MODIFY `subsectorID` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `facilities`
--
ALTER TABLE `facilities`
  ADD CONSTRAINT `fkfacilitieslocation` FOREIGN KEY (`locationID`) REFERENCES `locations` (`locationID`) ON UPDATE CASCADE;

--
-- Constraints for table `locations`
--
ALTER TABLE `locations`
  ADD CONSTRAINT `fklocationowner` FOREIGN KEY (`ownerID`) REFERENCES `nation` (`nationID`),
  ADD CONSTRAINT `fklocationsubsector` FOREIGN KEY (`subsectorID`) REFERENCES `subsectors` (`subsectorID`) ON UPDATE CASCADE;

--
-- Constraints for table `nationgrowth`
--
ALTER TABLE `nationgrowth`
  ADD CONSTRAINT `fknationnationgrowth` FOREIGN KEY (`nationID`) REFERENCES `nation` (`nationID`);

--
-- Constraints for table `nationpolicies`
--
ALTER TABLE `nationpolicies`
  ADD CONSTRAINT `fknationpoliciesnation` FOREIGN KEY (`nationID`) REFERENCES `nation` (`nationID`),
  ADD CONSTRAINT `fknationpoliciespolicy` FOREIGN KEY (`PolicyID`) REFERENCES `policies` (`policyID`);

--
-- Constraints for table `nationprojects`
--
ALTER TABLE `nationprojects`
  ADD CONSTRAINT `fknationprojectsnation` FOREIGN KEY (`nationID`) REFERENCES `nation` (`nationID`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fknationprojectsproject` FOREIGN KEY (`projectID`) REFERENCES `projects` (`projectID`) ON UPDATE CASCADE;

--
-- Constraints for table `nationsectors`
--
ALTER TABLE `nationsectors`
  ADD CONSTRAINT `fknationsectornation` FOREIGN KEY (`nationID`) REFERENCES `nation` (`nationID`),
  ADD CONSTRAINT `fknationsectorsector` FOREIGN KEY (`sectorID`) REFERENCES `sectors` (`sectorID`);

--
-- Constraints for table `nationstats`
--
ALTER TABLE `nationstats`
  ADD CONSTRAINT `fknationstatsnation` FOREIGN KEY (`nationID`) REFERENCES `nation` (`nationID`);

--
-- Constraints for table `nationsubsectors`
--
ALTER TABLE `nationsubsectors`
  ADD CONSTRAINT `fknationsubsectornation` FOREIGN KEY (`nationID`) REFERENCES `nation` (`nationID`),
  ADD CONSTRAINT `fknationsubsectorsubsector` FOREIGN KEY (`subsectorID`) REFERENCES `subsectors` (`subsectorID`);

--
-- Constraints for table `policies`
--
ALTER TABLE `policies`
  ADD CONSTRAINT `fkpolicyPcategory` FOREIGN KEY (`policyCategory`) REFERENCES `policycategories` (`categoryID`);

--
-- Constraints for table `sectors`
--
ALTER TABLE `sectors`
  ADD CONSTRAINT `fksectorplanet` FOREIGN KEY (`planetID`) REFERENCES `planets` (`planetID`);

--
-- Constraints for table `subsectors`
--
ALTER TABLE `subsectors`
  ADD CONSTRAINT `fksubsectorsector` FOREIGN KEY (`sectorID`) REFERENCES `sectors` (`sectorID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
