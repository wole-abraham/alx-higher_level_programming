-- SELEECT ALL WITH THE SAME SCOER
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;

