-- script that lists all shows contained in the database hbtn_0d_tvshows.
SELECT
	A.title,
    B.genre_id
	FROM tv_shows AS A
	LEFT JOIN tv_show_genres AS B
	ON A.id = B.show_id 
	ORDER BY A.title, B.genre_id;
