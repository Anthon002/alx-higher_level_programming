-- Displays all TV shows in the hbtn_0d_tvshows database.
SELECT sh.`title`, gen.`genre_id`
  FROM `tv_shows` AS sh
       LEFT JOIN `tv_show_genres` AS gen
       ON sh.`id` = gen.`show_id`
 ORDER BY sh.`title`, gen.`genre_id`;
