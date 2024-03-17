-- this will show all the rows from the highest score to the lowest that are >= 10
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
