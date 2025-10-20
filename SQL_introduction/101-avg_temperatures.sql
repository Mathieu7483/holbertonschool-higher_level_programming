-- script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending
USE hbtn_0c_0;
SOURCE temperatures.sql;

SELECT 
    city,
    ROUND(AVG(temperature_value), 4) AS avg_temp
FROM 
    temperatures
GROUP BY
    city
ORDER BY
    avg_temp DESC;
