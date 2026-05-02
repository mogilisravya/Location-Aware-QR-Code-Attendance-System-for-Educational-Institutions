-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: May 22, 2024 at 01:48 PM
-- Server version: 10.4.10-MariaDB
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `location_based_smart_attendance`
--
CREATE DATABASE IF NOT EXISTS `location_based_smart_attendance` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `location_based_smart_attendance`;

-- --------------------------------------------------------

--
-- Table structure for table `attendance_details`
--

DROP TABLE IF EXISTS `attendance_details`;
CREATE TABLE IF NOT EXISTS `attendance_details` (
  `Att_Id` int(11) NOT NULL AUTO_INCREMENT,
  `Student_Name` longtext NOT NULL,
  `Student_Branch` longtext NOT NULL,
  `Student_Subject` longtext NOT NULL,
  `Student_Section` longtext NOT NULL,
  `Student_Rollnum` longtext NOT NULL,
  `Att_Date` date DEFAULT NULL,
  `Att_Status` longtext NOT NULL,
  `Stu_Foregin_id` int(11) DEFAULT NULL,
  `Cla_Foregin_id` int(11) DEFAULT NULL,
  `Cpu` longtext DEFAULT NULL,
  `Ram` longtext DEFAULT NULL,
  `HardDisk` longtext DEFAULT NULL,
  `Class_Incharge` longtext DEFAULT NULL,
  `Class_Time` time(6) DEFAULT NULL,
  `QR_Time` time(6) DEFAULT NULL,
  PRIMARY KEY (`Att_Id`),
  KEY `attendance_details_Stu_Foregin_id_bd0b5bfd` (`Stu_Foregin_id`),
  KEY `attendance_details_Cla_Foregin_id_9e34d999` (`Cla_Foregin_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `attendance_details`
--

INSERT INTO `attendance_details` (`Att_Id`, `Student_Name`, `Student_Branch`, `Student_Subject`, `Student_Section`, `Student_Rollnum`, `Att_Date`, `Att_Status`, `Stu_Foregin_id`, `Cla_Foregin_id`, `Cpu`, `Ram`, `HardDisk`, `Class_Incharge`, `Class_Time`, `QR_Time`) VALUES
(1, 'Ravi kumar', 'ECE', 'Programming', 'A', '20A12345', '2024-05-22', 'present', 1, 1, '28.6', '86.4', ' 150 GiB', 'Seema', '05:15:00.000000', '05:17:00.000000'),
(2, 'Rahman', 'CSE', 'Web Technologies', 'A', '20AB58789', '2024-05-22', 'present', 3, 2, '51.4', '85.8', ' 150 GiB', 'Harry', '06:00:00.000000', '06:08:00.000000'),
(3, 'Rajesh', 'CSE', 'Web Technologies', 'A', '20AB56321', '2024-05-22', 'absent', 4, 2, NULL, NULL, NULL, 'Harry', '06:00:00.000000', NULL),
(4, 'Rahman', 'CSE', 'Web Technologies', 'A', '20AB58789', '2024-05-22', 'absent', 3, 2, NULL, NULL, NULL, 'Harry', '06:00:00.000000', NULL),
(5, 'Rajesh', 'CSE', 'Web Technologies', 'A', '20AB56321', '2024-05-22', 'absent', 4, 2, NULL, NULL, NULL, 'Harry', '06:00:00.000000', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=41 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add student_ details_ model', 7, 'add_student_details_model'),
(26, 'Can change student_ details_ model', 7, 'change_student_details_model'),
(27, 'Can delete student_ details_ model', 7, 'delete_student_details_model'),
(28, 'Can view student_ details_ model', 7, 'view_student_details_model'),
(29, 'Can add class_ details_ model', 8, 'add_class_details_model'),
(30, 'Can change class_ details_ model', 8, 'change_class_details_model'),
(31, 'Can delete class_ details_ model', 8, 'delete_class_details_model'),
(32, 'Can view class_ details_ model', 8, 'view_class_details_model'),
(33, 'Can add attendance_ details_ model', 9, 'add_attendance_details_model'),
(34, 'Can change attendance_ details_ model', 9, 'change_attendance_details_model'),
(35, 'Can delete attendance_ details_ model', 9, 'delete_attendance_details_model'),
(36, 'Can view attendance_ details_ model', 9, 'view_attendance_details_model'),
(37, 'Can add classes_ coducted_ model', 10, 'add_classes_coducted_model'),
(38, 'Can change classes_ coducted_ model', 10, 'change_classes_coducted_model'),
(39, 'Can delete classes_ coducted_ model', 10, 'delete_classes_coducted_model'),
(40, 'Can view classes_ coducted_ model', 10, 'view_classes_coducted_model');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `classes_conduct`
--

DROP TABLE IF EXISTS `classes_conduct`;
CREATE TABLE IF NOT EXISTS `classes_conduct` (
  `Cla_Id` int(11) NOT NULL AUTO_INCREMENT,
  `Class_Inch` longtext DEFAULT NULL,
  `Branch` longtext NOT NULL,
  `Section` longtext NOT NULL,
  `Subject` longtext NOT NULL,
  `Cl_Date` date DEFAULT NULL,
  `Cl_Time` time(6) DEFAULT NULL,
  `Atten_Foregin_id` int(11) DEFAULT NULL,
  `Cla_Foregin_id` int(11) DEFAULT NULL,
  `Stu_Foregin_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`Cla_Id`),
  KEY `classes_conduct_Atten_Foregin_id_b1a0700c` (`Atten_Foregin_id`),
  KEY `classes_conduct_Cla_Foregin_id_e2e8b428` (`Cla_Foregin_id`),
  KEY `classes_conduct_Stu_Foregin_id_fd841924` (`Stu_Foregin_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `classes_conduct`
--

INSERT INTO `classes_conduct` (`Cla_Id`, `Class_Inch`, `Branch`, `Section`, `Subject`, `Cl_Date`, `Cl_Time`, `Atten_Foregin_id`, `Cla_Foregin_id`, `Stu_Foregin_id`) VALUES
(1, 'Seema', 'ECE', 'A', 'Programming', '2024-05-22', '10:15:00.000000', NULL, 1, NULL),
(2, 'Harry', 'CSE', 'A', 'Web Technologies', '2024-05-22', '06:00:00.000000', NULL, 2, NULL),
(3, 'Harry', 'CSE', 'A', 'Web Technologies', '2024-05-22', '06:00:00.000000', NULL, 2, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `class_details`
--

DROP TABLE IF EXISTS `class_details`;
CREATE TABLE IF NOT EXISTS `class_details` (
  `Class_Id` int(11) NOT NULL AUTO_INCREMENT,
  `Class_Incharge_Name` longtext NOT NULL,
  `Subject_Name` longtext DEFAULT NULL,
  `Branch_Name` longtext NOT NULL,
  `Section` longtext NOT NULL,
  `Class_Start_Time` time(6) DEFAULT NULL,
  `Class_End_Time` time(6) DEFAULT NULL,
  `Class_Duration` longtext NOT NULL,
  `Class_Floor_Number` longtext DEFAULT NULL,
  `Class_Room_Number` longtext DEFAULT NULL,
  `Class_Latitude` double DEFAULT NULL,
  `Class_Longitude` double DEFAULT NULL,
  `Class_QR_Code` varchar(100) DEFAULT NULL,
  `Class_QR_Status` longtext NOT NULL,
  `Class_Date` date DEFAULT NULL,
  `Student_Details_Foregin_id` int(11) DEFAULT NULL,
  `Class_Count` int(11) NOT NULL,
  PRIMARY KEY (`Class_Id`),
  KEY `class_details_Student_Details_Foregin_id_6101a50b` (`Student_Details_Foregin_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `class_details`
--

INSERT INTO `class_details` (`Class_Id`, `Class_Incharge_Name`, `Subject_Name`, `Branch_Name`, `Section`, `Class_Start_Time`, `Class_End_Time`, `Class_Duration`, `Class_Floor_Number`, `Class_Room_Number`, `Class_Latitude`, `Class_Longitude`, `Class_QR_Code`, `Class_QR_Status`, `Class_Date`, `Student_Details_Foregin_id`, `Class_Count`) VALUES
(1, 'Seema', 'Programming', 'ECE', 'A', '05:15:00.000000', '11:00:00.000000', '', '2', '205', 17.3521825, 78.549362, 'images/cla_qr/ProgrammingA.png', 'deactive', '2024-05-22', NULL, 1),
(2, 'Harry', 'Web Technologies', 'CSE', 'A', '06:00:00.000000', '06:40:00.000000', '', '2', '203', 17.4375012, 78.4482505, 'images/cla_qr/Web_TechnologiesA_ZmlPcaP.png', 'deactive', '2024-05-22', NULL, 2);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'teacherapp', 'student_details_model'),
(8, 'teacherapp', 'class_details_model'),
(9, 'teacherapp', 'attendance_details_model'),
(10, 'teacherapp', 'classes_coducted_model');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=110 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-05-21 23:39:08.406918'),
(2, 'auth', '0001_initial', '2024-05-21 23:39:08.696753'),
(3, 'admin', '0001_initial', '2024-05-21 23:39:08.769719'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-05-21 23:39:08.784709'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-05-21 23:39:08.802700'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-05-21 23:39:08.859671'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-05-21 23:39:08.890650'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-05-21 23:39:08.921633'),
(9, 'auth', '0004_alter_user_username_opts', '2024-05-21 23:39:08.939623'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-05-21 23:39:08.970603'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-05-21 23:39:08.977600'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-05-21 23:39:08.991592'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-05-21 23:39:09.025575'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-05-21 23:39:09.055557'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-05-21 23:39:09.086540'),
(16, 'auth', '0011_update_proxy_permissions', '2024-05-21 23:39:09.107529'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-05-21 23:39:09.139509'),
(18, 'sessions', '0001_initial', '2024-05-21 23:39:09.166492'),
(19, 'teacherapp', '0001_initial', '2024-05-21 23:39:09.179486'),
(20, 'teacherapp', '0002_alter_student_details_model_student_address_and_more', '2024-05-21 23:39:09.286425'),
(21, 'teacherapp', '0003_student_details_model_student_status_and_more', '2024-05-21 23:39:09.318407'),
(22, 'teacherapp', '0004_alter_student_details_model_student_profile', '2024-05-21 23:39:09.331399'),
(23, 'teacherapp', '0005_alter_student_details_model_student_profile', '2024-05-21 23:39:09.341393'),
(24, 'teacherapp', '0006_alter_student_details_model_student_profile', '2024-05-21 23:39:09.355387'),
(25, 'teacherapp', '0007_alter_student_details_model_student_profile', '2024-05-21 23:39:09.365379'),
(26, 'teacherapp', '0008_class_details_model_and_more', '2024-05-21 23:39:09.384368'),
(27, 'teacherapp', '0009_class_details_model_class_floor_number_and_more', '2024-05-21 23:39:09.459326'),
(28, 'teacherapp', '0010_alter_class_details_model_class_start_time', '2024-05-21 23:39:09.487313'),
(29, 'teacherapp', '0011_student_details_model_student_password', '2024-05-21 23:39:09.506299'),
(30, 'teacherapp', '0012_class_details_model_subject_name', '2024-05-21 23:39:09.524287'),
(31, 'teacherapp', '0013_class_details_model_class_end_time', '2024-05-21 23:39:09.542278'),
(32, 'teacherapp', '0014_student_details_model_student_last_login_date_and_more', '2024-05-21 23:39:09.574258'),
(33, 'teacherapp', '0015_student_details_model_student_no_of_times_login', '2024-05-21 23:39:09.601250'),
(34, 'teacherapp', '0016_student_details_model_student_no_of_times_logout', '2024-05-21 23:39:09.619235'),
(35, 'teacherapp', '0017_alter_student_details_model_student_no_of_times_logout', '2024-05-21 23:39:09.627235'),
(36, 'teacherapp', '0018_alter_student_details_model_student_no_of_times_logout', '2024-05-21 23:39:09.651215'),
(37, 'teacherapp', '0019_student_details_model_student_online_status', '2024-05-21 23:39:09.692191'),
(38, 'teacherapp', '0020_alter_student_details_model_student_password', '2024-05-21 23:39:09.721174'),
(39, 'teacherapp', '0021_class_details_model_class_qr_code', '2024-05-21 23:39:09.743163'),
(40, 'teacherapp', '0022_alter_class_details_model_class_qr_code', '2024-05-21 23:39:09.760152'),
(41, 'teacherapp', '0023_alter_class_details_model_class_qr_code', '2024-05-21 23:39:09.774144'),
(42, 'teacherapp', '0024_alter_class_details_model_class_qr_code', '2024-05-21 23:39:09.788140'),
(43, 'teacherapp', '0025_alter_class_details_model_class_qr_code', '2024-05-21 23:39:09.801131'),
(44, 'teacherapp', '0026_student_details_model_student_upload_qr_codes', '2024-05-21 23:39:09.826114'),
(45, 'teacherapp', '0027_alter_student_details_model_student_upload_qr_codes', '2024-05-21 23:39:09.840107'),
(46, 'teacherapp', '0028_class_details_model_class_qr_status', '2024-05-21 23:39:09.873089'),
(47, 'teacherapp', '0029_alter_student_details_model_student_upload_qr_codes', '2024-05-21 23:39:09.886081'),
(48, 'teacherapp', '0030_student_details_model_class_subject', '2024-05-21 23:39:09.910068'),
(49, 'teacherapp', '0031_alter_class_details_model_class_qr_code', '2024-05-21 23:39:09.924060'),
(50, 'teacherapp', '0032_alter_class_details_model_class_qr_code', '2024-05-21 23:39:09.936054'),
(51, 'teacherapp', '0033_alter_class_details_model_class_qr_code', '2024-05-21 23:39:09.948046'),
(52, 'teacherapp', '0034_alter_class_details_model_class_qr_code_and_more', '2024-05-21 23:39:09.964036'),
(53, 'teacherapp', '0035_alter_class_details_model_class_qr_code_and_more', '2024-05-21 23:39:09.981029'),
(54, 'teacherapp', '0036_alter_class_details_model_class_qr_code_and_more', '2024-05-21 23:39:09.994020'),
(55, 'teacherapp', '0037_alter_class_details_model_class_qr_code_and_more', '2024-05-21 23:39:10.007011'),
(56, 'teacherapp', '0038_alter_class_details_model_class_qr_code_and_more', '2024-05-21 23:39:10.020006'),
(57, 'teacherapp', '0039_alter_class_details_model_class_qr_code', '2024-05-21 23:39:10.032998'),
(58, 'teacherapp', '0040_alter_class_details_model_class_qr_code', '2024-05-21 23:39:10.040992'),
(59, 'teacherapp', '0041_alter_class_details_model_class_qr_code', '2024-05-21 23:39:10.053985'),
(60, 'teacherapp', '0042_alter_class_details_model_class_qr_code', '2024-05-21 23:39:10.065978'),
(61, 'teacherapp', '0043_alter_class_details_model_class_qr_code', '2024-05-21 23:39:10.078970'),
(62, 'teacherapp', '0044_alter_class_details_model_class_qr_code', '2024-05-21 23:39:10.087966'),
(63, 'teacherapp', '0045_alter_class_details_model_class_qr_code', '2024-05-21 23:39:10.099960'),
(64, 'teacherapp', '0046_student_details_model_student_qr_code_upload_time', '2024-05-21 23:39:10.127951'),
(65, 'teacherapp', '0047_rename_student_qr_code_upload_time_student_details_model_student_qr_code_upload_time', '2024-05-21 23:39:10.147943'),
(66, 'teacherapp', '0048_class_details_model_class_date', '2024-05-21 23:39:10.170919'),
(67, 'teacherapp', '0049_student_details_model_student_qr_code_upload_date', '2024-05-21 23:39:10.195904'),
(68, 'teacherapp', '0050_student_details_model_student_qr_status', '2024-05-21 23:39:10.229887'),
(69, 'teacherapp', '0051_delete_student_details_model', '2024-05-21 23:39:10.244876'),
(70, 'teacherapp', '0052_student_details_model', '2024-05-21 23:39:10.296847'),
(71, 'teacherapp', '0053_alter_student_details_model_class_details_foregin', '2024-05-21 23:39:17.266510'),
(72, 'teacherapp', '0054_remove_student_details_model_class_details_foregin_and_more', '2024-05-21 23:39:20.086876'),
(73, 'teacherapp', '0055_class_details_model', '2024-05-21 23:39:20.126852'),
(74, 'teacherapp', '0056_alter_class_details_model_student_details_foregin', '2024-05-21 23:39:23.147271'),
(75, 'teacherapp', '0057_student_details_model_qr_latitude_and_more', '2024-05-21 23:39:23.181250'),
(76, 'teacherapp', '0058_student_details_model_student_last_logout_time', '2024-05-21 23:39:23.200240'),
(77, 'teacherapp', '0059_student_details_model_att_chemistry_and_more', '2024-05-21 23:39:23.302379'),
(78, 'teacherapp', '0060_student_details_model_att_english', '2024-05-21 23:39:23.327379'),
(79, 'teacherapp', '0061_attendance_details_model', '2024-05-21 23:39:23.336355'),
(80, 'teacherapp', '0062_rename_stu_id_attendance_details_model_att_id_and_more', '2024-05-21 23:39:23.381332'),
(81, 'teacherapp', '0063_attendance_details_model_cla_foregin', '2024-05-21 23:39:23.414312'),
(82, 'teacherapp', '0064_alter_class_details_model_student_details_foregin', '2024-05-21 23:39:23.424305'),
(83, 'teacherapp', '0065_remove_class_details_model_student_details_foregin', '2024-05-21 23:39:26.408726'),
(84, 'teacherapp', '0066_class_details_model_student_details_foregin', '2024-05-21 23:39:26.444704'),
(85, 'teacherapp', '0067_alter_class_details_model_student_details_foregin', '2024-05-21 23:39:26.455698'),
(86, 'teacherapp', '0068_remove_class_details_model_student_details_foregin', '2024-05-21 23:39:29.365147'),
(87, 'teacherapp', '0069_class_details_model_student_details_foregin', '2024-05-21 23:39:29.403126'),
(88, 'teacherapp', '0070_student_details_model_cpu', '2024-05-21 23:39:29.430110'),
(89, 'teacherapp', '0071_remove_student_details_model_cpu_and_more', '2024-05-21 23:39:29.486080'),
(90, 'teacherapp', '0072_attendance_details_model_ram', '2024-05-21 23:39:29.508067'),
(91, 'teacherapp', '0073_attendance_details_model_harddisk', '2024-05-21 23:39:29.529053'),
(92, 'teacherapp', '0074_class_details_model_class_count', '2024-05-21 23:39:29.550041'),
(93, 'teacherapp', '0075_alter_class_details_model_class_count', '2024-05-21 23:39:29.577026'),
(94, 'teacherapp', '0076_attendance_details_model_class_incharge', '2024-05-21 23:39:29.598018'),
(95, 'teacherapp', '0077_alter_attendance_details_model_class_incharge', '2024-05-21 23:39:29.619002'),
(96, 'teacherapp', '0078_attendance_details_model_class_time_and_more', '2024-05-21 23:39:29.653984'),
(97, 'teacherapp', '0079_attendance_details_model_qr_time', '2024-05-21 23:39:29.673971'),
(98, 'teacherapp', '0080_classes_coducted_model', '2024-05-21 23:39:29.730939'),
(99, 'teacherapp', '0081_remove_classes_coducted_model_stu_foregin', '2024-05-21 23:39:32.838340'),
(100, 'teacherapp', '0082_classes_coducted_model_class_inch', '2024-05-21 23:39:32.864326'),
(101, 'teacherapp', '0083_classes_coducted_model_atten_foregin_and_more', '2024-05-21 23:39:32.923292'),
(102, 'teacherapp', '0084_student_details_model_class_date', '2024-05-21 23:39:32.946278'),
(103, 'teacherapp', '0085_remove_student_details_model_att_chemistry_and_more', '2024-05-21 23:39:33.093197'),
(104, 'teacherapp', '0086_student_details_model_class_time', '2024-05-21 23:39:33.115185'),
(105, 'teacherapp', '0087_delete_classes_coducted_model', '2024-05-21 23:39:33.121181'),
(106, 'teacherapp', '0088_student_details_model_student_latitude_and_more', '2024-05-21 23:39:33.156162'),
(107, 'teacherapp', '0089_class_details_model_class_status', '2024-05-21 23:39:33.181145'),
(108, 'teacherapp', '0090_remove_class_details_model_class_status', '2024-05-21 23:39:33.199136'),
(109, 'teacherapp', '0091_classes_coducted_model', '2024-05-21 23:39:33.277101');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('8ychivqg1py3c3olftap0ngzx8v1ke1f', 'eyJTdHVkZW50X0lkIjozfQ:1s9b6J:BuVIm6LFC-55XizBvist8ax4CNZsULAtyCzP4o5uqtU', '2024-06-05 01:49:07.188562');

-- --------------------------------------------------------

--
-- Table structure for table `student_details`
--

DROP TABLE IF EXISTS `student_details`;
CREATE TABLE IF NOT EXISTS `student_details` (
  `Student_Id` int(11) NOT NULL AUTO_INCREMENT,
  `Student_Name` longtext NOT NULL,
  `Student_Age` int(11) DEFAULT NULL,
  `Student_Email` varchar(100) NOT NULL,
  `Student_Phone_Number` longtext DEFAULT NULL,
  `Student_RollNumber` longtext DEFAULT NULL,
  `Student_Address` longtext DEFAULT NULL,
  `Student_Branch` longtext DEFAULT NULL,
  `Student_Section` longtext DEFAULT NULL,
  `Student_Gender` longtext DEFAULT NULL,
  `Student_Profile` varchar(100) NOT NULL,
  `Student_Status` longtext NOT NULL,
  `Student_Password` longtext DEFAULT NULL,
  `Student_Last_Login_Time` time(6) DEFAULT NULL,
  `Student_Last_Login_Date` date DEFAULT NULL,
  `Student_No_Of_Times_Login` int(11) DEFAULT NULL,
  `Student_No_Of_Times_Logout` int(11) DEFAULT NULL,
  `Student_Online_Status` longtext NOT NULL,
  `Student_Upload_QR_Codes` varchar(100) DEFAULT NULL,
  `Class_Subject` longtext DEFAULT NULL,
  `Student_QR_Code_Upload_Time` time(6) DEFAULT NULL,
  `Student_QR_Code_Upload_Date` date DEFAULT NULL,
  `Student_QR_Status` longtext NOT NULL,
  `Student_Last_Logout_Time` time(6) DEFAULT NULL,
  `Class_Date` date DEFAULT NULL,
  `Class_Inch_Name` longtext DEFAULT NULL,
  `Class_Time` time(6) DEFAULT NULL,
  `Student_Latitude` double DEFAULT NULL,
  `Student_Longitude` double DEFAULT NULL,
  PRIMARY KEY (`Student_Id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student_details`
--

INSERT INTO `student_details` (`Student_Id`, `Student_Name`, `Student_Age`, `Student_Email`, `Student_Phone_Number`, `Student_RollNumber`, `Student_Address`, `Student_Branch`, `Student_Section`, `Student_Gender`, `Student_Profile`, `Student_Status`, `Student_Password`, `Student_Last_Login_Time`, `Student_Last_Login_Date`, `Student_No_Of_Times_Login`, `Student_No_Of_Times_Logout`, `Student_Online_Status`, `Student_Upload_QR_Codes`, `Class_Subject`, `Student_QR_Code_Upload_Time`, `Student_QR_Code_Upload_Date`, `Student_QR_Status`, `Student_Last_Logout_Time`, `Class_Date`, `Class_Inch_Name`, `Class_Time`, `Student_Latitude`, `Student_Longitude`) VALUES
(1, 'Ravi kumar', 25, 'ravi@gmail.com', '9876543210', '20A12345', 'ameerpet', 'ECE', 'A', 'Male', 'images/face16.jpg', 'accepted', 'aOqQ', '05:15:00.000000', '2024-05-22', 1, 1, 'offline', 'images/stu_qr/ProgrammingA_f2hjAjp.png', '', '05:17:00.000000', '2024-05-22', 'not-uploaded', '05:18:00.000000', '2024-05-22', 'Seema', '10:15:00.000000', NULL, NULL),
(2, 'Fazal', 25, 'fazalsirmail@gmail.com', '8555887986', '20AC5456', 'hyderabad', 'CSE', 'B', 'Male', 'images/face21.jpg', 'accepted', 'qarG', NULL, NULL, 0, 0, 'offline', '', NULL, NULL, NULL, 'not-uploaded', NULL, NULL, NULL, NULL, NULL, NULL),
(3, 'Rahman', 26, 'fazalsirprojects@gmail.com', '9912221087', '20AB58789', 'malakpet', 'CSE', 'A', 'Male', 'images/face24.jpg', 'accepted', 'znLQ', '07:19:00.000000', '2024-05-22', 2, 2, 'offline', 'images/stu_qr/Web_TechnologiesA_P1ZP5DY.png', '', '06:08:00.000000', '2024-05-22', 'not-uploaded', '07:19:00.000000', '2024-05-22', 'Harry', '06:00:00.000000', NULL, NULL),
(4, 'Rajesh', 24, 'ai1in@gmail.com', '9912221087', '20AB56321', 'ameerpet', 'CSE', 'A', 'Male', 'images/face18.jpg', 'accepted', 'zIYk', '06:10:00.000000', '2024-05-22', 1, 1, 'offline', 'images/stu_qr/Web_TechnologiesA_1.png', '', '06:13:00.000000', '2024-05-22', 'not-uploaded', '06:16:00.000000', '2024-05-22', 'Harry', '06:00:00.000000', NULL, NULL);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
