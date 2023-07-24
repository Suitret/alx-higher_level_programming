-- script that lists all shows contained in hbtn_0d_tvshows without a genre linked. 
SELECT
	A.name AS genre,
    COUNT(B.genre_id) AS number_of_shows
	FROM tv_genres AS A
	LEFT JOIN tv_show_genres AS B
	ON A.id = B.genre_id
	GROUP BY genre
	HAVING number_of_shows > 0
	ORDER BY number_of_shows DESC;
