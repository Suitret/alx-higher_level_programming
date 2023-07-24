-- script that lists all shows contained in hbtn_0d_tvshows without a genre linked. 
SELECT
	tv_shows.title,
    tv_show_genres.genre_id
	FROM tv_shows
	LEFT JOIN tv_show_genres
	WHERE tv_shows.id = tv_show_genres.show_id,
	tv_show_genres.show_id IS NULL
	ORDER BY tv_shows.title, tv_show_genres.genre_id;
