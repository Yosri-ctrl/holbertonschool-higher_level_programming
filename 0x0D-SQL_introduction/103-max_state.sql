-- Temperatures #2
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
LIMIT 3;