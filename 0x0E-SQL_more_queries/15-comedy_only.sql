-- script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT
	C.title
	FROM tv_genres AS A
	JOIN tv_show_genres AS B ON A.id = B.genre_id
	JOIN tv_shows AS C ON B.show_id = C.id
	WHERE A.name = 'Comedy'
	ORDER BY C.title ASC;
