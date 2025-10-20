-- script that prints the following description of the table first_table from the database hbtn_0c_0 in your MySQL server.
FROM 
    INFORMATION_SCHEMA.COLUMNS
WHERE 
    -- Filtrer sur la base de données spécifiée
    TABLE_SCHEMA = 'hbtn_0c_0'
    -- Filtrer sur la table 'first_table'
    AND TABLE_NAME = 'first_table'