-- This script is going to update the bob row score to 10
SELECT name, score
UPDATE second_table
SET score = 10
WHERE name = 'Bob';
