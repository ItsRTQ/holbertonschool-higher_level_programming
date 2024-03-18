-- This script list all cities contained in the database hbtn_0d_usa
SELECT city.id, city.name, a.name
FROM cities AS city
INNER JOIN states AS a
ON city.state_id = a.id
ORDER BY city.id;