-- This SQL script can be used in Visual Studio Code
-- with the MySQL extension (v6.7.0) by Weijan Chen.

-- Create a database
CREATE DATABASE my_database;

-- Use the created database
USE my_database;

-- Create a table named 'Employee' with columns
CREATE TABLE Employee (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    age INT,
    salary FLOAT
);

-- Insert dummy data into the 'Employee' table
INSERT INTO Employee (first_name, last_name, age, salary)
VALUES
    ('John', 'Doe', 30, 50000.00),
    ('Jane', 'Smith', 25, 60000.00),
    ('Michael', 'Johnson', 40, 75000.00);

-- Update salary of an employee
UPDATE Employee
SET salary = 80000.00
WHERE first_name = 'John';

-- Delete an employee
DELETE FROM Employee
WHERE first_name = 'Jane';
