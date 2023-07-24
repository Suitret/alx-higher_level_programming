-- script that lists all the cities of California that can be found in the database hbtn_0d_usa.
WITH my_id AS (SELECT id FROM states WHERE name = 'California') SELECT id, name FROM cities WHERE cities.state_id = my_id GROUP BY name ORDER BY cities.id ASC;
