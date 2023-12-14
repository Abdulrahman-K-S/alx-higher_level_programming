-- A script that lists all shows contained in `hbtn_0d_tvshows` without a genre linked.
SELECT
	shows.title,
	genres.genre_id
FROM
	tv_shows AS shows,
	tv_show_genres AS genres
WHERE
	shows.id = genres.show_id
	AND
	genres.genre_id is null
ORDER BY
	shows.title,
	genres.genre_id
	ASC
