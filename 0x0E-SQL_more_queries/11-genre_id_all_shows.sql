-- script that lists all shows contained in the database hbtn_0d_tvshows.
SELECT
	tv_shows.title,
	CASE
        WHEN tv_show_genres.genre_id IS NOT NULL THEN tv_show_genres.genre_id
		ELSE NULL
    END AS 'genre_id'
	FROM tv_shows
	JOIN tv_show_genres
	WHERE tv_shows.id = tv_show_genres.show_id 
	ORDER BY tv_shows.title, tv_show_genres.genre_id;
