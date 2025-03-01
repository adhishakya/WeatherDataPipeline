CREATE DATABASE IF NOT EXISTS `weather`;
USE `weather`;
CREATE TABLE weather_data(
    id int PRIMARY KEY AUTO_INCREMENT,
    name varchar(255),
    temperature float,
    weather_type varchar(255),
    weather_description varchar(255),
    pressure float,
    humidity float,
    response_timestamp timestamp,
    stored_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);