-- script that lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT tv_shows.title, tv_ratings.rating
FROM tv_shows
JOIN tv_ratings ON tv_shows.id = tv_ratings.show_id
ORDER BY tv_ratings.rating DESC;
