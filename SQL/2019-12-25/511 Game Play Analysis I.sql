SELECT
    A1.player_id,
    MIN(A1.event_date) AS "first_login"
FROM
    Activity AS A1
GROUP BY A1.player_id
;