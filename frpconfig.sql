/*
Navicat MySQL Data Transfer

Source Server         : localmysql
Source Server Version : 50553
Source Host           : localhost:3306
Source Database       : frpconfig

Target Server Type    : MYSQL
Target Server Version : 50553
File Encoding         : 65001

Date: 2017-10-22 17:20:46
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for alembic_version
-- ----------------------------
DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of alembic_version
-- ----------------------------
INSERT INTO `alembic_version` VALUES ('389069ba1901');

-- ----------------------------
-- Table structure for frp_http
-- ----------------------------
DROP TABLE IF EXISTS `frp_http`;
CREATE TABLE `frp_http` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) DEFAULT NULL,
  `local_ip` varchar(64) DEFAULT NULL,
  `local_port` varchar(64) DEFAULT NULL,
  `use_encryption` tinyint(1) DEFAULT NULL,
  `use_compression` tinyint(1) DEFAULT NULL,
  `http_user` varchar(64) DEFAULT NULL,
  `http_pwd` varchar(64) DEFAULT NULL,
  `subdomain` varchar(64) DEFAULT NULL,
  `custom_domains` varchar(64) DEFAULT NULL,
  `locations` varchar(64) DEFAULT NULL,
  `host_header_rewrite` varchar(64) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `service_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `service_id` (`service_id`),
  KEY `user_id` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of frp_http
-- ----------------------------

-- ----------------------------
-- Table structure for frp_https
-- ----------------------------
DROP TABLE IF EXISTS `frp_https`;
CREATE TABLE `frp_https` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) DEFAULT NULL,
  `local_ip` varchar(64) DEFAULT NULL,
  `local_port` varchar(64) DEFAULT NULL,
  `use_encryption` tinyint(1) DEFAULT NULL,
  `use_compression` tinyint(1) DEFAULT NULL,
  `subdomain` varchar(64) DEFAULT NULL,
  `custom_domains` varchar(64) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `service_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `service_id` (`service_id`),
  KEY `user_id` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of frp_https
-- ----------------------------

-- ----------------------------
-- Table structure for frp_pluginhttp
-- ----------------------------
DROP TABLE IF EXISTS `frp_pluginhttp`;
CREATE TABLE `frp_pluginhttp` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) DEFAULT NULL,
  `remote_port` varchar(64) DEFAULT NULL,
  `plugin_http_user` varchar(64) DEFAULT NULL,
  `plugin_http_passwd` varchar(64) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `service_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `service_id` (`service_id`),
  KEY `user_id` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of frp_pluginhttp
-- ----------------------------

-- ----------------------------
-- Table structure for frp_pluginunixsocket
-- ----------------------------
DROP TABLE IF EXISTS `frp_pluginunixsocket`;
CREATE TABLE `frp_pluginunixsocket` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) DEFAULT NULL,
  `remote_port` varchar(64) DEFAULT NULL,
  `plugin_unix_path` varchar(64) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `service_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `service_id` (`service_id`),
  KEY `user_id` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of frp_pluginunixsocket
-- ----------------------------

-- ----------------------------
-- Table structure for frp_services
-- ----------------------------
DROP TABLE IF EXISTS `frp_services`;
CREATE TABLE `frp_services` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) DEFAULT NULL,
  `server_addr` varchar(64) DEFAULT NULL,
  `server_port` varchar(64) DEFAULT NULL,
  `log_file` varchar(64) DEFAULT NULL,
  `log_level` varchar(64) DEFAULT NULL,
  `log_max_days` varchar(64) DEFAULT NULL,
  `privilege_token` varchar(64) DEFAULT NULL,
  `admin_addr` varchar(64) DEFAULT NULL,
  `admin_port` varchar(64) DEFAULT NULL,
  `admin_user` varchar(64) DEFAULT NULL,
  `admin_pwd` varchar(64) DEFAULT NULL,
  `pool_count` varchar(64) DEFAULT NULL,
  `tcp_mux` varchar(64) DEFAULT NULL,
  `user` varchar(64) DEFAULT NULL,
  `login_fail_exit` varchar(64) DEFAULT NULL,
  `protocol` varchar(64) DEFAULT NULL,
  `start` varchar(128) DEFAULT NULL,
  `heartbeat_interval` varchar(64) DEFAULT NULL,
  `heartbeat_timeout` varchar(64) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_frp_services_user` (`user`),
  KEY `user_id` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of frp_services
-- ----------------------------

-- ----------------------------
-- Table structure for frp_stcp
-- ----------------------------
DROP TABLE IF EXISTS `frp_stcp`;
CREATE TABLE `frp_stcp` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) DEFAULT NULL,
  `sk` varchar(64) DEFAULT NULL,
  `local_ip` varchar(64) DEFAULT NULL,
  `local_port` varchar(64) DEFAULT NULL,
  `use_encryption` tinyint(1) DEFAULT NULL,
  `use_compression` tinyint(1) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `service_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `service_id` (`service_id`),
  KEY `user_id` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of frp_stcp
-- ----------------------------

-- ----------------------------
-- Table structure for frp_stcpvistor
-- ----------------------------
DROP TABLE IF EXISTS `frp_stcpvistor`;
CREATE TABLE `frp_stcpvistor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) DEFAULT NULL,
  `server_name` varchar(64) DEFAULT NULL,
  `sk` varchar(64) DEFAULT NULL,
  `bind_addr` varchar(64) DEFAULT NULL,
  `bind_port` varchar(64) DEFAULT NULL,
  `use_encryption` tinyint(1) DEFAULT NULL,
  `use_compression` tinyint(1) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `service_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `service_id` (`service_id`),
  KEY `user_id` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of frp_stcpvistor
-- ----------------------------

-- ----------------------------
-- Table structure for frp_tcp
-- ----------------------------
DROP TABLE IF EXISTS `frp_tcp`;
CREATE TABLE `frp_tcp` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) DEFAULT NULL,
  `local_ip` varchar(64) DEFAULT NULL,
  `local_port` varchar(64) DEFAULT NULL,
  `use_encryption` tinyint(1) DEFAULT NULL,
  `use_compression` tinyint(1) DEFAULT NULL,
  `remote_port` varchar(64) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `service_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `service_id` (`service_id`),
  KEY `user_id` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of frp_tcp
-- ----------------------------

-- ----------------------------
-- Table structure for frp_udp
-- ----------------------------
DROP TABLE IF EXISTS `frp_udp`;
CREATE TABLE `frp_udp` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) DEFAULT NULL,
  `local_ip` varchar(64) DEFAULT NULL,
  `local_port` varchar(64) DEFAULT NULL,
  `remote_port` varchar(64) DEFAULT NULL,
  `use_encryption` tinyint(1) DEFAULT NULL,
  `use_compression` tinyint(1) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `service_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `service_id` (`service_id`),
  KEY `user_id` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of frp_udp
-- ----------------------------

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `qq_openid` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users
-- ----------------------------
