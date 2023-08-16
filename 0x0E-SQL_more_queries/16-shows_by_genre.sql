-- Displays all shows and their linked genres from the hbtn_0d_tvshows database.
-- Records are ordered by ascending show title and genre name.
SELECT sh.`title`, gen.`name`
  FROM `tv_shows` AS sh
       LEFT JOIN `tv_show_genres` AS tsg
       ON sh.`id` = tsg.`show_id`

       LEFT JOIN `tv_genres` AS gen
       ON tsg.`genre_id` = gen.`id`
 ORDER BY sh.`title`, gen.`name`;
