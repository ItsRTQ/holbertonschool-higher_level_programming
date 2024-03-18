-- This script list all shows contained in a database
SELECT tv_shows.title, IFNULL(tv_show_genres.g_id, 'NULL') AS g_id
FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.g_id ASC;