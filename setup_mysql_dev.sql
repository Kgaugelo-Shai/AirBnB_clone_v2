-- Prepares a MySQL server with:
-- Database hbnb_dev_db.
-- A new User hbnb_dev with password hbnb_dev_pwd in localhost.
-- Grants all privileges for hbnb_ev on hbnb_dev_db.
-- Grants SELECT privilege for Hbnb_dev on performance.

-- Creates the database if it doesn't exist.
CREATE DATABASE IF NOT EXITS hbnb_dev_db;

-- Create the user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant Privileges on hbnb_devdb
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT Privilege on performance schema
GRANT SELECT ON performance_schema * TO 'hbnb_dev'@'localhost';

-- Flush Privilege
FLUSH PRIVILEGES;
