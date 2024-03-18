-- This script all shows contained in hbtn_0d_tvshows
SELECT show.title, num.genre_id
FROM tv_shows AS show
INNER JOIN tv_show_genres AS num
ON show.id = num.show_id
ORDER BY show.title, num.genre_id;