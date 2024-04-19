-- Creates a MySQL server with:
-- Creates the database if it doesn't exist.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant Privileges on hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Select the database
USE hbnb_dev_db;

-- Grant SELECT Privilege on performance schema
GRANT SELECT ON performance_schema * TO 'hbnb_dev'@'localhost';

-- Flush Privilege
FLUSH PRIVILEGES;
