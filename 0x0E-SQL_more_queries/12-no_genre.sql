-- script that lists all shows contained in hbtn_0d_tvshows without a genre linked. 
SELECT
	tv_shows.title,
    tv_show_genres.genre_id
	FROM tv_shows A
	LEFT JOIN tv_show_genres B
	ON A.id = B.show_id
	WHERE B.show_id IS NULL
	ORDER BY A.title, B.genre_id;
