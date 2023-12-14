-- A script that lists all shows contained in the database `hbtn_0d_tvshows`.
-- If there's a show that doesn't have a genre display `NULL`
SELECT
	shows.title,
	genres.genre_id
FROM
	tv_shows as shows
	LEFT OUTER JOIN
	tv_show_genres AS genres
	ON
	shows.id = genres.show_id
ORDER BY
      shows.title,
      genres.genre_id
      ASC;
