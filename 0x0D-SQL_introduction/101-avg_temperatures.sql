-- displays the average temperature 
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city DESC;

