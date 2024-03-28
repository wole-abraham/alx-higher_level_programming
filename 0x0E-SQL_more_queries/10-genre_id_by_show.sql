-- tables
SELECT tv_shows.title as title, tv_show_genres.genres_id as genre_id FROM tv_show JOIN tv_show_genre ON tv_shows.id = tv_show_genres.genre_id ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ;

