-- Displays all genres of the TV show "Dexter" from the hbtn_0d_tvshows database.
SELECT gen.`name`
  FROM `tv_genres` AS gen
       INNER JOIN `tv_show_genres` AS tsg
       ON gen.`id` = tsg.`genre_id`

       INNER JOIN `tv_shows` AS sh
       ON sh.`id` = tsg.`show_id`
       WHERE sh.`title` = "Dexter"
 ORDER BY gen.`name`;
