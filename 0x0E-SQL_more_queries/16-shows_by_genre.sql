-- script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
SELECT
	A.title, C.name
	FROM tv_shows AS A
	LEFT JOIN tv_show_genres AS B ON A.id = B.show_id
	LEFT JOIN tv_genres AS C ON B.genre_id = C.id
	ORDER BY A.title, C.name;
