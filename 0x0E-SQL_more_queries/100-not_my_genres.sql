-- script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT
	C.name
	FROM tv_shows AS A
	JOIN tv_show_genres AS B ON A.id = B.show_id
	JOIN tv_genres AS C ON B.genre_id = C.id
	WHERE A.title = 'Dexter'
	ORDER BY C.name ASC;
