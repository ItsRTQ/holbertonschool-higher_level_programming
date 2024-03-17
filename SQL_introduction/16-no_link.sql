-- This script list all rows score in descending order that have name
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
