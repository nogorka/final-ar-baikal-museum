CREATE TABLE IF NOT EXISTS `Entities` (
	`id` int NOT NULL AUTO_INCREMENT,
	`name` varchar(255) NOT NULL,
	`roomId` int NOT NULL,
	`targetUri` varchar(255) NOT NULL,
	`overlayType` int NOT NULL,
	`overlayUri` varchar(255) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `Rooms` (
	`id` int NOT NULL AUTO_INCREMENT,
	`name` varchar(255) NOT NULL,
	`exsStr` varchar(255), 
	PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `VisitingRecords` (
	`id` int NOT NULL AUTO_INCREMENT,
	`startTime` TIMESTAMP NOT NULL,
	`entityId` int NOT NULL,
	`spentTimeSec` int NOT NULL,
	`visualFeedback` int NOT NULL,
	`description` int NOT NULL,
	`completeness` int NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `PredefinedRoutes` (
	`id` int NOT NULL AUTO_INCREMENT,
	`name` varchar(255) NOT NULL,
	`route` varchar(255) NOT NULL,
	`mapId` int NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `Map` (
	`id` int NOT NULL AUTO_INCREMENT,
	`name` varchar(255) NOT NULL,
	`jsonUri` varchar(255) NOT NULL,
	PRIMARY KEY (`id`)
);

ALTER TABLE `Entities` ADD CONSTRAINT `Entities_fk0` FOREIGN KEY (`roomId`) REFERENCES `Rooms`(`id`);

ALTER TABLE `VisitingRecords` ADD CONSTRAINT `VisitingRecords_fk0` FOREIGN KEY (`entityId`) REFERENCES `Entities`(`id`);

ALTER TABLE `PredefinedRoutes` ADD CONSTRAINT `PredefinedRoutes_fk0` FOREIGN KEY (`mapId`) REFERENCES `Map`(`id`);