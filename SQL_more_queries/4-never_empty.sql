--  Script that creates the table id_not_null on your MySQL server
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT with the default value 1 AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256)
);