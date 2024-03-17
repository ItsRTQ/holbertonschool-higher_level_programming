-- This sql script list the row with the same score
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
HAVING COUNT(*) > 1;