SELECT
    ROUND(SUM( CASE WHEN a.event_date = b.event_date -1 THEN 1 ELSE 0 END) / COUNT(DISTINCT a.player_id), 2) AS 'fraction'
FROM (
    SELECT player_id, MIN(event_date) AS event_date
    FROM   Activity
    GROUP BY player_id) As a 
JOIN Activity AS b
ON a.player_id = b.player_id
;
