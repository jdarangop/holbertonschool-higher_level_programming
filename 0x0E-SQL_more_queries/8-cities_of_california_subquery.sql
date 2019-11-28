-- lists all privileges of the MySQL users user_0d_1 and user_0d_2
SELECT * FROM cities WHERE state_id = (SELECT id FROM states WHERE name = "California") ORDER BY cities.id ASC;
