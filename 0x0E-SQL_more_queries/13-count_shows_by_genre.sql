-- Displays all genres from the hbtn_0d_tvshows database along with the count
SELECT gen.`name` AS `genre`,
       COUNT(*) AS `number_of_shows`
  FROM `tv_genres` AS gen
       INNER JOIN `tv_show_genres` AS tsg
       ON gen.`id` = tsg.`genre_id`
 GROUP BY gen.`name`
 ORDER BY `number_of_shows` DESC;
