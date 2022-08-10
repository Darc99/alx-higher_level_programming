-- script that displays the average temperature of cities rdered by temperature (descending). --
SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
