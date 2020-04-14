SELECT 
    ROUND(SUM(IF(a.event_date = b.event_date - 1, 1, 0)) / COUNT(DISTINCT a.player_id), 2) AS 'fraction'
FROM
    (SELECT player_id, MIN(event_date) AS event_date FROM Activity GROUP BY player_id) a 
    JOIN Activity b
    ON a.player_id = b.player_id
;

/* be aware of group by for the calculation !!*/