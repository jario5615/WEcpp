DROP DATABASE IF EXISTS ProductDbTest;
CREATE DATABASE ProductDbTest;
USE ProductDbTest;

CREATE TABLE Product(
    Pid INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    ProductName VARCHAR(255) NOT NULL,
    ProductDescription VARCHAR(255),
    Category VARCHAR(255) NOT NULL,
    Price FLOAT(2) NOT NULL
);

INSERT INTO Product (ProductName, ProductDescription, Category, Price) VALUES
('Apple iPhone 12', 'A high-end smartphone from Apple', 'Electronics', 999.00),
('Samsung Galaxy S21', 'A top-tier Android phone from Samsung', 'Electronics', 799.00),
('Sony WH-1000XM4', 'Wireless noise-cancelling headphones', 'Electronics', 349.99),
('Fitbit Versa 3', 'A smartwatch with fitness tracking features', 'Fitness', 229.95),
('Nike Air Zoom Pegasus 38', 'Running shoes for men', 'Fitness', 119.99),
('Yoga Mat', 'A non-slip mat for yoga or other exercise', 'Fitness', 29.99),
('Instant Pot Duo Nova', 'A 7-in-1 electric pressure cooker', 'Kitchen', 99.99),
('Cuisinart Toaster Oven', 'A compact toaster oven with multiple cooking functions', 'Kitchen', 129.95),
('Keurig K-Elite', 'A single-serve coffee maker', 'Kitchen', 169.99),
('Nest Learning Thermostat', 'A smart thermostat that learns your preferences', 'Home', 249.00),
('Philips Hue Starter Kit', 'A set of smart light bulbs with color-changing capabilities', 'Home', 139.99),
('Roomba 980', 'A robot vacuum cleaner', 'Home', 899.99),
('Kindle Paperwhite', 'A waterproof e-reader with a high-resolution display', 'Books', 129.99),
('Becoming by Michelle Obama', 'A memoir by the former First Lady', 'Books', 14.50),
('The Silent Patient by Alex Michaelides', 'A thriller novel', 'Books', 18.99),
('PlayStation 5', 'A next-generation gaming console from Sony', 'Entertainment', 499.99),
('Xbox Series X', 'A powerful gaming console from Microsoft', 'Entertainment', 499.99),
('Nintendo Switch', 'A hybrid console for gaming on the go', 'Entertainment', 299.99),
('Canon EOS Rebel T7', 'A DSLR camera with Wi-Fi and NFC connectivity', 'Photography', 599.00),
('DJI Mavic Mini', 'A compact drone with a 3-axis gimbal', 'Photography', 399.00);
