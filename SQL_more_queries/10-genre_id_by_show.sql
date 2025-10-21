-- Script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT t.title, s.genre_id
FROM hbtn_0d_tvshows.shows t
JOIN tv_show_genres ON t.id = s.show_id
ORDER BY t.title ASC, s.genre_id ASC;