-- Script that displays the maw teamperature of each state ordered by state name
SELECT
    state,
    ROUND(MAX(value), 4) AS max_temp
FROM
    temperatures
GROUP BY
    state
ORDER BY
    state ASC;