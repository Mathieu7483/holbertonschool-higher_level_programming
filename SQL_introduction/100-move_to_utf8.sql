-- Script that changes the character set of the database hbtn_0c_0 to utf8mb4
-- and changes the character set of the table first_table and its name column to utf8mb4
-- and utf8mb4_unicode_ci
ALTER DATABASE 
    hbtn_0c_0 
    CHARACTER SET = utf8mb4 
    COLLATE = utf8mb4_unicode_ci;

USE hbtn_0c_0;

ALTER TABLE 
    first_table 
    CONVERT TO CHARACTER SET utf8mb4 
    COLLATE utf8mb4_unicode_ci;

ALTER TABLE 
    first_table 
    MODIFY name VARCHAR(256);