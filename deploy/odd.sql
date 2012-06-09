-- MySQL dump 10.13  Distrib 5.1.62, for debian-linux-gnu (i686)
--
-- Host: localhost    Database: odd
-- ------------------------------------------------------
-- Server version	5.1.62-0ubuntu0.11.10.1

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
-- Table structure for table `answer_ups`
--

DROP TABLE IF EXISTS `answer_ups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `answer_ups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `answer_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `up` (`answer_id`,`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `answer_ups`
--

LOCK TABLES `answer_ups` WRITE;
/*!40000 ALTER TABLE `answer_ups` DISABLE KEYS */;
INSERT INTO `answer_ups` VALUES (1,1,1),(2,2,1),(3,3,1),(4,4,1),(5,2,3),(6,5,1),(7,4,4),(8,10,1),(9,12,5),(10,1,3),(11,2,4),(12,1,4),(13,19,1),(14,18,1),(15,17,1),(16,20,1),(17,25,1),(18,28,4),(19,31,1),(20,30,3),(21,31,3),(22,32,1),(23,33,1),(24,34,1),(25,44,1),(26,45,1),(27,46,1),(28,30,1);
/*!40000 ALTER TABLE `answer_ups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `answers`
--

DROP TABLE IF EXISTS `answers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `answers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `content` text NOT NULL,
  `create_time` datetime NOT NULL,
  `up` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `question_id` (`question_id`)
) ENGINE=MyISAM AUTO_INCREMENT=47 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `answers`
--

LOCK TABLES `answers` WRITE;
/*!40000 ALTER TABLE `answers` DISABLE KEYS */;
INSERT INTO `answers` VALUES (1,2,1,'还是马里兰好一点吧 地址位置比较重要','2012-05-23 21:35:44',3),(2,2,1,'xx','2012-05-23 21:41:00',3),(3,2,1,'oo','2012-05-24 12:31:42',1),(4,2,1,'shit','2012-05-24 16:18:03',2),(5,3,3,'女人去上班了','2012-05-24 19:13:50',1),(6,6,4,'价格还可以 400一个月以内吧','2012-05-24 19:38:53',0),(7,4,4,'芝大化学系还可以啊 全美12的样子','2012-05-24 19:43:42',0),(8,5,4,'必须啊 多的一米','2012-05-24 19:43:56',0),(9,10,4,'1抓紧买吧  \r\n2离学校不远 有shuttle \r\n3这个可以连接中国学生会','2012-05-24 19:44:31',0),(10,8,1,'wo shi shi ','2012-05-24 21:14:45',1),(11,13,1,'狗男女！！！！','2012-05-24 21:23:27',0),(12,13,5,'马骁野你是屎！！！','2012-05-24 21:27:15',1),(13,8,1,'房价又涨了','2012-05-26 11:24:38',0),(14,8,1,'广告招租','2012-05-26 11:40:02',0),(15,8,1,'我能说脏话吗','2012-05-26 11:44:17',0),(16,8,1,'顶ls','2012-05-26 12:05:56',0),(17,2,1,'aa','2012-05-26 12:10:27',1),(18,2,1,'bb','2012-05-26 12:12:22',1),(19,2,1,'cc','2012-05-26 12:15:38',1),(20,2,1,'dd','2012-05-26 12:21:53',1),(21,12,1,'今天晚上就分了','2012-05-26 13:56:44',0),(22,11,3,'好','2012-05-26 15:25:24',0),(23,12,1,'oohh','2012-05-26 16:12:31',0),(24,2,1,'shit','2012-05-26 16:14:32',0),(25,2,1,'ooo','2012-05-26 16:25:06',1),(26,9,4,'1百万','2012-05-26 17:32:55',0),(27,21,4,'怎么讲？','2012-05-26 17:34:01',0),(28,5,4,'多的一米那啥','2012-05-26 17:36:34',1),(29,21,1,'hello\r\nworld','2012-05-26 21:09:53',0),(30,26,3,'据我所知明年这个时候会有','2012-05-26 21:17:13',2),(31,26,1,' 在马骁野被据签以后就来了 就在6.1号哈哈','2012-05-26 21:17:46',2),(32,24,1,'匆匆过客','2012-05-29 16:25:26',2),(33,24,1,'太年轻了','2012-05-29 16:47:08',1),(34,24,1,'too simple','2012-05-29 16:56:40',1),(35,24,1,'so naive','2012-05-29 16:59:09',0),(36,24,1,'2b','2012-05-29 17:02:37',0),(37,24,1,'战斗吧，少年！','2012-05-29 17:06:45',0),(38,24,1,'ohh','2012-05-29 17:22:34',0),(39,24,1,'aaa','2012-05-29 17:23:19',0),(40,24,1,'ohh','2012-05-29 18:06:33',0),(41,24,1,'0hh\r\n','2012-05-29 19:48:24',0),(42,24,1,'haha','2012-05-30 21:01:39',0),(43,24,1,'hahah','2012-05-30 21:03:32',0),(44,23,1,'hello','2012-05-30 21:04:42',1),(45,23,1,'world\r\n','2012-05-30 21:09:49',1),(46,35,1,'helo','2012-05-31 10:52:28',1);
/*!40000 ALTER TABLE `answers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `answer_id` int(11) NOT NULL,
  `comment_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `content` text NOT NULL,
  `create_time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `answer_id` (`answer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=46 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES (1,1,-1,1,'shit','2012-05-24 11:38:21'),(2,1,-1,1,'oh,shit','2012-05-24 12:16:17'),(3,1,1,1,'回复xys:fuck','2012-05-24 12:17:12'),(4,2,-1,1,'DXX','2012-05-24 12:18:27'),(5,2,4,1,'回复xys：DDXX','2012-05-24 12:18:37'),(6,3,-1,1,'dirty man','2012-05-24 12:32:17'),(7,3,6,1,'回复xys：说谁呢','2012-05-24 12:32:30'),(8,4,-1,1,'oh','2012-05-24 16:18:15'),(9,4,8,1,'回复xys：ohoh','2012-05-24 16:18:32'),(10,1,1,3,'回复xys：粗俗的一米','2012-05-24 19:12:34'),(11,1,-1,3,'o shit','2012-05-24 19:12:49'),(12,1,3,4,'回复xys：强哥要注意身体','2012-05-24 19:45:41'),(13,2,4,4,'回复xys：强哥说的在理','2012-05-24 19:45:56'),(14,1,10,4,'回复urantroiin：你别装逼了！','2012-05-24 19:46:10'),(15,3,7,4,'回复xys：最近压力是不是太大了？','2012-05-24 19:46:23'),(16,4,-1,4,'yeah yeah yeah','2012-05-24 19:46:36'),(17,5,-1,1,'pi','2012-05-24 21:15:29'),(18,5,17,1,'回复xys：pi','2012-05-24 21:15:44'),(19,5,18,4,'回复xys：黄一桐你不是人','2012-05-24 21:17:52'),(20,5,18,4,'回复xys：放开我！','2012-05-24 21:18:01'),(21,12,-1,1,'黄一桐快点送冰棍来，想吃了！','2012-05-25 19:10:58'),(22,12,21,1,'回复xys：GD！','2012-05-25 19:57:41'),(23,13,-1,1,'人民生活在水深火热之中','2012-05-26 11:34:07'),(24,13,23,1,'回复xys：感谢党感谢国家','2012-05-26 11:38:11'),(25,19,-1,1,'dd','2012-05-26 12:21:00'),(26,16,-1,1,'顶啥顶','2012-05-26 13:42:13'),(27,16,26,1,'回复xys：怎么了找茬是吧','2012-05-26 13:50:17'),(28,1,3,3,'回复xys：隐没','2012-05-26 13:59:46'),(29,1,28,1,'回复urantroiin：不是','2012-05-26 14:00:15'),(30,22,-1,3,'好','2012-05-26 15:25:34'),(31,22,30,3,'回复urantroiin：好','2012-05-26 15:25:40'),(32,4,16,1,'回复daisent：hhh','2012-05-26 15:26:41'),(33,24,-1,1,'hello','2012-05-26 16:21:49'),(34,24,-1,1,'oh shit','2012-05-26 16:39:37'),(35,24,-1,1,'fuck','2012-05-26 16:40:36'),(36,24,-1,1,'you','2012-05-26 16:41:11'),(37,11,-1,1,'恩','2012-05-26 16:54:42'),(38,27,-1,4,'说的好','2012-05-26 17:34:18'),(39,27,38,4,'回复daisent：说的好','2012-05-26 17:34:31'),(40,27,39,4,'回复daisent：说的好','2012-05-26 17:34:38'),(41,27,39,4,'回复daisent：说的好','2012-05-26 17:34:45'),(42,24,-1,4,'yes','2012-05-26 20:04:12'),(43,24,42,4,'回复daisent：yes','2012-05-26 20:04:21'),(44,37,-1,1,'好基友','2012-05-29 17:07:28'),(45,37,44,1,'回复xys：好朋友','2012-05-29 17:17:09');
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notice_tags`
--

DROP TABLE IF EXISTS `notice_tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `notice_tags` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `notice_id` int(11) NOT NULL,
  `tag` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tag` (`tag`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notice_tags`
--

LOCK TABLES `notice_tags` WRITE;
/*!40000 ALTER TABLE `notice_tags` DISABLE KEYS */;
/*!40000 ALTER TABLE `notice_tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notices`
--

DROP TABLE IF EXISTS `notices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `notices` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(128) NOT NULL,
  `content` text NOT NULL,
  `create_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notices`
--

LOCK TABLES `notices` WRITE;
/*!40000 ALTER TABLE `notices` DISABLE KEYS */;
/*!40000 ALTER TABLE `notices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question_edits`
--

DROP TABLE IF EXISTS `question_edits`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `question_edits` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `question_id` int(11) NOT NULL,
  `tags` text NOT NULL,
  `create_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question_edits`
--

LOCK TABLES `question_edits` WRITE;
/*!40000 ALTER TABLE `question_edits` DISABLE KEYS */;
INSERT INTO `question_edits` VALUES (1,1,45,'g#SUNY--Stony Brook#American University','2012-06-07 16:46:31'),(2,1,45,'g#SUNY--Stony Brook#American University#c','2012-06-07 16:47:26');
/*!40000 ALTER TABLE `question_edits` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question_tags`
--

DROP TABLE IF EXISTS `question_tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `question_tags` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question_id` int(11) NOT NULL,
  `tag` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `question_id` (`question_id`),
  KEY `tag` (`tag`)
) ENGINE=MyISAM AUTO_INCREMENT=230 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question_tags`
--

LOCK TABLES `question_tags` WRITE;
/*!40000 ALTER TABLE `question_tags` DISABLE KEYS */;
INSERT INTO `question_tags` VALUES (1,2,'UIUC'),(2,2,'经济学'),(3,2,'马里兰大学'),(4,3,'uiuc'),(5,4,'uchicago'),(6,5,'选房'),(7,5,'uchicago'),(8,6,'iowa-city'),(9,6,'university'),(10,6,'iowa'),(11,6,'选房'),(12,6,'of'),(13,7,'iowa-city'),(14,7,'选房'),(15,7,'university-of-iowa'),(16,8,'UIUC'),(17,8,'选房'),(18,9,'university-of-iowa'),(19,9,'学费'),(20,10,'接机'),(21,10,'机票'),(22,10,'uchicago'),(23,11,'university-of-iowa'),(24,11,'Iowa-city'),(25,11,'iowa-city'),(26,12,'基情'),(27,12,'分手'),(28,13,'基情'),(29,14,'神'),(30,15,'排名'),(31,15,'Harvard'),(32,15,'化学'),(33,16,'Duke'),(34,16,'Columbia'),(35,16,'Stanford'),(36,16,'Princeton'),(37,16,'Caltech'),(38,16,'harvard'),(39,16,'MIT'),(40,17,'Emory'),(41,17,'Cornell'),(42,17,'University of Southern California(USC)'),(43,17,'University of North Carolina--Chapel Hill (UNC)'),(44,17,'Carnegie Mellon'),(45,17,'University of Michigan--Ann Arbor'),(46,17,'Rice'),(47,17,'California Institute of Technology'),(48,17,'Brown'),(49,17,'University of California--Los Angeles(UCLA)'),(50,17,'Chicago'),(51,17,'Vanderbilt'),(52,17,'Tufts'),(53,17,'Northwestern'),(54,17,'University of Pennsylvania'),(55,17,'Georgetown'),(56,17,'University of Virginia'),(57,17,'Washington University in St. Louis(WUSL)'),(58,17,'Notre Dame'),(59,17,'Massachusetts Institute of Technology (MIT)'),(60,17,'Duke'),(61,17,'Johns Hopkins'),(62,17,'Dartmouth College'),(63,17,'University of California--Berkeley(UCBerkeley)'),(64,17,'Wake Forest University'),(65,18,'University of Washington'),(66,18,'University of California--Davis(UCD)'),(67,18,'Pennsylvania State University--University Park'),(68,18,'New York University(NYU)'),(69,18,'Boston College(BC)'),(70,18,'University of Rochester'),(71,18,'University of California--Santa Barbara(UCSB)'),(72,18,'Georgia Institute of Technology(GIT)'),(73,18,'University of Wisconsin--Madison(UWM)'),(74,18,'Rensselaer Polytechnic Institute'),(75,18,'University of California--San Diego(UCSD)'),(76,18,'University of California--Irvine(UCI)'),(77,18,'College of William and Mary'),(78,18,'Brandeis University'),(79,18,'University of Illinois--Urbana-Champaign(UIUC)'),(80,18,'Yeshiva University'),(81,18,'Lehigh University'),(82,18,'University of Texas--Austin'),(83,18,'Case Western Reserve University'),(84,18,'University of Miami'),(85,19,'Syracuse University'),(86,19,'University of Connecticut'),(87,19,'University of Florida'),(88,19,'University of Minnesota--Twin Cities'),(89,19,'Purdue University--West Lafayette'),(90,19,'Tulane University'),(91,19,'Boston University(BU)'),(92,19,'the State University of New Jersey--New Brunswick'),(93,19,'Worcester Polytechnic Institute'),(94,19,'University of Pittsburgh'),(95,19,'University of Maryland--College Park（UMD)'),(96,19,'Rutgers'),(97,19,'George Washington University'),(98,19,'University of Georgia'),(99,19,'Southern Methodist University'),(100,19,'Ohio State University--Columbus'),(101,19,'Clemson University'),(102,19,'Northeastern University'),(103,19,'Texas A&M University--College Station'),(104,19,'Pepperdine University'),(105,19,'Virginia Tech'),(106,19,'Fordham University'),(107,20,'University of Dayton'),(108,20,'University of the Pacific'),(109,20,'University of Missouri'),(110,20,'SUNY College of Environmental Science and Forestry'),(111,20,'University of California--Santa Cruz(UCSC)'),(112,20,'Colorado School of Mines'),(113,20,'Brigham Young University--Provo'),(114,20,'Drexel University'),(115,20,'University of Colorado--Boulder'),(116,20,'University of Alabama'),(117,20,'Marquette University'),(118,20,'University of California--Riverside'),(119,20,'University of Vermont'),(120,20,'American University'),(121,20,'University of Delaware'),(122,20,'St. Louis University'),(123,20,'Auburn University'),(124,20,'Texas Christian University'),(125,20,'Miami University--Oxford'),(126,20,'Indiana University--Bloomington'),(127,20,'University of Iowa'),(128,20,'Baylor University'),(129,20,'Iowa State University'),(130,20,'University of Denver'),(131,20,'University of Tulsa'),(132,20,'SUNY--Stony Brook'),(133,20,'University of Massachusetts--Amherst'),(134,20,'Michigan State University'),(135,20,'Binghamton University--SUNY'),(136,20,'Stevens Institute of Technology'),(137,20,'University of San Diego'),(138,20,'Clark University'),(139,21,'基情'),(140,22,'test computer science'),(141,23,'computer'),(142,23,'science'),(143,24,'人生'),(144,24,'2B'),(217,25,'哲学'),(216,25,'SUNY--Stony Brook'),(215,25,'基情'),(149,26,'SUNY--Stony Brook'),(150,26,'i20'),(153,35,'经济学'),(154,37,'UIUC'),(155,38,'UIUC'),(156,38,'a'),(214,39,'d'),(213,39,'b'),(204,40,'d'),(161,41,'e'),(162,42,'e'),(163,42,'f'),(164,43,'f'),(165,43,'e'),(228,45,'American University'),(203,40,'c'),(208,44,'Caltech'),(212,39,'UIUC'),(207,44,'a'),(227,45,'SUNY--Stony Brook'),(226,45,'g'),(229,45,'c');
/*!40000 ALTER TABLE `question_tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questions`
--

DROP TABLE IF EXISTS `questions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `questions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `content` text NOT NULL,
  `create_time` datetime NOT NULL,
  `answer_count` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `create_time` (`create_time`),
  KEY `user_id` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=46 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questions`
--

LOCK TABLES `questions` WRITE;
/*!40000 ALTER TABLE `questions` DISABLE KEYS */;
INSERT INTO `questions` VALUES (1,1,'各位童鞋，UMD马里兰大学帕克分校是个什么情况？和UIUC比呢？','本科经济学，收了两个AD，UMD貌似地理位置不错，但网上那个学校的信息略少啊，求助！还有大家觉得UIUC好还是UMD好呢？谢谢谢啦!（^_^）','2012-05-23 15:43:14',0),(2,1,'各位童鞋，UMD马里兰大学帕克分校是个什么情况？和UIUC比呢？','本科经济学，收了两个AD，UMD貌似地理位置不错，但网上那个学校的信息略少啊，求助！还有大家觉得UIUC好还是UMD好呢？谢谢谢啦!（^_^）','2012-05-23 15:43:50',10),(3,3,'强哥的女人今天怎么没来','强哥说随便写','2012-05-24 19:12:07',1),(4,3,'芝大化学怎么样','求问？','2012-05-24 19:16:40',1),(5,3,'芝大黑人是不是有点太多了？','如题啊，地理位置有点担心','2012-05-24 19:18:04',2),(6,3,'iowa city 房子贵么？','中心城区房子价格在多少？','2012-05-24 19:18:56',1),(7,3,'iowa city 房子贵么？','中心城区房子价格在多少？','2012-05-24 19:19:20',0),(8,3,'UIUC 地区房子多少钱啊？','不知道香槟地区房子大概在一个什么价位呢？','2012-05-24 19:22:09',5),(9,3,'爱荷华大学一年学费大概多少？','本科生12个学分的话一年大概要花多少学费？','2012-05-24 19:29:04',1),(10,3,'大家都什么时候买机票？','弱问大家都什么时候买机票？另外从奥海尔到学校有多远？ 有人接机么？','2012-05-24 19:32:03',1),(11,4,'大家有关于爱荷华大学或者iowa-city的问题可以问我','RT','2012-05-24 19:40:45',1),(12,1,'你们什么时候分手？我吃醋了！！','再不分我就死给你们看！！','2012-05-24 21:19:42',2),(13,4,'黄一桐你来插一棒子是为了什么？','黄一桐你不是人！！！','2012-05-24 21:21:29',2),(14,5,'铁打的神为什么连饭都忘了吃？','神真是太专注了~~','2012-05-25 11:54:34',0),(15,6,'哈佛大学化学系怎么样','RT','2012-05-25 16:37:45',0),(16,6,'好学校有多难进？','RT','2012-05-26 09:28:11',0),(17,5,'美国前30的学校都有哪些','美国前30的学校都有哪些？','2012-05-26 16:04:40',0),(18,5,'美国30-50的大学有哪些','美国30-50的大学有哪些','2012-05-26 16:16:06',0),(19,5,'美国50-70的大学有哪些','美国50-70的大学有哪些','2012-05-26 16:26:13',0),(20,5,'美国70-100的学校有哪些','美国70-100的学校有哪些','2012-05-26 16:33:28',0),(21,4,'问基情为何物？','为什么呢？','2012-05-26 17:33:38',2),(22,1,'computer science','computer science','2012-05-26 17:44:36',0),(23,1,'computer science','computer science','2012-05-26 17:45:09',2),(24,1,'我是谁？','没有人曾告诉我。。。','2012-05-26 20:54:25',12),(25,3,'去NYSB的黄一桐是gay么？','RT','2012-05-26 20:56:01',0),(26,1,'我的i20到底什么时候来？？','suny sb开始发i20了吗？','2012-05-26 21:16:24',2),(35,1,'test','test','2012-05-31 10:47:33',1),(36,1,'test','test','2012-06-05 19:11:00',0),(37,1,'a','a','2012-06-05 19:26:32',0),(38,1,'b','b','2012-06-05 19:26:56',0),(39,1,'c','c','2012-06-05 19:30:51',0),(40,1,'d','d','2012-06-05 19:31:03',0),(41,1,'e','e','2012-06-06 15:37:48',0),(42,1,'e','e','2012-06-06 15:45:14',0),(43,1,'f','f','2012-06-06 15:47:02',0),(44,1,'e','e','2012-06-07 14:55:59',0),(45,1,'g','g','2012-06-07 16:28:45',0);
/*!40000 ALTER TABLE `questions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reminds`
--

DROP TABLE IF EXISTS `reminds`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reminds` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL COMMENT '被提醒人',
  `question_id` int(11) NOT NULL,
  `question_title` varchar(10) NOT NULL,
  `answer_id` int(11) NOT NULL COMMENT '新的答案',
  `answer_content` varchar(10) NOT NULL,
  `comment_id` int(11) NOT NULL COMMENT '新的评论',
  `comment_content` varchar(10) NOT NULL,
  `has_read` tinyint(4) NOT NULL,
  `create_time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user` (`user_id`,`has_read`,`create_time`)
) ENGINE=MyISAM AUTO_INCREMENT=33 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reminds`
--

LOCK TABLES `reminds` WRITE;
/*!40000 ALTER TABLE `reminds` DISABLE KEYS */;
INSERT INTO `reminds` VALUES (1,1,2,'',24,'',34,'',1,'2012-05-26 16:39:37'),(2,1,2,'',24,'',35,'',1,'2012-05-26 16:40:36'),(3,1,2,'',24,'',36,'',1,'2012-05-26 16:41:11'),(4,1,13,'',11,'',37,'',1,'2012-05-26 16:54:42'),(5,3,9,'',26,'',-1,'',1,'2012-05-26 17:32:55'),(6,4,21,'',27,'',-1,'',1,'2012-05-26 17:34:01'),(7,4,21,'',27,'',38,'',1,'2012-05-26 17:34:18'),(8,4,21,'',27,'',39,'',1,'2012-05-26 17:34:31'),(9,4,21,'',27,'',40,'',1,'2012-05-26 17:34:38'),(10,4,21,'',27,'',41,'',1,'2012-05-26 17:34:45'),(11,3,5,'',28,'',-1,'',0,'2012-05-26 17:36:34'),(12,1,2,'',24,'',42,'',1,'2012-05-26 20:04:12'),(13,1,2,'',24,'',43,'',1,'2012-05-26 20:04:21'),(14,4,21,'',29,'',-1,'',0,'2012-05-26 21:09:53'),(15,1,26,'',30,'',-1,'',1,'2012-05-26 21:17:13'),(16,1,26,'',31,'',-1,'',1,'2012-05-26 21:17:46'),(17,1,24,'',32,'',-1,'',1,'2012-05-29 16:25:26'),(18,1,24,'我是谁？',33,'太年轻了',-1,'',1,'2012-05-29 16:47:08'),(19,1,24,'我是谁？',34,'too simple',-1,'',1,'2012-05-29 16:56:40'),(20,1,24,'我是谁？',35,'so naive',-1,'',1,'2012-05-29 16:59:09'),(21,1,24,'我是谁？',36,'2b',-1,'',1,'2012-05-29 17:02:37'),(22,1,24,'我是谁？',37,'战斗吧，少年！',-1,'',1,'2012-05-29 17:06:45'),(23,1,24,'我是谁？',37,'战斗吧，少年！',44,'好基友',1,'2012-05-29 17:07:28'),(24,1,24,'我是谁？',37,'战斗吧，少年！',45,'回复xys：好朋友',1,'2012-05-29 17:17:09'),(25,1,24,'我是谁？',38,'ohh',-1,'',1,'2012-05-29 17:22:34'),(26,1,24,'我是谁？',39,'aaa',-1,'',1,'2012-05-29 17:23:19'),(27,1,24,'我是谁？',40,'ohh',-1,'',1,'2012-05-29 18:06:33'),(28,1,24,'我是谁？',41,'0hh\r\n',-1,'',1,'2012-05-29 19:48:24'),(29,1,24,'我是谁？',43,'hahah',-1,'',1,'2012-05-30 21:03:32'),(30,1,23,'computer s',44,'hello',-1,'',1,'2012-05-30 21:04:42'),(31,1,23,'computer s',45,'world\r\n',-1,'',1,'2012-05-30 21:09:49'),(32,1,35,'test',46,'helo',-1,'',1,'2012-05-31 10:52:28');
/*!40000 ALTER TABLE `reminds` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resource_tags`
--

DROP TABLE IF EXISTS `resource_tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `resource_tags` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `resource_id` int(11) NOT NULL,
  `tag` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tag` (`tag`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resource_tags`
--

LOCK TABLES `resource_tags` WRITE;
/*!40000 ALTER TABLE `resource_tags` DISABLE KEYS */;
/*!40000 ALTER TABLE `resource_tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resources`
--

DROP TABLE IF EXISTS `resources`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `resources` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `create_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resources`
--

LOCK TABLES `resources` WRITE;
/*!40000 ALTER TABLE `resources` DISABLE KEYS */;
/*!40000 ALTER TABLE `resources` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tag_edits`
--

DROP TABLE IF EXISTS `tag_edits`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tag_edits` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `tag_id` int(11) NOT NULL,
  `description` text NOT NULL,
  `photo` int(11) NOT NULL,
  `create_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tag_edits`
--

LOCK TABLES `tag_edits` WRITE;
/*!40000 ALTER TABLE `tag_edits` DISABLE KEYS */;
INSERT INTO `tag_edits` VALUES (1,1,130,'',1,'2012-06-06 19:41:12'),(2,1,130,'马里兰大学',-1,'2012-06-06 19:52:07'),(3,1,130,'马里兰大学哦',-1,'2012-06-06 19:52:12'),(4,1,1,'不需要解释',-1,'2012-06-08 10:26:05'),(5,1,1,'',1,'2012-06-08 10:29:14');
/*!40000 ALTER TABLE `tag_edits` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tag_follows`
--

DROP TABLE IF EXISTS `tag_follows`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tag_follows` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tag` varchar(50) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `tag` (`tag`)
) ENGINE=MyISAM AUTO_INCREMENT=62 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tag_follows`
--

LOCK TABLES `tag_follows` WRITE;
/*!40000 ALTER TABLE `tag_follows` DISABLE KEYS */;
INSERT INTO `tag_follows` VALUES (57,'SUNY--Stony Brook',1),(7,'马里兰大学',1),(14,'university-of-iowa',3),(13,'经济学',3),(12,'iowa-city',3),(15,'uchicago',3),(22,'iowa-city',4),(23,'university-of-iowa',4),(24,'uchicago',4),(26,'UIUC',1),(28,'UIUC',4),(56,'基情',1),(30,'基情',4),(31,'UIUC',5),(32,'经济学',5),(33,'基情',5),(34,'选房',5),(35,'uchicago',5),(36,'神',5),(37,'iowa-city',6),(42,'DUKE',5),(43,'Emory',5),(44,'University of San Diego',5),(45,'University of California--Davis(UCD)',5),(46,'George Washington University',5),(58,'哲学',1);
/*!40000 ALTER TABLE `tag_follows` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tags`
--

DROP TABLE IF EXISTS `tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tags` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tag` varchar(50) NOT NULL,
  `description` text NOT NULL,
  `create_time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tag` (`tag`)
) ENGINE=MyISAM AUTO_INCREMENT=136 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tags`
--

LOCK TABLES `tags` WRITE;
/*!40000 ALTER TABLE `tags` DISABLE KEYS */;
INSERT INTO `tags` VALUES (1,'2B','不需要解释','2012-06-03 00:07:55'),(2,'American University','','2012-06-03 00:07:55'),(3,'Auburn University','','2012-06-03 00:07:55'),(4,'Baylor University','','2012-06-03 00:07:55'),(5,'Binghamton University--SUNY','','2012-06-03 00:07:55'),(6,'Boston College(BC)','','2012-06-03 00:07:55'),(7,'Boston University(BU)','','2012-06-03 00:07:55'),(8,'Brandeis University','','2012-06-03 00:07:55'),(9,'Brigham Young University--Provo','','2012-06-03 00:07:55'),(10,'Brown','','2012-06-03 00:07:55'),(11,'California Institute of Technology','','2012-06-03 00:07:55'),(12,'Caltech','','2012-06-03 00:07:55'),(13,'Carnegie Mellon','','2012-06-03 00:07:55'),(14,'Case Western Reserve University','','2012-06-03 00:07:55'),(15,'Chicago','','2012-06-03 00:07:55'),(16,'Clark University','','2012-06-03 00:07:55'),(17,'Clemson University','','2012-06-03 00:07:55'),(18,'College of William and Mary','','2012-06-03 00:07:55'),(19,'Colorado School of Mines','','2012-06-03 00:07:55'),(20,'Columbia','','2012-06-03 00:07:55'),(21,'computer','','2012-06-03 00:07:55'),(22,'Cornell','','2012-06-03 00:07:55'),(23,'Dartmouth College','','2012-06-03 00:07:55'),(24,'Drexel University','','2012-06-03 00:07:55'),(25,'Duke','','2012-06-03 00:07:55'),(26,'Emory','','2012-06-03 00:07:55'),(27,'Fordham University','','2012-06-03 00:07:55'),(28,'George Washington University','','2012-06-03 00:07:55'),(29,'Georgetown','','2012-06-03 00:07:55'),(30,'Georgia Institute of Technology(GIT)','','2012-06-03 00:07:55'),(31,'Harvard','','2012-06-03 00:07:55'),(32,'i20','','2012-06-03 00:07:55'),(33,'Indiana University--Bloomington','','2012-06-03 00:07:55'),(34,'iowa','','2012-06-03 00:07:55'),(35,'Iowa State University','','2012-06-03 00:07:55'),(36,'iowa-city','','2012-06-03 00:07:55'),(37,'Johns Hopkins','','2012-06-03 00:07:55'),(38,'Lehigh University','','2012-06-03 00:07:55'),(39,'Marquette University','','2012-06-03 00:07:55'),(40,'Massachusetts Institute of Technology (MIT)','','2012-06-03 00:07:55'),(41,'Miami University--Oxford','','2012-06-03 00:07:55'),(42,'Michigan State University','','2012-06-03 00:07:55'),(43,'MIT','','2012-06-03 00:07:55'),(44,'New York University(NYU)','','2012-06-03 00:07:55'),(45,'Northeastern University','','2012-06-03 00:07:55'),(46,'Northwestern','','2012-06-03 00:07:55'),(47,'Notre Dame','','2012-06-03 00:07:55'),(48,'of','','2012-06-03 00:07:55'),(49,'Ohio State University--Columbus','','2012-06-03 00:07:55'),(50,'Pennsylvania State University--University Park','','2012-06-03 00:07:55'),(51,'Pepperdine University','','2012-06-03 00:07:55'),(52,'Princeton','','2012-06-03 00:07:55'),(53,'Purdue University--West Lafayette','','2012-06-03 00:07:55'),(54,'Rensselaer Polytechnic Institute','','2012-06-03 00:07:55'),(55,'Rice','','2012-06-03 00:07:55'),(56,'Rutgers','','2012-06-03 00:07:55'),(57,'science','','2012-06-03 00:07:55'),(58,'Southern Methodist University','','2012-06-03 00:07:55'),(59,'St. Louis University','','2012-06-03 00:07:55'),(60,'Stanford','','2012-06-03 00:07:55'),(61,'Stevens Institute of Technology','','2012-06-03 00:07:55'),(62,'SUNY College of Environmental Science and Forestry','','2012-06-03 00:07:55'),(63,'SUNY--Stony Brook','','2012-06-03 00:07:55'),(64,'Syracuse University','','2012-06-03 00:07:55'),(65,'test computer science','','2012-06-03 00:07:55'),(66,'Texas A&M University--College Station','','2012-06-03 00:07:55'),(67,'Texas Christian University','','2012-06-03 00:07:55'),(68,'the State University of New Jersey--New Brunswick','','2012-06-03 00:07:55'),(69,'Tufts','','2012-06-03 00:07:55'),(70,'Tulane University','','2012-06-03 00:07:55'),(71,'uchicago','','2012-06-03 00:07:55'),(72,'UIUC','','2012-06-03 00:07:55'),(73,'university','','2012-06-03 00:07:55'),(74,'University of Alabama','','2012-06-03 00:07:55'),(75,'University of California--Berkeley(UCBerkeley)','','2012-06-03 00:07:55'),(76,'University of California--Davis(UCD)','','2012-06-03 00:07:55'),(77,'University of California--Irvine(UCI)','','2012-06-03 00:07:55'),(78,'University of California--Los Angeles(UCLA)','','2012-06-03 00:07:55'),(79,'University of California--Riverside','','2012-06-03 00:07:55'),(80,'University of California--San Diego(UCSD)','','2012-06-03 00:07:55'),(81,'University of California--Santa Barbara(UCSB)','','2012-06-03 00:07:55'),(82,'University of California--Santa Cruz(UCSC)','','2012-06-03 00:07:55'),(83,'University of Colorado--Boulder','','2012-06-03 00:07:55'),(84,'University of Connecticut','','2012-06-03 00:07:55'),(85,'University of Dayton','','2012-06-03 00:07:55'),(86,'University of Delaware','','2012-06-03 00:07:55'),(87,'University of Denver','','2012-06-03 00:07:55'),(88,'University of Florida','','2012-06-03 00:07:55'),(89,'University of Georgia','','2012-06-03 00:07:55'),(90,'University of Illinois--Urbana-Champaign(UIUC)','','2012-06-03 00:07:55'),(91,'University of Iowa','','2012-06-03 00:07:55'),(92,'University of Maryland--College Park（UMD)','','2012-06-03 00:07:55'),(93,'University of Massachusetts--Amherst','','2012-06-03 00:07:55'),(94,'University of Miami','','2012-06-03 00:07:55'),(95,'University of Michigan--Ann Arbor','','2012-06-03 00:07:55'),(96,'University of Minnesota--Twin Cities','','2012-06-03 00:07:55'),(97,'University of Missouri','','2012-06-03 00:07:55'),(98,'University of North Carolina--Chapel Hill (UNC)','','2012-06-03 00:07:55'),(99,'University of Pennsylvania','','2012-06-03 00:07:55'),(100,'University of Pittsburgh','','2012-06-03 00:07:55'),(101,'University of Rochester','','2012-06-03 00:07:55'),(102,'University of San Diego','','2012-06-03 00:07:55'),(103,'University of Southern California(USC)','','2012-06-03 00:07:55'),(104,'University of Texas--Austin','','2012-06-03 00:07:55'),(105,'University of the Pacific','','2012-06-03 00:07:55'),(106,'University of Tulsa','','2012-06-03 00:07:55'),(107,'University of Vermont','','2012-06-03 00:07:55'),(108,'University of Virginia','','2012-06-03 00:07:55'),(109,'University of Washington','','2012-06-03 00:07:55'),(110,'University of Wisconsin--Madison(UWM)','','2012-06-03 00:07:55'),(111,'university-of-iowa','','2012-06-03 00:07:55'),(112,'Vanderbilt','','2012-06-03 00:07:55'),(113,'Virginia Tech','','2012-06-03 00:07:55'),(114,'Wake Forest University','','2012-06-03 00:07:55'),(115,'Washington University in St. Louis(WUSL)','','2012-06-03 00:07:55'),(116,'Worcester Polytechnic Institute','','2012-06-03 00:07:55'),(117,'Yeshiva University','','2012-06-03 00:07:55'),(118,'人生','','2012-06-03 00:07:55'),(119,'分手','','2012-06-03 00:07:55'),(120,'化学','','2012-06-03 00:07:55'),(121,'哲学','','2012-06-03 00:07:55'),(122,'基情','','2012-06-03 00:07:55'),(123,'学费','','2012-06-03 00:07:55'),(124,'排名','','2012-06-03 00:07:55'),(125,'接机','','2012-06-03 00:07:55'),(126,'机票','','2012-06-03 00:07:55'),(127,'神','','2012-06-03 00:07:55'),(128,'经济学','','2012-06-03 00:07:55'),(129,'选房','','2012-06-03 00:07:55'),(130,'马里兰大学','马里兰大学哦','2012-06-03 00:07:55'),(131,'d','d','2012-06-05 19:31:03'),(132,'e','','2012-06-06 15:37:48'),(133,'f','','2012-06-06 15:47:02'),(134,'c','','2012-06-07 14:30:59'),(135,'g','','2012-06-07 14:55:59');
/*!40000 ALTER TABLE `tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(50) NOT NULL,
  `nickname` varchar(32) NOT NULL,
  `passwd` varchar(50) NOT NULL,
  `create_time` datetime NOT NULL,
  `title` varchar(128) NOT NULL,
  `sex` tinyint(4) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `nickname` (`nickname`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'wsxys08@gmail.com','xys','8fee1ee6c6bc22a22f717a4efe3d21e1','2012-05-22 10:19:04','我是要成为海贼王的男人',0),(2,'qiangwang@anjuke.com','qiangwang','e10adc3949ba59abbe56e057f20f883e','2012-05-23 15:12:52','',0),(3,'xiaoshapiu@163.com','urantroiin','d03dc1fff544e159d7cc70d8b5bbf83d','2012-05-24 18:18:12','',0),(4,'daisent@163.com','daisent','d03dc1fff544e159d7cc70d8b5bbf83d','2012-05-24 19:38:13','',0),(5,'hopeyitong@gmail.com','hope','d7083a0df82c9b6d32c00511e7bb7384','2012-05-24 21:24:15','',0),(6,'xm2012application@gmail.com','xiaowangba','d03dc1fff544e159d7cc70d8b5bbf83d','2012-05-25 16:33:53','',0);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2012-06-08 15:41:55
