CREATE TABLE `realestate`.`real time data` (
);
CREATE TABLE `realestate`.`real time data` (
  `Id` INT NOT NULL,
  PRIMARY KEY (`Id`));
ALTER TABLE `realestate`.`real time data` 
ADD COLUMN `Location` VARCHAR(45) NULL AFTER `Id`;
ALTER TABLE `realestate`.`real time data` 
CHANGE COLUMN `Id` `` INT NOT NULL ;

SELECT * FROM realestate.`real time data`;
INSERT INTO `realestate`.`real time data` (`Id`, `Location`) VALUES ('1', 'Chennai');
INSERT INTO `realestate`.`real time data` (`Id`, `Location`) VALUES ('12', 'Bengaluru');
