-- Displays all TV shows in the hbtn_0d_tvshows database with at least one associated genre.
SELECT sh.`title`, gen.`genre_id`
  FROM `tv_shows` AS sh
       INNER JOIN `tv_show_genres` AS gen
       ON sh.`id` = gen.`show_id`
 ORDER BY sh.`title`, gen.`genre_id`;
