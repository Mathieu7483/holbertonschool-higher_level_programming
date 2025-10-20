-- script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending
USE hbtn_0c_0;
SOURCE temperatures.sql;

SELECT 
    city,
    AVG(value) * (9/5) + 32 AS avg_temp_f
FROM 
    temperatures
GROUP BY
    city
ORDER BY
    avg_temp_f DESC;
