CREATE DATABASE IF NOT EXISTS ProductDbTest;
USE ProductDbTest;

CREATE TABLE Product(
	Pid INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    ProductName VARCHAR(255) NOT NULL,
    ProductDescription VARCHAR(255),
    Category VARCHAR(255) NOT NULL
    );

    
    