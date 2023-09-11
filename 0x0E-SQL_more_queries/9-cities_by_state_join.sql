-- script to List all cities in the hbtn_0d_usa database
SELECT ci.`id`, ci.`name`, st.`name`
  FROM `cities` AS ci
       INNER JOIN `states` AS st
       ON ci.`state_id` = st.`id`
 ORDER BY ci.`id`;
