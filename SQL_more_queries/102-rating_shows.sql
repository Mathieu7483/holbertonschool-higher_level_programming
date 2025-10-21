-- Script that lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT tv_shows.title, SUM (tv_show_rate)
FROM tv_shows
JOIN tv_show_rate ON tv_shows.id = tv_show_rate.show_id
GROUP BY tv_shows.title
ORDER BY rate DESC;
