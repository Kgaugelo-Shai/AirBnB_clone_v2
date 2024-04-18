-- Creates a MySQL server with:
-- Create a DATABASE hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create a new USER hbnb_test with password hbnb_test_pwd in localhost
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant all privileges for hbnb_test on hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
-- Grant select privileges for hbnb_test on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
