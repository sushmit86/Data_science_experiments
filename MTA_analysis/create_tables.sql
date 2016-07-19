
-- This script loads the data into My sql database

drop table if exists `MTA`.`agency`;

CREATE TABLE if not exists`MTA`.`agency` (
  `agency_id` VARCHAR(45) NULL,
  `agency_name` VARCHAR(45) NULL,
  `agency_url` VARCHAR(45) NULL,
  `agency_timezone` VARCHAR(45) NULL,
  `agency_lang` VARCHAR(45) NULL,
  `agency_phone` VARCHAR(45) NULL);



LOAD DATA LOCAL
INFILE 
'/Users/sushmitroy/MTA_analysis/google_transit/agency.txt'
INTO TABLE MTA.agency 
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;


drop table if exists `MTA`.`calendar_dates`;

CREATE TABLE if not exists `MTA`.`calendar_dates` (
  `service_id` VARCHAR(55) NULL,
  `date` DATETIME NULL,
  `exception_type` INT NULL);
  
LOAD DATA LOCAL
INFILE 
'/Users/sushmitroy/MTA_analysis/google_transit/calendar_dates.txt'
INTO TABLE MTA.calendar_dates 
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

drop table if exists `MTA`.`calendar`;

CREATE TABLE if not exists `MTA`.`calendar` (
  `service_id` VARCHAR(45) NULL,
  `monday` INT NULL,
  `tuesday` INT NULL,
  `wednesday` INT NULL,
  `thursday` INT NULL,
  `friday` INT NULL,
  `saturday` INT NULL,
  `sunday` INT NULL,
  `start_date` DATETIME NULL,
  `end_date` DATETIME NULL);

LOAD DATA LOCAL
INFILE 
'/Users/sushmitroy/MTA_analysis/google_transit/calendar.txt'
INTO TABLE MTA.calendar 
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

drop table if  exists `MTA`.`routes`;

CREATE TABLE if not exists `MTA`.`routes` (
  `route_id` VARCHAR(45) NULL,
  `agency_id` VARCHAR(45) NULL,
  `route_short_name` VARCHAR(45) NULL,
  `route_long_name` VARCHAR(45) NULL,
  `route_desc` VARCHAR(1000) NULL,
  `route_type` INT NULL,
  `route_url` VARCHAR(100) NULL,
  `route_color` VARCHAR(45) NULL,
  `route_text_color` VARCHAR(45) NULL)
  ;
LOAD DATA LOCAL
INFILE 
'/Users/sushmitroy/MTA_analysis/google_transit/routes.txt'
INTO TABLE MTA.routes 
FIELDS TERMINATED BY ','
enclosed by '"' 
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;







drop table if  exists `MTA`.`shapes`;


CREATE TABLE if not exists`MTA`.`shapes` (
  `shape_id` VARCHAR(55) NULL,
  `shape_pt_lat` DECIMAL(11,9) NULL,
  `shape_pt_lon` DECIMAL(11,9) NULL,
  `shape_pt_sequence` INT NULL,
  `shape_dist_traveled` VARCHAR(55) NULL);
  
LOAD DATA LOCAL
INFILE 
'/Users/sushmitroy/MTA_analysis/google_transit/shapes.txt'
INTO TABLE MTA.shapes 
FIELDS TERMINATED BY ','
enclosed by '"' 
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;


drop table if exists `MTA`.`stop_times`;

CREATE TABLE if not exists `MTA`.`stop_times` (
  `trip_id` VARCHAR(100) NULL,
  `arrival_time` TIME NULL,
  `departure_time` TIME NULL,
  `stop_id` VARCHAR(45) NULL,
  `stop_sequence` INT NULL,
  `stop_headsign` VARCHAR(45) NULL,
  `pickup_type` INT NULL,
  `drop_off_type` INT NULL,
  `shape_dist_traveled` VARCHAR(45) NULL);


LOAD DATA LOCAL
INFILE 
'/Users/sushmitroy/MTA_analysis/google_transit/stop_times.txt'
INTO TABLE MTA.stop_times 
FIELDS TERMINATED BY ','
enclosed by '"' 
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;



drop table if exists `MTA`.`stops`;

CREATE TABLE if not exists `MTA`.`stops` (
  `stop_id` VARCHAR(45) NULL,
  `stop_code` VARCHAR(45) NULL,
  `stop_name` VARCHAR(100) NULL,
  `stop_desc` VARCHAR(45) NULL,
  `stop_lat` DECIMAL(12,10) NULL,
  `stop_lon` DECIMAL(12,10) NULL,
  `zone_id` VARCHAR(45) NULL,
  `stop_url` VARCHAR(45) NULL,
  `location_type` INT NULL,
  `parent_station` VARCHAR(45) NULL);

LOAD DATA LOCAL
INFILE 
'/Users/sushmitroy/MTA_analysis/google_transit/stops.txt'
INTO TABLE MTA.stops 
FIELDS TERMINATED BY ','
enclosed by '"' 
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;


drop table if exists `MTA`.`transfers`;

CREATE TABLE if not exists `MTA`.`transfers` (
  `from_stop_id` VARCHAR(45) NULL,
  `to_stop_id` VARCHAR(45) NULL,
  `transfer_type` INT NULL,
  `min_transfer_time` INT NULL);

LOAD DATA LOCAL
INFILE 
'/Users/sushmitroy/MTA_analysis/google_transit/transfers.txt'
INTO TABLE MTA.transfers 
FIELDS TERMINATED BY ','
enclosed by '"' 
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

drop table if exists `MTA`.`trips`;

CREATE TABLE if not exists `MTA`.`trips` (
  `route_id` VARCHAR(45) NULL,
  `service_id` VARCHAR(55) NULL,
  `trip_id` VARCHAR(100) NULL,
  `trip_headsign` VARCHAR(100) NULL,
  `direction_id` INT NULL,
  `block_id` VARCHAR(45) NULL,
  `shape_id` VARCHAR(45) NULL);

LOAD DATA LOCAL
INFILE 
'/Users/sushmitroy/MTA_analysis/google_transit/trips.txt'
INTO TABLE MTA.trips 
FIELDS TERMINATED BY ','
enclosed by '"' 
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;










