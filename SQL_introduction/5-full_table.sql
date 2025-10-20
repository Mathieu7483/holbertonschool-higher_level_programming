-- Ce script affiche la description (structure) de la table 'first_table' 
-- de la base de données 'hbtn_0c_0' en interrogeant INFORMATION_SCHEMA.COLUMNS.
-- Cela est fait pour contourner l'interdiction d'utiliser DESCRIBE ou EXPLAIN.

SELECT 
    -- 1. Le nom de la colonne (Field)
    COLUMN_NAME AS Field,
    
    -- 2. Le type de données (Type)
    COLUMN_TYPE AS Type,
    
    -- 3. La capacité à être NULL (Null)
    -- On utilise CASE pour convertir 'YES'/'NO' en la sortie standard de DESCRIBE
    CASE 
        WHEN IS_NULLABLE = 'YES' THEN 'YES'
        ELSE 'NO' 
    END AS 'Null',
    
    -- 4. Le type de clé (Key) : PRI (Primary), UNI (Unique), MUL (Multiple)
    COLUMN_KEY AS 'Key',
    
    -- 5. La valeur par défaut (Default)
    COLUMN_DEFAULT AS 'Default',
    
    -- 6. Les informations supplémentaires (Extra) comme auto_increment
    EXTRA AS Extra
FROM 
    INFORMATION_SCHEMA.COLUMNS
WHERE 
    -- Filtrer sur la base de données spécifiée
    TABLE_SCHEMA = 'hbtn_0c_0'
    -- Filtrer sur la table 'first_table'
    AND TABLE_NAME = 'first_table'
ORDER BY 
    -- S'assurer que l'ordre des colonnes correspond à l'ordre de création
    ORDINAL_POSITION;