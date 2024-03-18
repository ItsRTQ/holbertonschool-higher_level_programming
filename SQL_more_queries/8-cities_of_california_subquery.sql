-- This script list all cities of California that can be found in set database
SELECT id, name
FROM cities
WHERE state_id IN (SELECT id FROM states WHERE name = "California") ORDER BY id;
