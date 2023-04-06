DROP DATABASE IF EXISTS ProductDbTest;
CREATE DATABASE ProductDbTest;
USE ProductDbTest;

CREATE TABLE Product(
	Pid INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    ProductName VARCHAR(255) NOT NULL,
    ProductDescription VARCHAR(255),
    Category VARCHAR(255) NOT NULL
    );

INSERT INTO Product (ProductName, ProductDescription, Category) VALUES
('Apple iPhone 12', 'A high-end smartphone from Apple', 'Electronics'),
('Samsung Galaxy S21', 'A top-tier Android phone from Samsung', 'Electronics'),
('Sony WH-1000XM4', 'Wireless noise-cancelling headphones', 'Electronics'),
('Fitbit Versa 3', 'A smartwatch with fitness tracking features', 'Fitness'),
('Nike Air Zoom Pegasus 38', 'Running shoes for men', 'Fitness'),
('Yoga Mat', 'A non-slip mat for yoga or other exercise', 'Fitness'),
('Instant Pot Duo Nova', 'A 7-in-1 electric pressure cooker', 'Kitchen'),
('Cuisinart Toaster Oven', 'A compact toaster oven with multiple cooking functions', 'Kitchen'),
('Keurig K-Elite', 'A single-serve coffee maker', 'Kitchen'),
('Nest Learning Thermostat', 'A smart thermostat that learns your preferences', 'Home'),
('Philips Hue Starter Kit', 'A set of smart light bulbs with color-changing capabilities', 'Home'),
('Roomba 980', 'A robot vacuum cleaner', 'Home'),
('Kindle Paperwhite', 'A waterproof e-reader with a high-resolution display', 'Books'),
('Becoming by Michelle Obama', 'A memoir by the former First Lady', 'Books'),
('The Silent Patient by Alex Michaelides', 'A thriller novel', 'Books'),
('PlayStation 5', 'A next-generation gaming console from Sony', 'Entertainment'),
('Xbox Series X', 'A powerful gaming console from Microsoft', 'Entertainment'),
('Nintendo Switch', 'A hybrid console for gaming on the go', 'Entertainment'),
('Canon EOS Rebel T7', 'A DSLR camera with Wi-Fi and NFC connectivity', 'Photography'),
('DJI Mavic Mini', 'A compact drone with a 3-axis gimbal', 'Photography');

    
    