-- lists all privileges of the MySQL users user_0d_1 and user_0d_2
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.genre_id ORDER BY tv_shows.title, tv_show_genres.genre_id;
