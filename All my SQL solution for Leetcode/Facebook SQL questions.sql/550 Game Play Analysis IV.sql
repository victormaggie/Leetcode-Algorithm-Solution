SELECT
    ROUND(
        IFNULL(
            SUM(IF(t.first_date = a.event - 1, 1, 0)) / COUNT(DISTINCT a.player_id)
            ,0)
    ,2) AS fraction
FROM 
    (SELECT player_id, MIN(event_date) AS first_date FROM Activity GROUP BY player_id) t
    LEFT JOIN Activity a 
    ON a.player_id = t.player_id 

/* be aware of group by for the calculation !!*/


