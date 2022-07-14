-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jul 14, 2022 at 05:15 PM
-- Server version: 5.7.26
-- PHP Version: 7.3.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `spider`
--

-- --------------------------------------------------------

--
-- Table structure for table `cellbank_failed_arc_url`
--

CREATE TABLE `cellbank_failed_arc_url` (
  `id` int(11) NOT NULL,
  `url` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- --------------------------------------------------------

--
-- Table structure for table `cellbank_failed_list_url`
--

CREATE TABLE `cellbank_failed_list_url` (
  `id` int(11) NOT NULL,
  `url` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- --------------------------------------------------------

--
-- Table structure for table `cellbank_production`
--

CREATE TABLE `cellbank_production` (
  `id` int(11) NOT NULL,
  `KCLBNo` varchar(100) DEFAULT NULL,
  `ProductName` varchar(100) DEFAULT NULL,
  `Distributibility` varchar(100) DEFAULT NULL,
  `CellLineSTRProfile` varchar(255) DEFAULT NULL,
  `Origin` varchar(200) DEFAULT NULL,
  `Species` varchar(100) DEFAULT NULL,
  `Strain` varchar(200) DEFAULT NULL,
  `VirusSusceptibilit` varchar(500) DEFAULT NULL,
  `VirusResistance` varchar(500) DEFAULT NULL,
  `Reversetranscritase` varchar(500) DEFAULT NULL,
  `Tumorigenecity` varchar(200) DEFAULT NULL,
  `Isoenzyme` varchar(255) DEFAULT NULL,
  `Karyology` varchar(400) DEFAULT NULL,
  `CellularMorphology` varchar(100) DEFAULT NULL,
  `Production` varchar(500) DEFAULT NULL,
  `Histocompatibility` varchar(255) DEFAULT NULL,
  `GrowthPattern` varchar(100) DEFAULT NULL,
  `Histopathology` varchar(200) DEFAULT NULL,
  `Differentiation` varchar(255) DEFAULT NULL,
  `FreezingMedia` varchar(150) DEFAULT NULL,
  `OriginalMedia` varchar(300) DEFAULT NULL,
  `KCLBMedia` varchar(500) DEFAULT NULL,
  `Depositor` varchar(500) DEFAULT NULL,
  `Subculture` varchar(500) DEFAULT NULL,
  `Reference` varchar(500) DEFAULT NULL,
  `Note` varchar(1500) DEFAULT NULL,
  `Hit` varchar(100) DEFAULT NULL,
  `SplitRatio` varchar(100) DEFAULT NULL,
  `MediaChange` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- --------------------------------------------------------

--
-- Table structure for table `userinfo`
--

CREATE TABLE `userinfo` (
  `id` int(11) NOT NULL,
  `account` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `country` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `wallet` varchar(500) COLLATE utf8_unicode_ci DEFAULT NULL,
  `balance` varchar(500) COLLATE utf8_unicode_ci DEFAULT NULL,
  `orderinfo` varchar(1000) COLLATE utf8_unicode_ci DEFAULT NULL,
  `purchases` varchar(500) COLLATE utf8_unicode_ci DEFAULT NULL,
  `address` varchar(500) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ua` varchar(500) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `userinfo`
--

INSERT INTO `userinfo` (`id`, `account`, `country`, `wallet`, `balance`, `orderinfo`, `purchases`, `address`, `ua`) VALUES
(6, 'lm', 'jp', '{}', '$0.00', '最近三个月 无订单|无订单', '不可以评论', '{}', 'Mozilla/4.0 (Mozilla/4.0; MSIE 7.0; Windows NT 5.1; FDM; SV1)'),
(8, 'ln', 'jp', '{}', NULL, NULL, '不可以评论', '{}', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.9683.99 Safari/537.36');

-- --------------------------------------------------------

--
-- Table structure for table `userlist`
--

CREATE TABLE `userlist` (
  `id` int(11) NOT NULL,
  `account` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cookie` text COLLATE utf8_unicode_ci,
  `status` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `host` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `password` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `region` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ip` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ua` varchar(500) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci ROW_FORMAT=DYNAMIC;

--
-- Dumping data for table `userlist`
--

INSERT INTO `userlist` (`id`, `account`, `cookie`, `status`, `host`, `password`, `region`, `ip`, `ua`) VALUES
(1, 'lm', '[\r\n    {\r\n        \"domain\": \".amazon.com\",\r\n        \"expiry\": 1687485434,\r\n        \"httpOnly\": false,\r\n        \"name\": \"i18n-prefs\",\r\n        \"path\": \"/\",\r\n        \"secure\": false,\r\n        \"value\": \"USD\"\r\n    },\r\n    {\r\n        \"domain\": \".amazon.com\",\r\n        \"expiry\": 1687485434,\r\n        \"httpOnly\": false,\r\n        \"name\": \"session-id-time\",\r\n        \"path\": \"/\",\r\n        \"secure\": true,\r\n        \"value\": \"2082787201l\"\r\n    },\r\n    {\r\n        \"domain\": \".amazon.com\",\r\n        \"expiry\": 1687485434,\r\n        \"httpOnly\": false,\r\n        \"name\": \"lc-main\",\r\n        \"path\": \"/\",\r\n        \"secure\": false,\r\n        \"value\": \"en_US\"\r\n    },\r\n    {\r\n        \"domain\": \".amazon.com\",\r\n        \"expiry\": 1687485434,\r\n        \"httpOnly\": true,\r\n        \"name\": \"sst-main\",\r\n        \"path\": \"/\",\r\n        \"secure\": true,\r\n        \"value\": \"Sst1|PQES8VCVFwxfCs3_9OTgAJiZCdPU6o0AiWIP4sQpT7U47WdVEyYTXYz2FjR99KM9tlfZ9HVsjcRq-QTnPQZKzRSj-jbPiXficDD3sRa89VrNUMbKMqg623eal5koAY1eW4Op2lcutXHC-ogCJWgEz9oCQY-3VajFK9EbYbA_BqdLglCmea5Z9hQCl0af007cJmEMDbwa6Tr6Dh6i0K_cPVjdbHfmq1Qd_Fx3uWMbBf3RRbHYki6jv5gx58uHu4hnjhLjBjW7gFD3IXQFwZC-J6YXwidtl6mb1TQXkwBlF-GlUjw\"\r\n    },\r\n    {\r\n        \"domain\": \".amazon.com\",\r\n        \"expiry\": 1687485434,\r\n        \"httpOnly\": true,\r\n        \"name\": \"sess-at-main\",\r\n        \"path\": \"/\",\r\n        \"secure\": true,\r\n        \"value\": \"\\\"I4M9zooxw106cHzziMPiAKtYsfqOK20N/+eC98NGH+g=\\\"\"\r\n    },\r\n    {\r\n        \"domain\": \".amazon.com\",\r\n        \"expiry\": 1687485434,\r\n        \"httpOnly\": false,\r\n        \"name\": \"session-id\",\r\n        \"path\": \"/\",\r\n        \"secure\": true,\r\n        \"value\": \"133-1539554-9308568\"\r\n    },\r\n    {\r\n        \"domain\": \".amazon.com\",\r\n        \"expiry\": 1687485434,\r\n        \"httpOnly\": false,\r\n        \"name\": \"x-main\",\r\n        \"path\": \"/\",\r\n        \"secure\": true,\r\n        \"value\": \"\\\"SATBkrP6ijVnAZY0G2ojikFpw?BWVTVfML52BGdC4UXsvqnR@Vius9Birlf74P2g\\\"\"\r\n    },\r\n    {\r\n        \"domain\": \".amazon.com\",\r\n        \"expiry\": 1687485434,\r\n        \"httpOnly\": false,\r\n        \"name\": \"session-token\",\r\n        \"path\": \"/\",\r\n        \"secure\": true,\r\n        \"value\": \"bg7fU8Ar0k8Yfa18jGtB9W38pRuiSDQseGmqdc5JOcmsh4SschP5G6IXTI489r3zOOzxYHbfPjw6Tkn4OaspBxWEZOSVrpUhriD6uiIJQtOpbJSow3FSnFV/AehfQCC7zCGi9rVrjOiPeSOOizUAeehpxKnp6DbL2qUbZWie3Lhn4yCKwxMKtb+9E0YEs+qFHXlSHpFAKRKlIduVrS8fXVtm87P33V5srlbvNHbvwEVl/xuG0TbS2EBfdrQ6ZyG2\"\r\n    },\r\n    {\r\n        \"domain\": \".amazon.com\",\r\n        \"expiry\": 1687485434,\r\n        \"httpOnly\": false,\r\n        \"name\": \"ubid-main\",\r\n        \"path\": \"/\",\r\n        \"secure\": true,\r\n        \"value\": \"131-5614265-4524345\"\r\n    },\r\n    {\r\n        \"domain\": \"www.amazon.com\",\r\n        \"expiry\": 1686189435,\r\n        \"httpOnly\": false,\r\n        \"name\": \"csm-hit\",\r\n        \"path\": \"/\",\r\n        \"secure\": false,\r\n        \"value\": \"tb:s-X7RG2JBBVW4XQ57H13CZ|1655949435072&t:1655949435561&adb:adblk_no\"\r\n    },\r\n    {\r\n        \"domain\": \".amazon.com\",\r\n        \"expiry\": 1687485434,\r\n        \"httpOnly\": true,\r\n        \"name\": \"at-main\",\r\n        \"path\": \"/\",\r\n        \"secure\": true,\r\n        \"value\": \"Atza|IwEBILaWu9ygWzzRh32JLIcZ2-fG4hAuGsJkI0JYLGr-UNHocG90_4q2azss5PSP5-KJN93eDEoAhLzu1x2zt3WvAFAjSAMEtvlrOQp67pfYd-L8wI85f_ax1goYUsXYwbCcijXv74eECn8AFwM5EnDcc4ValYpV_8XHLMdexwKa87iLahR7rWMqfBDIVD6HSCvX1DaNdjRkA9ldN1aHIm0ZH_Nn84J_bBl1Lpl5mRCutR7APQ\"\r\n    }\r\n]', '1', 'www.amazon.com', NULL, 'us', NULL, NULL),
(2, 'ln', '[\r\n    {\r\n        \"domain\": \".amazon.co.jp\",\r\n        \"expirationDate\": 1686142372.60009,\r\n        \"hostOnly\": false,\r\n        \"httpOnly\": true,\r\n        \"name\": \"at-acbjp\",\r\n        \"path\": \"/\",\r\n        \"sameSite\": \"unspecified\",\r\n        \"secure\": true,\r\n        \"session\": false,\r\n        \"storeId\": \"0\",\r\n        \"value\": \"Atza|IwEBIB5-kOuh2EUPDkfv1U_xpJK4tbIx4-5ixGKPRlQKaH_W6JEAphY80S3gWkk0TMGsppjKnRtLYoyXBVkqTzH2vCO9R7ULe8ugUG97ZjJpspI5wKljI1oAruiQEDTggD5Rt9h28lpERyOktztPtfBQq_6-fKglIrVNZKJe9LkAteriPCDnoQP2Nr4L_zs3-sBB0NGw6u7qJyNmDa3W-hQ8zwBLjtFU0EwDlojZTqANTKkQxoafu51xNPic8Ldl2g77YaI\",\r\n        \"id\": 1\r\n    },\r\n    {\r\n        \"domain\": \".amazon.co.jp\",\r\n        \"expirationDate\": 1686143963.469789,\r\n        \"hostOnly\": false,\r\n        \"httpOnly\": false,\r\n        \"name\": \"i18n-prefs\",\r\n        \"path\": \"/\",\r\n        \"sameSite\": \"unspecified\",\r\n        \"secure\": false,\r\n        \"session\": false,\r\n        \"storeId\": \"0\",\r\n        \"value\": \"JPY\",\r\n        \"id\": 2\r\n    },\r\n    {\r\n        \"domain\": \".amazon.co.jp\",\r\n        \"expirationDate\": 1686143963.469799,\r\n        \"hostOnly\": false,\r\n        \"httpOnly\": false,\r\n        \"name\": \"lc-acbjp\",\r\n        \"path\": \"/\",\r\n        \"sameSite\": \"unspecified\",\r\n        \"secure\": false,\r\n        \"session\": false,\r\n        \"storeId\": \"0\",\r\n        \"value\": \"ja_JP\",\r\n        \"id\": 3\r\n    },\r\n    {\r\n        \"domain\": \".amazon.co.jp\",\r\n        \"expirationDate\": 1686142372.600099,\r\n        \"hostOnly\": false,\r\n        \"httpOnly\": true,\r\n        \"name\": \"sess-at-acbjp\",\r\n        \"path\": \"/\",\r\n        \"sameSite\": \"unspecified\",\r\n        \"secure\": true,\r\n        \"session\": false,\r\n        \"storeId\": \"0\",\r\n        \"value\": \"\\\"FivsmmX1jR7rT0PQFGbJswEkgOLN3sOrrn67WaNDMN0=\\\"\",\r\n        \"id\": 4\r\n    },\r\n    {\r\n        \"domain\": \".amazon.co.jp\",\r\n        \"expirationDate\": 1686143963.469694,\r\n        \"hostOnly\": false,\r\n        \"httpOnly\": false,\r\n        \"name\": \"session-id\",\r\n        \"path\": \"/\",\r\n        \"sameSite\": \"unspecified\",\r\n        \"secure\": true,\r\n        \"session\": false,\r\n        \"storeId\": \"0\",\r\n        \"value\": \"357-9529525-0515314\",\r\n        \"id\": 5\r\n    },\r\n    {\r\n        \"domain\": \".amazon.co.jp\",\r\n        \"expirationDate\": 1686143963.469767,\r\n        \"hostOnly\": false,\r\n        \"httpOnly\": false,\r\n        \"name\": \"session-id-time\",\r\n        \"path\": \"/\",\r\n        \"sameSite\": \"unspecified\",\r\n        \"secure\": true,\r\n        \"session\": false,\r\n        \"storeId\": \"0\",\r\n        \"value\": \"2082787201l\",\r\n        \"id\": 6\r\n    },\r\n    {\r\n        \"domain\": \".amazon.co.jp\",\r\n        \"expirationDate\": 1686195208.741157,\r\n        \"hostOnly\": false,\r\n        \"httpOnly\": false,\r\n        \"name\": \"session-token\",\r\n        \"path\": \"/\",\r\n        \"sameSite\": \"unspecified\",\r\n        \"secure\": true,\r\n        \"session\": false,\r\n        \"storeId\": \"0\",\r\n        \"value\": \"uwOmbVwcOeObXKR0I2nCx9WYCbv9CRGzH+k7ky/0CnhBdw2wE1aH01G9is5zm+tQmh2dKIwb1TZNmM+gDfIeUsYYq125iDKcALQ0dbKhLDigYaPGxc0cdsTgKZnNT/gU11Z5Ee3RapU+o7DiclDmIMviHDPCGoOM/TwEV0xcn9EHB2HEegHp+e845QNJX8QS39B8g7704nsgZh3+2G8wHjbB8Jb9zDOL\",\r\n        \"id\": 7\r\n    },\r\n    {\r\n        \"domain\": \".amazon.co.jp\",\r\n        \"hostOnly\": false,\r\n        \"httpOnly\": false,\r\n        \"name\": \"skin\",\r\n        \"path\": \"/\",\r\n        \"sameSite\": \"unspecified\",\r\n        \"secure\": false,\r\n        \"session\": true,\r\n        \"storeId\": \"0\",\r\n        \"value\": \"noskin\",\r\n        \"id\": 8\r\n    },\r\n    {\r\n        \"domain\": \".amazon.co.jp\",\r\n        \"expirationDate\": 1686142372.600108,\r\n        \"hostOnly\": false,\r\n        \"httpOnly\": true,\r\n        \"name\": \"sst-acbjp\",\r\n        \"path\": \"/\",\r\n        \"sameSite\": \"unspecified\",\r\n        \"secure\": true,\r\n        \"session\": false,\r\n        \"storeId\": \"0\",\r\n        \"value\": \"Sst1|PQFkoyfq0GjOnDJCprWDKmSUCf_--66flUkfUEgMnosRg4i2q1uh0wZ2KKVFgK5wNrugBq3HbBbx_e9dJ77D3bhkDm_5mhCx5lYOQeg2HtwqInzR2-AEEtwgVN5UpUkoDybljii68Uhhx4BrHPCxnL1M1sVBVTHTT2GCJnVxRgbHcgAqXtOBKNX-MArIz7bPZrGs_2Jf3aiOfSJVgd-PB_UTPmQsVQEmHjjLsXXNYOIXZ_DMoIs6S1QJzgJ4vL-RLMgED1G0g9Ysgg19sIdgKjqi_OokroYQFiYiUVisoT3Oz4o\",\r\n        \"id\": 9\r\n    },\r\n    {\r\n        \"domain\": \".amazon.co.jp\",\r\n        \"expirationDate\": 1686143963.469742,\r\n        \"hostOnly\": false,\r\n        \"httpOnly\": false,\r\n        \"name\": \"ubid-acbjp\",\r\n        \"path\": \"/\",\r\n        \"sameSite\": \"unspecified\",\r\n        \"secure\": true,\r\n        \"session\": false,\r\n        \"storeId\": \"0\",\r\n        \"value\": \"357-5284980-2541423\",\r\n        \"id\": 10\r\n    },\r\n    {\r\n        \"domain\": \".amazon.co.jp\",\r\n        \"expirationDate\": 1686143963.469777,\r\n        \"hostOnly\": false,\r\n        \"httpOnly\": false,\r\n        \"name\": \"x-acbjp\",\r\n        \"path\": \"/\",\r\n        \"sameSite\": \"unspecified\",\r\n        \"secure\": true,\r\n        \"session\": false,\r\n        \"storeId\": \"0\",\r\n        \"value\": \"OVwP6oObfMJKxAYBvg6lObFaClAdMFOhx5R2wLKllL8SoWPMpGYqBuRb8w5ftlcu\",\r\n        \"id\": 11\r\n    },\r\n    {\r\n        \"domain\": \"www.amazon.co.jp\",\r\n        \"expirationDate\": 1659791189,\r\n        \"hostOnly\": true,\r\n        \"httpOnly\": false,\r\n        \"name\": \"csd-key\",\r\n        \"path\": \"/\",\r\n        \"sameSite\": \"unspecified\",\r\n        \"secure\": true,\r\n        \"session\": false,\r\n        \"storeId\": \"0\",\r\n        \"value\": \"eyJ3YXNtVGVzdGVkIjp0cnVlLCJ3YXNtQ29tcGF0aWJsZSI6dHJ1ZSwid2ViQ3J5cHRvVGVzdGVkIjpmYWxzZSwidiI6MSwia2lkIjoiMTE2M2EzIiwia2V5IjoiWldVK1dPOTMyYmVYTGZ4SVdjQnN3cUpIME1FNE9qZmVKVGI4UFVTeEtGS3VCakFPN21kbUJXTWtrajRZRnVyMWd3MVZqT1VSVlNZdlg5Wmx0TFo3NFdiQzB6bGhpbUg4TnNGQ2NSQnYvQWl3RWhscGZQTUFnbTlPMldyRnFrNXNWejRNK3krdDBCalloWGdTODZEL2wrK2pGT2VyYllTY1dZNUttOXhoeTZnK0I3a2xmdFBpYzRIc2d1bzcreUZmcXIwcmMwM2x6MHV6Rkc2TnVzc0R1dlhjTFJSOHBIaXZqSFdoazBpYnUyTGU2OC9tSU1pTCtIM2Y2RDN3alJHdHRTd3JrUTlRV2hzYTZNY0hxR2ozUUZzS2FRcEhaVDBNRG1TaGdEVExmaFRZcVVoeE1wQS82UjNGaFF1bEw1SUZKVE1UYmgzOXQ5WTZWalJuSHI0ZFBnPT0ifQ==\",\r\n        \"id\": 12\r\n    },\r\n    {\r\n        \"domain\": \"www.amazon.co.jp\",\r\n        \"expirationDate\": 1684899211,\r\n        \"hostOnly\": true,\r\n        \"httpOnly\": false,\r\n        \"name\": \"csm-hit\",\r\n        \"path\": \"/\",\r\n        \"sameSite\": \"unspecified\",\r\n        \"secure\": false,\r\n        \"session\": false,\r\n        \"storeId\": \"0\",\r\n        \"value\": \"tb:s-E7CVRNSVBWWE6SKSENB6|1654659209112&t:1654659211672&adb:adblk_yes\",\r\n        \"id\": 13\r\n    }\r\n    ]', '1', 'www.amazon.co.jp', NULL, 'jp', NULL, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cellbank_failed_arc_url`
--
ALTER TABLE `cellbank_failed_arc_url`
  ADD PRIMARY KEY (`id`) USING BTREE;

--
-- Indexes for table `cellbank_failed_list_url`
--
ALTER TABLE `cellbank_failed_list_url`
  ADD PRIMARY KEY (`id`) USING BTREE;

--
-- Indexes for table `cellbank_production`
--
ALTER TABLE `cellbank_production`
  ADD PRIMARY KEY (`id`) USING BTREE;

--
-- Indexes for table `userinfo`
--
ALTER TABLE `userinfo`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `account_2` (`account`),
  ADD KEY `account` (`account`);

--
-- Indexes for table `userlist`
--
ALTER TABLE `userlist`
  ADD PRIMARY KEY (`id`) USING BTREE;

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cellbank_failed_arc_url`
--
ALTER TABLE `cellbank_failed_arc_url`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `cellbank_failed_list_url`
--
ALTER TABLE `cellbank_failed_list_url`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `cellbank_production`
--
ALTER TABLE `cellbank_production`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userinfo`
--
ALTER TABLE `userinfo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `userlist`
--
ALTER TABLE `userlist`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
