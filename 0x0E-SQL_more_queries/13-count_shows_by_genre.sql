-- script that lists all shows contained in hbtn_0d_tvshows without a genre linked. 
SELECT
	A.title AS genre,
    COUNT(B.genre_id) AS number_of_shows,
	FROM tv_shows AS A
	INNER JOIN tv_show_genres AS B
	ON A.id = B.show_id
	GROUP BY A.title
	ORDER BY number_of_shows DESC;
