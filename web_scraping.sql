/***************************
Setting up the environment
***************************/
DROP DATABASE IF EXISTS metropolis;
CREATE DATABASE metropolis;
USE metropolis;

/***************************
Creating the table 'city'
***************************/
CREATE TABLE City (
    CityId INT AUTO_INCREMENT,
    CityName VARCHAR(45) NOT NULL,
    PRIMARY KEY (CityId)
);

/***************************
Creating the table 'country'
***************************/
CREATE TABLE country (
    CountryId INT AUTO_INCREMENT,
    CountryName VARCHAR(45) NOT NULL,
    CityId INT,
    PRIMARY KEY (CountryId),
    FOREIGN KEY (CityId) REFERENCES City (CityId) 
);

/***************************
Creating the table 'geolocation'
***************************/
CREATE TABLE geolocation (
    LocId INT AUTO_INCREMENT,
    Latitude FLOAT,
    Longitude FLOAT,
    CityId INT,
    PRIMARY KEY (LocId),
    FOREIGN KEY (CityId) REFERENCES City (CityId) 
);

/***************************
Creating the table 'population'
***************************/
CREATE TABLE population (
    FactId INT AUTO_INCREMENT,
    YearDataRetrieved YEAR,
    Population INT,
    CityId INT,
    PRIMARY KEY (FactId),
    FOREIGN KEY (CityId) REFERENCES City (CityId) 
);