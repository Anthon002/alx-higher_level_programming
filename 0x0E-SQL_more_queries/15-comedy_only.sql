-- Displays all comedy shows from the hbtn_0d_tvshows database.
SELECT sh.`title`
  FROM `tv_shows` AS sh
       INNER JOIN `tv_show_genres` AS tsg
       ON sh.`id` = tsg.`show_id`

       INNER JOIN `tv_genres` AS gen
       ON gen.`id` = tsg.`genre_id`
       WHERE gen.`name` = "Comedy"
 ORDER BY sh.`title`;
